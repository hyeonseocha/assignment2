"""Your Track A recipe: how the fixed model is trained on your selection.

src/official.py imports this file and calls the functions below. Change
anything in it. The grader copies this one file and your selection.csv to its
own computer and runs src/official.py with them, so everything your recipe
needs has to be in this file: it cannot read other files, download anything,
or load another model.

What you cannot change, because official.py decides it:
  - the model: ResNet18 with the ImageNet weights, a new last layer of 5
  - the photos: only the ones in selection.csv, with the city of their folder
  - how many photos go through the network in training: rules.TRACK_A_BUDGET
    (250,000). A bigger batch means fewer steps, not more photos.
  - the image size the model sees, 224 x 224
  - mixed precision (float16), and the seed

This is the recipe the starter code came with, with one change to how the
photos are drawn (sample_weights below), made in two steps. The score is the
accuracy in each city averaged over the five cities, so every city is worth a
fifth, but the photos are not: Tokyo has 13,310 of them and Busan 5,174, so
drawn in proportion Tokyo comes up nearly three times as often as Busan. The
first step is that every city is now drawn equally often. The second step is
that, inside a city, the three kinds of photo (commons, youtube, osv5m) are
drawn more evenly than they occur, because the photos the grader scores are not
mixed like the photos we train on: the leaderboard photos are all frames of
YouTube walking and driving videos, the final photos are street photos taken
with a phone, and two thirds of our own photos are commons. On top of that the
kind of photo says a lot about the city (Busan has no osv5m photo at all, Seoul
320 and Tokyo 1,916), so a model can learn "commons means Tokyo, osv5m means
Osaka", look good on our own photos, and still miss the leaderboard: there
Busan and Taipei are close to guessing (0.19 and 0.22) while on our own
validation photos they are 0.40 and 0.54. The second step is done by halves,
one over the square root of the count: drawing Seoul's 320 street-view photos a
third of the time would repeat each of them 52 times in 250,000 draws, while by
halves they come up about 4.6 times as often as Seoul's commons photos instead
of 21 times.
"""

import collections
import math

import torch
import torch.nn.functional as F
from torchvision import transforms as T

BATCH_SIZE = 64


def train_transform():
    """A function that turns one training photo (a PIL image) into a 224 x 224 one.

    It may return a PIL image or a float tensor (3, 224, 224) with values
    0..1. official.py normalises it afterwards. It runs once every time a
    photo is drawn, so the same photo looks different every time.
    """
    return T.Compose([
        T.RandomResizedCrop(224, scale=(0.35, 1.0)),
        T.RandomHorizontalFlip(),
        T.ColorJitter(0.2, 0.2, 0.2),
    ])


def _kind(path):
    """commons, osv5m or youtube: where the photo came from, from its file name."""
    return path.replace("\\", "/").split("/")[-1].split("_")[0]


def sample_weights(cities, paths):
    """How often each photo in your selection is drawn.

    cities and paths are lists, one entry per row of selection.csv. Return a
    list of positive numbers of the same length, where a photo with weight 2
    is drawn twice as often as one with weight 1. Return None to go through
    the selection in a new random order each time, every photo once per round.

    Every city comes up equally often, and inside a city a photo is drawn one
    over the square root of the number of photos of its kind in that city: the
    city's photos add up to one however many kinds it has, and a rare kind is
    drawn more often than it occurs, but only by the square root.
    """
    kinds = collections.Counter((c, _kind(p)) for c, p in zip(cities, paths))
    spread = collections.Counter()
    for (c, kind), n in kinds.items():
        spread[c] += math.sqrt(n)
    return [
        1.0 / (spread[c] * math.sqrt(kinds[(c, _kind(p))]))
        for c, p in zip(cities, paths)
    ]


def make_optimizer(model):
    return torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)


def make_scheduler(optimizer, total_steps):
    """Stepped once after every training step. total_steps is BUDGET // BATCH_SIZE."""
    return torch.optim.lr_scheduler.OneCycleLR(
        optimizer, max_lr=3e-4, total_steps=total_steps, pct_start=0.15)


def mix(images, labels):
    """Change a batch on the GPU before the model sees it.

    images is (BATCH_SIZE, 3, 224, 224), normalised; labels is (BATCH_SIZE,)
    city numbers. Return images of the same shape and the targets for
    loss_fn: the labels, or probabilities (BATCH_SIZE, 5) if you mix photos.
    """
    return images, labels


def loss_fn(logits, targets):
    return F.cross_entropy(logits, targets, label_smoothing=0.1)


def on_step(step, total_steps, model, optimizer):
    """Called after every step, with the step number from 0. Returns nothing."""


def final_model(model):
    """The model to hand in, at the end of training. It must still be the same ResNet18."""
    return model
