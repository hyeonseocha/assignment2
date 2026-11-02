# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 1 November, before any training: what tells the cities apart (Track A)

Looked at `results/curate/look_<city>_NN.png` (48 photos per sheet, number and
file name under each photo). My own notes, in my own words:

**Busan**
- 글자: 한글, 영어로 "Busan ... Festival"이라고 쓴 글
- 도로·차량: 바다를 가로지르는 다리가 보임, 열차, 갓길에 차량이나 오토바이가 세워져 있음, 우측통행
- 건물: 아파트, 한옥(기와집? 절처럼 생긴 건물), 알록달록한 집(감천문화마을)
- 지형: 바다, 해변, 포장되어 있는 인도, 산책로
- 사진의 종류: commons, youtube
- "이건 아니다": 동물 사진(앵무새?), 차량 전시 사진

**Osaka**
- 글자: 일본어, "Osaka ..." 라고 쓴 영어
- 도로·차량: 좌측 보행, 자기부상열차, 열차(지하철?)
- 건물: 일본식 성, 높은 건물이 밀집, 네온사인이 가득한 건물
- 지형: 산이 없음, 사진이 선명해 보임, 맑아 보임, 물(바다인지 호수인지 강인지 모르겠음)이 있고 배를 탐
- 사진의 종류: commons, youtube
- "이건 아니다": 꽃 사진, 인형 사진, 마네킹 사진

**Taipei**
- 하늘이 맑다, 중국어? 를 쓴다, 중화권 성(castle), 오토바이, 나무나 풀 많음, 색감이 좀 뿌옇다

**Seoul**
- 글자: 한국어, "Seoul"
- 도로·차량: 따릉이, 우측 통행, 지하철, 버스
- 건물: 한옥, 높은 빌딩
- 지형: 산이 있다, 뭔가 푸릇푸릇함

**Tokyo**
- 회색이 많은 느낌, 후지산, 길에 주차된 차나 자전거 같은 게 없음, 좌측 통행, 높은 건물이 많음

**What surprised me**
- 도쿄와 오사카는 차가 왼쪽으로 다니고 서울·부산은 오른쪽이라, 사진을 좌우로 뒤집으면 도시를 가르는 단서가 사라질 수도 있겠다

**A rule I want to try from this**
- 부산 시트의 앵무새·차량 전시 사진, 오사카 시트의 꽃·인형·마네킹처럼 길 사진이 아닌 것은 학습에서 빼본다

Counts in the training folder (measured from `data/starter/train`, not an
opinion — I ran a count to check what I saw):

| city | photos | commons | youtube | osv5m |
|---|---|---|---|---|
| seoul | 11,274 | 6,770 | 4,184 | 320 |
| busan | 5,191 | 3,487 | 1,704 | 0 |
| tokyo | 13,347 | 6,975 | 4,456 | 1,916 |
| osaka | 7,200 | 5,347 | 1,512 | 341 |
| taipei | 7,245 | 5,668 | 1,044 | 533 |

- Busan has no `osv5m` (street-view) photos at all, Tokyo has 1,916.
- Taipei is only 14% youtube frames; Seoul is 37%.
- So a city can also be told apart by the camera it was shot on, which is not
  what the grader wants the model to learn.

## 1 November baseline seed 0 (Track A)
- changed: nothing; the starter recipe, on all 44,257 training photos
- why: 내가 앞으로 바꾸는 것들이 정말 나아진 건지 비교할 기준이 필요해서.
- validation: 0.497 (before: none, this is the first run)
- what it means: 오사카와 도쿄를 이렇게 많이 헷갈릴 줄은 몰랐다. 내가 봐도 오사카인지
  도쿄인지 구분이 안 되는 사진이 많았다.

## 1 November baseline seed 1 (Track A)
- changed: nothing; the same recipe again, only the seed is different
- why: 점수가 그냥 우연으로 나온 건지 궁금했고, 한 번 더 돌려서 확실히 해보고
  싶었다.
- validation: 0.491 (before: 0.497 with seed 0)
- what it means: 도쿄와 오사카 점수가 seed에 따라 0.03씩 서로 뒤집힌 걸 보면
  0.4965와 0.4913의 차이는 우연이라고 본다. 앞으로는 노이즈 범위를 벗어나는
  **전체 점수 0.015 이상 상승**이 있거나, 오사카·부산처럼 약한 도시의 점수가
  **0.03 이상 안정적으로** 올랐을 때 "성능이 좋아졌다"고 말하겠다.

### What the baseline's mistakes have in common (my own words)

I looked at all five sheets, `results/curate/mistakes_baseline_seed0_<city>_00.png`
(48 photos each, the ones the model was most sure about and still got wrong).

- 이 도시에만 있는 것이 보이면 맞히는데, 어디에나 있는 도로·낮은 건물(7층 이하)·인도 뷰만 보이면 구분을 못한다. 서울↔부산이 특히 그렇고, 도쿄↔오사카도 거리·인도 뷰에서 헷갈리며, 타이베이도 그냥 번화가 길거리면 헷갈린다.
- 확대(줌)된 사진, 즉 길 전체가 아니라 일부만 크게 보이는 사진도 구분을 못한다.

## 2 November wide_crop (Track A)
- changed: 학습 사진을 잘라내는 범위를 0.35에서 0.6으로 넓혀서, 사진의 최소 60%가
  남게 했다. 다른 것은 하나도 그대로.
- why: 채점기가 줌을 하지 않는다는 것을 발견한 것도 있지만, 너무 좁게 크롭해서
  학습하면 그 사진이 무엇인지 알려주는 배경 정보가 너무 없다고 생각해서 바꿔본
  거였다.
- validation: 0.490 (before: 0.494, baseline 두 번의 평균)
- what it means: 개선은 아니다. 오사카가 0.336 → 0.381로 +0.045 올랐지만 도쿄가
  0.647 → 0.596으로 −0.051 떨어져서, 한쪽 클래스의 희생을 동반한 결과였다.
  앞으로 이렇게 한쪽 클래스의 희생이 따라오는 결과가 나오면, 단순히 적용 범위를
  바꾸기보다는 두 도시를 구분할 수 있는 고유한 특징을 모델이 학습할 수 있도록
  다르게 접근해야겠다.

## 2 November trackb_base (Track B)
- changed: 없음; `train_b.py`의 기본값 그대로 (ResNet18, 224px, 4 epoch,
  `data/starter/train` 전체). 검사 결과 format and limits: OK (11.17M 파라미터,
  1.81B multiply-adds).
- why: 본격적인 모델 튜닝을 시작하기 전에 Track B 환경이 에러 없이 잘 돌아가는지
  확인하고, 최악의 경우에도 제출할 수 있는 기본 제출물을 만들고 싶었다.
- validation: 0.486 (before: 없음, Track B 첫 실행)
- what it means: <!-- me -->

## 다음에 할 것 (내 계획)

- **no_flip**: 크롭은 starter의 0.35로 되돌리고, 좌우반전(`RandomHorizontalFlip`)만
  없앤 레시피를 학습한다. 이유는 내가 사진에서 본 것 때문이다 — 서울·부산은
  우측통행이고 도쿄·오사카는 좌측통행이며, 한글·중국어 간판의 글자 방향도 고정되어
  있다. 좌우반전은 사진을 거울로 뒤집어서 이 단서를 전부 무효로 만든다.
- wide_crop처럼 한쪽 도시가 오르고 다른 도시가 그만큼 떨어지는 결과는 개선으로
  보지 않는다. 다음부터는 전체 점수 0.015 이상 상승이면서 어느 도시도 크게
  떨어지지 않았을 때만 채택한다.
