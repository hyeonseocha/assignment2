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
- 

**A rule I want to try from this**
-

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
