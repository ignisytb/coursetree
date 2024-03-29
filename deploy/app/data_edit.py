import numpy as np

data = """BS102	[1학년] 공학수학 I (3)	3	2	2	0	0	0	0	0	0	0	0	F	F	F
BS101	[1학년] 다변수 미적분학 (3) [가을]	3	2	1	0	0	0	0	0	0	0	0	F	F	F
BS103	[1학년] 일반물리 I (3) [봄]	3	2	0	0	0	0	0	0	0	0	0	F	F	F
BS118	[1학년] 일반화학 I (3) [봄]	3	2	0	0	0	0	0	0	0	0	0	F	F	F
BS113	[1학년] 일반화학실험 I (1) [가을]	1	2	1	0	0	0	0	0	0	0	0	F	F	F
BS115	[1학년] 일반생물학 실험 (1)	1	2	2	0	0	0	0	0	0	0	0	F	F	F
BE101	[1학년] 프로그래밍 (3) [가을]	3	2	1	0	0	0	0	0	0	0	0	F	F	F
BE202	[2학년] 데이터사이언스기초 (3) [봄]	3	2	0	0	0	0	0	0	0	0	0	F	F	F
BE201	[2학년] 인공지능기초 (3) [가을]	3	2	1	0	0	0	0	0	0	0	0	F	F	F
HSS201	인문1 (3)	3	4	2	0	0	0	0	0	0	0	0	F	F	F
HSS202	인문2 (3)	3	4	2	0	0	0	0	0	0	0	0	F	F	F
HSS203	인문3 (3)	3	4	2	0	0	0	0	0	0	0	0	F	F	F
HSS204	인문4 (3)	3	4	2	0	0	0	0	0	0	0	0	F	F	F
GC101	[1학년] Academic English: Speaking and Correspondence (2) [봄]	2	4	0	0	0	0	0	0	0	0	0	F	F	F
GC102	[1학년] Academic English: Research and Writing (2) [가을]	2	4	1	0	0	0	0	0	0	0	0	F	F	F
BS203	[2학년] 선형대수학 (3)	3	M	2	2	0	0	2	0	2	3	0	F	F	F
BS201	[2학년] 공학수학 II (3)	3	M	2	1	0	0	1	0	1	0	0	F	F	F
BS202	[2학년] 확률과 통계 및 실습 (3)	3	M	2	1	0	0	0	0	2	2	0	F	F	F
BS104	[1학년] 일반물리실험 I (1) [봄]	1	P	0	0	0	0	0	0	0	0	0	F	F	F
BS106	[1학년] 일반물리실험 II (1) [가을]	1	P	1	0	0	0	0	0	0	0	0	F	F	F
BS105	[1학년] 일반물리 II  (3) [가을]	3	S	1	3	0	0	1	0	3	0	1	F	F	F
BS119	[1학년] 일반화학 II (3) [가을]	3	S	1	0	3	0	0	3	0	0	3	F	F	F
BS116	[1학년] 일반생물학 I (3) [봄]	3	3	0	0	0	3	0	0	0	0	0	F	F	F
BS117	[1학년] 일반생물학 II (3) [가을]	3	S	1	0	0	3	0	0	0	0	0	F	F	F
BS114	[1학년] 생명과학개론 (3)	3	3	2	3	3	0	3	3	3	3	3	F	F	F
BE205	[2학년] 회로이론과 계측법(이론) (2) [봄]	2	E	0	2	0	0	1	0	3	0	0	F	F	F
BE206	[2학년] 회로이론과 계측법(실습) (1) [봄]	1	E	0	2	0	0	1	0	3	0	0	F	F	F
BE203	[2학년] 창의기계설계 (3) [봄]	3	E	0	0	0	0	3	0	0	0	0	F	F	F
BE204	[2학년] 화학공학개론 (3) [가을]	3	E	1	0	1	0	0	1	0	0	3	F	F	F
HSS109	[1학년] 쓰기·읽기·말하기 (3)	3	H	2	0	0	0	0	0	0	0	0	F	F	F
HSS301	[3학년] Scientific Writing (3)	3	H	2	0	0	0	0	0	0	0	0	F	F	F
PHY202a	[2학년] [물] 해석역학 (2021년도) (3) [봄]	3	0	0	3	0	0	0	0	0	0	0	T	T	T
PHY202	[2학년] [물] 해석역학 I (3) [봄]	3	0	0	3	0	0	0	0	0	0	0	T	T	T
PHY204	[2학년] [물] 해석역학 II (3) [가을]	3	0	1	4	0	0	0	0	0	0	0	T	T	T
PHY203	[2학년] [물] 전기역학 (3) [가을]	3	0	1	3	0	0	0	0	0	0	0	T	T	T
PHY307	[3학년] [물] 열 및 통계 물리 (3) [가을]	3	0	1	4	0	0	0	0	0	0	0	T	T	T
PHY302	[3학년] [물] 현대물리 실험 (2) [봄]	2	0	0	4	0	0	0	0	0	0	0	T	F	T
PHY304	[3학년] [물] 양자역학 I (3) [봄]	3	0	0	3	0	0	0	0	0	0	0	T	T	T
PHY306	[3학년] [물] 수리물리 (3) [봄]	3	0	0	2	0	0	0	0	0	0	0	T	F	T
PHY303	[3학년] [물] 고체물리 I (3) [가을]	3	0	1	2	0	0	0	0	0	0	0	T	T	T
PHY305	[3학년] [물] 양자역학 II (3) [가을]	3	0	1	2	0	0	0	0	0	0	0	T	T	T
PHY301	[3학년] [물] 응용물리실험 (2) [가을]	2	0	1	4	0	0	0	0	0	0	0	T	T	T
PHY403	[4학년] [물] 고체물리 II (3) [봄]	3	0	0	2	0	0	0	0	0	0	0	T	T	T
PHY401	[4학년] [물] 현대광학 (3) [봄]	3	0	0	2	0	0	0	0	0	0	0	T	T	T
PHY402	[4학년] [물] 응용물리특론 (3) [가을]	3	0	1	2	0	0	0	0	0	0	0	T	T	T
PHY404	[4학년] [물] 반도체 소자 물리학 (3) [가을]	3	0	1	2	0	0	0	0	0	0	0	T	T	T
CHEM206	[2학년] [화] 일반화학실험 II (1) [봄]	1	0	0	0	4	0	0	0	0	0	0	T	F	T
CHEM205	[2학년] [화] 유기화학 I (3) [봄]	3	0	0	0	3	0	0	2	0	0	4	T	T	T
CHEM201	[2학년] [화] 분석화학 (3) [봄]	3	0	0	0	3	0	0	2	0	0	2	T	T	T
CHEM202	[2학년] [화] 무기화학 I (3) [가을]	3	0	1	0	3	0	0	2	0	0	4	T	T	T
CHEM203	[2학년] [화] 물리화학 I (3) [가을]	3	0	1	0	3	0	0	2	0	0	2	T	T	T
CHEM204	[2학년] [화] 유기화학 II (3) [가을]	3	0	1	0	3	0	0	0	0	0	2	T	T	T
CHEM305	[3학년] [화] 물리화학 II (3) [봄]	3	0	0	0	3	0	0	0	0	0	2	T	T	T
CHEM306	[3학년] [화] 무기화학 II (3) [봄]	3	0	0	0	4	0	0	0	0	0	2	T	T	T
CHEM301	[3학년] [화] 심화화학실험 I (2) [봄]	2	0	0	0	4	0	0	0	0	0	0	T	F	T
CHEM302	[3학년] [화] 심화화학실험 II (2) [가을]	2	0	1	0	4	0	0	0	0	0	0	T	F	T
CHEM303	[3학년] [화] 유기화학 III (3) [가을]	3	0	1	0	2	0	0	0	0	0	2	T	T	T
CHEM304	[3학년] [화] 물리화학 III (3) [가을]	3	0	1	0	2	0	0	0	0	0	2	T	T	T
CHEM401	[4학년] [화] 전기화학 (3) [가을]	3	0	1	0	2	0	0	0	0	0	2	T	T	T
CHEM402	[4학년] [화] 고체화학 I (3) [가을]	3	0	1	0	2	0	0	0	0	0	0	T	F	T
LS204	[2학년] [생] 세포생물학 (3) [봄]	3	0	0	0	0	3	0	0	0	0	0	T	F	T
LS203	[2학년] [생] 세포생물학 실험 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS202	[2학년] [생] 유전학 (3) [가을]	3	0	1	0	0	3	0	0	0	0	0	T	F	T
LS205	[2학년] [생] 유전학 실험 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS308	[3학년] [생] 생화학 I (3) [봄]	3	0	0	0	0	3	0	0	0	0	0	T	F	T
LS304	[3학년] [생] 생명체의 다양성과 유기적 관계 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS305	[3학년] [생] 신경과학 I (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS301	[3학년] [생] 생명과학특강 I (짝수년도) (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS302	[3학년] [생] 생명과학특강 II (홀수년도) (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS301	[3학년] [생] 생명과학특강 I (홀수년도) (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS302	[3학년] [생] 생명과학특강 II (짝수년도) (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS307	[3학년] [생] 분자생물학 (3) [가을]	3	0	1	0	0	3	0	0	0	0	0	T	F	T
LS309	[3학년] [생] 생화학 II (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS303	[3학년] [생] 정량 생물과학 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS310	[3학년] [생] 해부생리학 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS306	[3학년] [생] 신경과학 II (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS403	[4학년] [생] 발생 및 발달생물학 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS402	[4학년] [생] 융합생명과학 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	F	T
LS406	[4학년] [생] 의생명공학 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	T	T
LS405	[4학년] [생] 생물정보학 (3) [봄]	3	0	0	0	0	2	0	0	0	0	0	T	T	T
LS401	[4학년] [생] 면역학 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS407	[4학년] [생] 동물생리학 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS408	[4학년] [생] 일주기 생체리듬 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
LS409	[4학년] [생] 식물 생명과학 (3) [가을]	3	0	1	0	0	2	0	0	0	0	0	T	F	T
MECH201	[2학년] [기] 고체역학 (3) [봄]	3	0	0	0	0	0	3	0	0	0	0	F	T	T
MECH202	[2학년] [기] 유체역학 (3) [가을]	3	0	1	0	0	0	3	0	0	0	2	F	T	T
MECH203	[2학년] [기] 동역학 (3) [가을]	3	0	1	0	0	0	3	0	0	0	0	F	T	T
MECH305	[3학년] [기] 기계열역학 (3) [봄]	3	0	0	0	0	0	3	0	0	0	0	F	T	T
MECH309	[3학년] [기] 자동제어시스템 (3) [봄]	3	0	0	0	0	0	3	0	2	0	0	F	T	T
MECH301	[3학년] [기] 인간과 공학 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH306	[3학년] [기] 진동공학 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH307	[3학년] [기] 인공지능개론 (3) [가을]	3	0	1	0	0	0	3	0	0	0	0	F	T	T
MECH302	[3학년] [기] 의공학개론 (3) [가을]	3	0	1	0	0	0	2	0	2	0	0	F	T	T
MECH304	[3학년] [기] 시스템의 통합적 모델링 (3) [가을]	3	0	1	0	0	0	2	0	2	0	0	F	T	T
MECH303	[3학년] [기] 기구학 (3) [가을]	3	0	1	0	0	0	2	0	0	0	0	F	T	T
MECH403	[4학년] [기] 메카트로닉스 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH405	[4학년] [기] 열전달 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH401	[4학년] [기] 로봇동역학 및 제어 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH402	[4학년] [기] 마이크로/나노공학 (3) [봄]	3	0	0	0	0	0	2	0	0	0	0	F	T	T
MECH40X	[4학년] [기] 기계재료학 (3) [가을]	3	0	1	0	0	0	2	0	0	0	0	T	T	T
MECH404	[4학년] [기] 공학적설계 (3) [가을]	3	0	1	0	0	0	2	0	0	0	0	F	T	T
MSE305	[3학년] [재] 재료공학개론 I (3) [봄]	3	0	0	0	2	0	0	3	0	0	0	T	T	T
MSE302a	[3학년] [재] 재료열역학개론 (2021년도) (3) [봄]	3	0	0	2	0	0	0	3	0	0	0	T	T	T
MSE304	[3학년] [재] 재료공학실험 (3) [봄]	3	0	0	0	0	0	0	3	0	0	0	F	T	T
MSE302	[3학년] [재] 재료열역학개론 (3) [가을]	3	0	1	2	0	0	0	3	0	0	0	T	T	T
MSE306	[3학년] [재] 재료공학개론 II (3) [가을]	3	0	1	0	0	0	0	3	0	0	0	T	T	T
MSE303	[3학년] [재] 나노재료학 (3) [가을]	3	0	1	0	0	0	0	3	0	0	2	T	T	T
MSE404a	[4학년] [재] 결정학 및 회절 (2021년도) (3) [봄]	3	0	0	2	2	0	0	3	0	0	0	F	T	T
MSE402	[4학년] [재] 재료상변태 (3) [봄]	3	0	0	2	0	0	0	3	0	0	0	T	T	T
MSE405	[4학년] [재] 전자물성학 (3) [봄]	3	0	0	0	0	0	0	2	0	0	0	F	T	T
MSE406	[4학년] [재] 박막재료공학 (3) [봄]	3	0	0	0	0	0	0	2	0	0	0	T	T	T
MSE404	[4학년] [재] 결정학 및 회절 (3) [가을]	3	0	1	2	2	0	0	3	0	0	0	F	T	T
MSE403	[4학년] [재] 전자재료학 (3) [가을]	3	0	1	0	0	0	0	2	0	0	0	F	T	T
EE201	[2학년] [전] 디지털 논리회로 (3) [가을]	3	0	1	0	0	0	0	0	2	3	0	F	T	T
EE301	[3학년] [전] 신호 및 시스템 (3) [봄]	3	0	0	0	0	0	0	0	3	0	0	F	T	T
EE304	[3학년] [전] 반도체물성개론 (3) [봄]	3	0	0	0	0	0	0	0	3	0	0	F	T	T
EE303	[3학년] [전] 전자회로 이론 (3) [봄]	3	0	0	0	0	0	0	0	3	0	0	F	T	T
EE302	[3학년] [전] 전자소자개론 (3) [가을]	3	0	1	0	0	0	0	0	3	0	0	F	T	T
EE305	[3학년] [전] 통신의기초 (3) [가을]	3	0	1	0	0	0	0	0	2	0	0	F	T	T
EE403	[4학년] [전] 디지털통신 (3) [봄]	3	0	0	0	0	0	0	0	2	0	0	F	T	T
EE406	[4학년] [전] 지능형제어시스템 (3) [봄]	3	0	0	0	0	0	0	0	2	0	0	F	T	T
EE404	[4학년] [전] 반도체공정개론 (3) [봄]	3	0	0	0	0	0	0	0	2	0	0	F	T	T
EE401	[4학년] [전] 디지털 신호처리 (3) [봄]	3	0	0	0	0	0	0	0	2	2	0	F	T	T
EE405	[4학년] [전] 반도체공정실습 (3) [가을]	3	0	1	0	0	0	0	0	2	0	0	F	T	T
EE402	[4학년] [전] 디지털 영상처리 (3) [가을]	3	0	1	0	0	0	0	0	2	2	0	T	T	T
CSE203	[2학년] [컴] 자료구조 (3) [봄]	3	0	0	0	0	0	0	0	2	3	0	T	T	T
CSE202	[2학년] [컴] 이산수학 (3) [가을]	3	0	1	0	0	0	0	0	2	3	0	T	T	T
CSE201	[2학년] [컴] 객체지향 프로그래밍 (3) [가을]	3	0	1	0	0	0	0	0	2	3	0	T	T	T
CSE305	[3학년] [컴] 컴퓨터구조 (3) [봄]	3	0	0	0	0	0	0	0	2	3	0	F	T	T
CSE306	[3학년] [컴] 시스템 프로그래밍 (3) [봄]	3	0	0	0	0	0	0	0	0	3	0	F	T	T
CSE302	[3학년] [컴] 기계학습개론 (3) [봄]	3	0	0	0	0	0	0	0	0	2	0	T	T	T
CSE301	[3학년] [컴] 컴퓨터 알고리즘 (3) [가을]	3	0	1	0	0	0	0	0	0	3	0	T	T	T
CSE304	[3학년] [컴] 운영체제 (3) [가을]	3	0	1	0	0	0	0	0	2	3	0	F	T	T
CSE303	[3학년] [컴] 딥러닝개론 (3) [가을]	3	0	1	0	0	0	0	0	2	2	0	F	T	T
CSE402	[4학년] [컴] 강화학습 (3) [봄]	3	0	0	0	0	0	0	0	2	2	0	T	T	T
CSE404	[4학년] [컴] 컴퓨터 비전 개론 (3) [봄]	3	0	0	0	0	0	0	0	0	2	0	F	T	T
CSE401	[4학년] [컴] 데이터베이스개론 (3) [가을]	3	0	1	0	0	0	0	0	0	2	0	F	T	T
CSE403	[4학년] [컴] 컴퓨터 네트워크 (3) [가을]	3	0	1	0	0	0	0	0	2	2	0	T	T	T
CE201	[2학년] [화공] 화학공학기초실험 (2) [가을]	2	0	1	0	0	0	0	0	0	0	2	F	T	T
CE303	[3학년] [화공] 화학공학열역학 (3) [봄]	3	0	0	0	0	0	0	0	0	0	3	F	T	T
CE302a	[3학년] [화공] 이동현상개론 (2021년도) (3) [봄]	3	0	0	0	0	0	0	0	0	0	3	F	T	T
CE302	[3학년] [화공] 이동현상개론 (3) [가을]	3	0	1	0	0	0	0	0	0	0	3	F	T	T
CE301	[3학년] [화공] 반응공학 (3) [가을]	3	0	1	0	0	0	0	0	0	0	3	F	T	T
CE401	[4학년] [화공] 고분자개론 (3) [봄]	3	0	0	0	2	0	0	0	0	0	2	T	T	T
CE402	[4학년] [화공] 화학 제품 및 공정설계 (3) [봄]	3	0	0	0	0	0	0	0	0	0	2	F	T	T
TP101	[1학년] 디자인사고 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP306	[3학년] 산업과 법 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP305	[3학년] 게임이론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP307	[3학년] UX디자인 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP301	[3학년] 커뮤니케이션과 현대사회 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP311	[3학년] 감성공학과 디자인 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP201	[2학년] 디자인 기획과 전략 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP405	[4학년] 단분자 생물물리학 개론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP308	[3학년] 생명에 대한 융합적 이해 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP30a	[3학년] 학부생을 위한 해석학 개론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP30b	[3학년] 현대대수학 개론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP30c	[3학년] 기하학 개론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
TP404	[4학년] 양자 컴퓨팅 개론 (3)	3	1	2	0	0	0	0	0	0	0	0	F	F	T
ENT301	[3학년] 기업가 정신과 사회적 책임 (3)	3	5	2	0	0	0	0	0	0	0	0	F	F	T
ENT302	[3학년] 경영학원론 (3)	3	5	2	0	0	0	0	0	0	0	0	F	F	T
ENT303	[3학년] 하이테크 마케팅 (3)	3	5	2	0	0	0	0	0	0	0	0	F	F	T
RP301	[3학년] UGRP I (3) [봄]	3	2	0	0	0	0	0	0	0	0	0	F	F	T
RP302	[3학년] UGRP II (3) [가을]	3	2	1	0	0	0	0	0	0	0	0	F	F	T
RP201	[2학년] URP (2) [가을]	2	3	1	0	0	0	0	0	0	0	0	F	F	T
RP407	[4학년] URP (2) [봄]	2	3	0	0	0	0	0	0	0	0	0	F	F	T
INTERN1	인턴	1	4	2	0	0	0	0	0	0	0	0	F	F	T
INTERN2	인턴	1	4	2	0	0	0	0	0	0	0	0	F	F	T"""

res = []
datas = data.split("\n")
for i in datas:
    res.append(i.split("\t"))

res = np.array(res)
for i in res:
    print(i[1]+" | "+i[5])