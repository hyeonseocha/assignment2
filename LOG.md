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
- what it means: Track B의 기본 점수(0.486)가 Track A 베이스라인(0.497)과 큰 차이가
  나지 않는 점이 좀 신기했다. 조건이 달라져도 모델이 느끼는 한계의 종류는 비슷한
  것 같다 (예를 들면 오사카를 도쿄로 헷갈리는 것). 앞으로 어떤 기법이 진짜 효과가
  있는지 검증할 수 있는 기준이 생긴 것 같았다.

## 2 November no_flip (Track A)
- changed: 크롭은 starter의 0.35로 되돌리고, 좌우반전(`RandomHorizontalFlip`)만
  없앴다. 다른 것은 하나도 그대로.
- why: 간판 글자 방향이나 도로 통행 방향이 국가나 도시를 구분하는 힌트가 될 거라고
  생각했는데, 이미지를 좌우반전하면 그 단서가 헷갈릴 것 같았다.
- validation: 0.493 (before: 0.497 with seed 0, 같은 seed라 바로 비교가 된다)
- what it means: 학습 손실이 더 낮아진 걸 보니 모델이 학습 사진만 더 잘 외우고
  테스트 점수는 안 좋아진 것 같다. 우선 regularization 쪽으로 과적합을 막아보는
  방향을 해볼 생각이 들었다.

## 2 November mixup (Track A)
- changed: `mix`에서 배치 안의 사진 두 장을 섞고(alpha 0.2), 라벨도 섞인 비율만큼
  확률로 바꿨다. 크롭 0.35와 좌우반전 없음은 `no_flip` 그대로.
- why: `no_flip`에서 학습 손실은 낮아지고 검증 점수는 그대로였으니, regularization으로
  과적합을 막아보자는 생각이었다.
- validation: 0.488 (before: 0.493 on no_flip, 같은 조건에서 mixup만 추가)
- what it means: mixup이 학습 손실을 0.96까지 올려서 모델이 데이터를 무작정 외우지
  못하도록 제 역할을 했는데도 검증 점수는 제자리걸음이거나 떨어졌다. 이건 모델
  과적합의 문제라기보다 데이터 자체에 노이즈가 너무 많은 건 아닌지 생각이 든다.
  서울-부산, 도쿄-오사카처럼 육안으로도 구분이 안 가는 애매한 사진이나 잘못된
  라벨링이 성능 향상을 가로막는 진짜 병목일 것 같다.

## 3 November b_mnv3_320 (Track B)
- changed: ResNet18 224px → MobileNetV3-Large 320px. 사진·epoch(4)·학습률·배치
  크기는 `train_b.py` 기본값 그대로. 검사 결과 format and limits: OK
  (4.20M 파라미터, 0.44B multiply-adds; 한도 12M / 2.0B).
- why: 해상도를 키우는 게 좋을 것 같아서. 그러면 비슷한 도시를 좀 더 잘 구분하지
  않을까 싶었다. ResNet18은 224px에서 이미 11.2M 파라미터를 다 써서 더 큰 사진을
  볼 여지가 없었으니, 파라미터를 아끼는 모델로 바꿔서 사진을 크게 보여주는 쪽으로
  갔다.
- validation: 0.539 (before: 0.486 on trackb_base)
- what it means: 다섯 도시가 전부 올랐다(서울 +0.043, 부산 +0.058, 도쿄 +0.075,
  오사카 +0.051, 타이베이 +0.040). 그래도 결과를 보고 든 생각은 여전히 오사카랑
  도쿄를 좀 헷갈리는 것 같아서, 부족한 부분을 보완할 여지가 있다고 생각이 들었다
  (오사카를 도쿄로 837장 틀림). 학습 손실도 1.29 → 0.75로 아직 내려가는 중이라
  epoch를 더 늘리는 쪽에 여지가 남아 있다.

## 3 November the leaderboard, first scores (Track A and B)
- 무엇이 올라갔나: Track A `track-a-1`은 11월 1일 릴리스였는데 보드에 행이 없었다
  (오류 표시도 없이). Track B `track-b-1`은 11월 3일 업데이트에서 채점되어
  **0.392** (서울 0.63, 부산 0.16, 도쿄 0.69, 오사카 0.22, 타이베이 0.27)로 나왔다.
  Track A는 `track-a-2`로 다시 릴리스해서 다음 업데이트에 **0.389**
  (서울 0.60, 부산 0.18, 도쿄 0.73, 오사카 0.24, 타이베이 0.20, 보드가 잰
  validation 0.482)로 들어왔다.
- why: 릴리스가 보드까지 도달하는지, 내 점수가 어디쯤인지 확인하려고.
- what it means: 스타터 레시피보다 점수가 낮다(0.401 → 0.389, 보드 validation도
  0.501 → 0.482). 내 validation 사진에서 0.497 → 0.488로 본 것보다 차이가 커서,
  mixup과 좌우반전 제거는 우연이 아니라 실제로 손해였다고 본다. 도쿄만 0.72 → 0.73
  으로 오르고 오사카·타이베이가 떨어진 것도 같은 방향이다. 그러니 다음에는 recipe를
  스타터로 되돌리고, 바꾸는 것은 사진(selection) 하나로 두고 비교해야겠다.
  또 배운 것: 보드 점수는 내 validation보다 약 0.09 낮게 나온다(0.486 → 0.392).

## 3 November curated (Track A)
- changed: recipe는 스타터 그대로 되돌리고(0.389였던 mixup·좌우반전 없음은 취소),
  바꾸는 것은 사진 하나로 두었다. `curate.py suspects`로 44,248장을 훑어 만든
  20장의 시트를 직접 보고, 도시로 구분이 안 되는 사진 143장을 빼서 44,105장으로
  학습했다(`track_a/dropped.csv`, 뺀 이유도 그 파일에 있다).
- why: mixup 결과를 보고 병목이 데이터 노이즈라고 판단했기 때문에, 모델이 확신했는데
  틀린 사진을 내가 직접 보고 고르는 쪽이 레시피를 더 만지는 것보다 낫다고 봤다.
- validation: 0.5038 (before: 0.4965 on baseline seed 0, 같은 스타터 레시피)
- what it means: 애매한 사진을 솎아낸 큐레이션 방향 자체는 맞았지만(전체 +0.0073,
  서울 0.623 · 부산 0.404 · 오사카 0.369로 셋이 올랐다), 도쿄가 0.647 → 0.588로
  떨어진 걸 보면 도쿄와 오사카 사이에서 한쪽으로 억지로 맞추면 다른 쪽이 틀려버리는
  현상이 아직 남아 있다고 생각했다. 보드에서는 0.395로 스타터 0.401에 0.006 모자랐다.

## 3 November b_mnv3_320_e10 (Track B)
- changed: 같은 MobileNetV3-Large 320px에서 epoch만 4 → 10. 사진·학습률·배치 크기는
  그대로이고, 검사 결과 format and limits: OK (4.20M, 0.44B multiply-adds).
- why: 4 epoch에서 학습 손실이 1.29 → 0.75로 아직 내려가고 있었고, 오사카를 도쿄로
  837장 틀리는 것이 남아 있었다. 모델 구조나 데이터를 바꾸지 않고 학습 횟수만
  늘려도 오를 여지가 있다고 봤다.
- validation: 0.5588 (before: 0.5394 on b_mnv3_320, 같은 조건에서 epoch만 다르다)
- what it means: 모델이 아직 학습을 완전히 끝내지 못했다고 느꼈다. 구조나 데이터를
  바꾸지 않고 epoch만 늘려도 점수가 더 오를 여력이 충분히 남아 있다는 뜻으로 봤다
  (부산 +0.045, 오사카 +0.026, 타이베이 +0.025, 도쿄 +0.011, 서울만 −0.010).
  보드에서 0.439로 스타터 0.403을 넘었다.

## 4 November balanced (Track A)
- changed: 사진은 curated 44,105장 그대로, augmentation도 스타터 그대로 두고
  `sample_weights` 하나만 바꿨다. 사진마다 1/(그 도시 사진 수)를 줘서 다섯 도시가
  똑같이 20%씩 뽑히게 했다(전에는 도쿄 30.2%, 부산 11.7%).
- why: 점수는 다섯 도시 정확도의 평균이라 도시마다 20%씩 똑같이 반영되는데, 사진은
  도쿄 13,310 · 부산 5,174로 기울어져 있었다. 데이터가 많은 도시로 예측이 편향되는
  것을 막고, 가장 취약한 도시들의 학습 비중을 강제로 높여 약점을 보완하려고 했다.
- validation: 0.5032 (before: 0.5038 on curated, 같은 사진·같은 seed 0)
- what it means: 취약 클래스를 살리겠다는 의도는 성공했으나, 본질적으로는 분류
  경계선이 이동해버린 것 같다. 부산 0.404 → 0.437, 오사카 0.369 → 0.446,
  타이베이 0.535 → 0.566으로 셋이 올랐지만 서울 0.623 → 0.538, 도쿄 0.588 → 0.529로
  두 도시가 그만큼 내려 총점은 0.5032로 제자리였다. 다시 말해 도시를 더 잘 구분하게
  된 것이 아니라, 결정 경계가 부산·오사카·타이베이 쪽으로 밀린 것이다.
  보드에는 `track-a-4`(balanced sampling for the weak cities)로 올렸다.

## 4 November batch32 (Track A)
- changed: 도시 균등 샘플링을 취소해 스타터 샘플링으로 되돌리고, `BATCH_SIZE`만
  64 → 32로 바꿨다. 예산은 250,000장 그대로라 네트워크를 통과하는 사진 수는 같고
  (249,984장), step이 3,906 → 7,812로 두 배가 되며 학습 시간은 39.1 → 39.7분으로
  거의 같았다.
- why: 바로 앞 run(balanced)의 학습 손실이 step 390에서 1.428, 마지막에 0.767로 아직
  내려가고 있었으니, 같은 사진으로 업데이트를 두 배 더 하면 더 배우지 않을까 싶었다.
- validation: 0.4945 (before: 0.5038 on curated, 같은 사진·같은 seed 0)
- what it means: 노이즈 심화, 과적합 현상이라고 생각한다. 다섯 도시가 전부 내려
  (서울 −0.016, 부산 −0.012, 도쿄 −0.027, 오사카 +0.016, 타이베이 −0.008) step을
  늘린 것이 어느 도시에도 도움이 되지 않았다. 같은 249,984장을 두 배로 나눠 넣었더니
  학습 손실도 마지막에 0.810으로, 절반의 step으로 끝낸 balanced의 0.767보다 오히려
  높았다. 더 자주 고쳐도 배우는 것이 없었으니 부족한 것은 학습 횟수가 아니었다.
  그래서 배치 크기는 64로 되돌렸다.

## 4 November the leaderboard, three seeds (Track A)
- 무엇을 알았나: 보드의 validation 점수는 seed 0·1·2의 **평균**이었고, 내 로컬 기록은
  전부 seed 0 하나였다. 그래서 curated의 보드 validation 0.494는 seed 1·2가 약
  0.489였다는 뜻이고, 같은 사진으로 세 번 재면 스타터 0.501 vs curated 0.494라
  curated는 사실상 손해였다(내 seed 0의 +0.0073은 seed 운이었다).
- why: 릴리스는 한 번에 하나씩이고 보드는 3-seed로 재므로, 내 seed 0 점수로는
  개선인지 아닌지를 판단할 수 없다는 것을 확인하려고.
- what it means: 보드의 같은 행에 있는 도시별 점수를 봐야 한다. 스타터
  0.60/0.19/0.72/0.27/0.22와 curated 0.62/0.19/0.68/0.26/0.22를 비교하면 부산·타이베이는
  두 릴리스 모두 찍기 수준이고, 0.006 차이는 대부분 도쿄였다. 앞으로도 1 November에
  정한 기준 그대로, 보드 총점이 0.015 이상 오르거나 약한 도시가 0.03 이상 안정적으로
  오르지 않으면 개선이라고 말하지 않는다.

## 다음에 할 것 (내 계획)

- **srcbal (도시도, 사진 출처도 균등)**: balanced로 취약 도시가 올랐지만 총점이
  그대로였던 이유는 경계선이 이동했기 때문이고, 1 November에 적어 둔 대로 "도시는
  찍은 카메라로도 구분된다"는 문제가 남아 있다. 도쿄에는 osv5m이 1,916장, 부산에는
  0장이고, 서울은 youtube가 37%인데 타이베이는 14%다. 그래서 도시는 20%씩 똑같이
  뽑되, 도시 안에서는 사진 종류(commons/youtube/osv5m)를 √ 비율로 고르게 잡아,
  사진 수가 적은 종류를 더 자주 뽑고 많은 종류는 덜 뽑게 했다(서울 osv5m 320장이
  commons보다 4.6배 자주 나오고, 21배씩 반복하지는 않는다). 이렇게 하면 카메라나
  출처를 단서로 쓰는 지름길이 줄어들 것으로 본다.
- **큐레이션 2차**: srcbal 모델의 `suspects` 시트를 보고, 여전히 도시 구분이 안 되는
  사진을 이번에도 내가 직접 골라 뺀다.
- wide_crop처럼 한쪽 도시가 오르고 다른 도시가 그만큼 떨어지는 결과는 개선으로 보지
  않는다. 다음부터는 전체 점수 0.015 이상 상승이면서 어느 도시도 크게 떨어지지
  않았을 때만 채택한다. (curated는 +0.0073이라 이 기준에 못 미쳤고, 3-seed로 재면
  스타터보다 낮았지만, 보드에서 0.389 → 0.395로 올라 실패한 릴리스보다는 나았으므로
  올려 두었다. balanced는 기준에 정확히 걸린다: 부산·오사카·타이베이는 크게 올랐지만
  서울·도쿄가 그만큼 내려 총점이 제자리였다.)
- 순서: 11/5 아침에 보드에서 `track-a-4`의 3-seed 점수와 도시별 점수를 확인 →
  부산·타이베이가 올랐으면 srcbal을 `track-a-5`로 릴리스 → 결과를 보고 큐레이션 2차.
  최종 릴리스는 11/8 밤, 마감은 11/10.
