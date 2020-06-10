## :mag_right: 3-1. 요구사항 정의 (Table)

| Req ID |              요구사항 명              | 설명                                                         |
| :----: | :-----------------------------------: | :----------------------------------------------------------- |
| Req 1  |            유저 관리:man:             | - 관리자: 서비스를 관리한다.<br />- 방문자: 고유 ip를 통해 랜덤 닉네임을 부여 받는다. |
|        |             방문자 서비스             | (커뮤니티: 고유 ip로 닉네임 형성 해야 함)<br />- 거래<br />- 자랑<br />- 친구 찾기<br />- 기타<br /><br />(정보)<br />- 물고기<br />- 곤충<br />- 화석<br />- 미술품<br />- 꽃 |
|        |                유저 DB                | 유지 관리에 필요한 최소 정보는 필수로 포함<br />- 방문자 ip (CharField) (자동입력, 랜덤 닉네임 형성에 사용)<br />- 비밀번호 (CharField) <br />- 악성유저 여부 (IntField) |
| Req 2  |           물고기 조회:fish:           | 크롤링을 통해 가져온 물고기 정보를 보기 편한 UI로 디자인     |
|        |           곤충 조회:beetle:           | 크롤링을 통해 가져온 곤충 정보를 보기 편한 UI로 디자인       |
|        |               물고기 DB               | 물고기 데이터베이스 테이블 만들기<br /><br />- 물고기 이름 (CharField)<br />- 포획 가능 달 (IntField)<br />- 포획 가능 시간대 (CharField)<br />- 포획 장소 (CharField)<br />- 포획 난이도 (IntField) |
|        |                곤충 DB                | 곤충 데이터베이스 테이블 만들기<br /><br />- 곤충 이름 (CharField)<br />- 포획 가능 달 (CharField) <br />- 포획 가능 시간 대 (CharField) |
| Req 3  |            그림 조회:art:             | - 미술관을 구성할 수 있는 특정 그림 수집 방법 소개<br />- 진품/가품 구분 기준 제공 |
|        |                그림 DB                | 그림 데이터베이스 테이블 만들기<br /><br />- 그림 제목 (CharField)<br />- 진품 그림 설명 (TextField)<br />- 가품 그림 설명 (TextField)<br />- 구분 방법 (TextField) |
| Req 4  |        꽃 교배:cherry_blossom:        | 가져온 꽃 정보를 기반으로 보기 편한 UI로 제공<br /><br />- 교배 방법<br />- 교배 시 나오는 꽃의 종류<br />- 특정 꽃을 얻는 방법<br />- 시뮬레이션 기능: 시간이 남으면 도전해볼 것 |
|        |                 꽃 DB                 | 꽃 데이터베이스 테이블 만들기<br /><br />- 꽃 이름 (CharField)<br />- 꽃 그림 (CharField)<br />- 꽃 종류 (CharField)<br />- 꽃 색깔 (CharField or IntField)<br />- 꽃 세대 (CharField, 교배 여부) |
| Req 5  | 커뮤니티<br />거래:currency_exchange: | 회원을 위한 동물의숲 커뮤니티 (1)<br />회원은 거래 커뮤니티에서 본인이 원하는 재화를 얻기 위해 다른 유저와 소통한다. |
|        |               주요 기능               | - 글 작성<br />- 댓글 작성<br />- 좋아요 기능 **없음**<br />- 판매자와 수요자 간 1:1 통신 채널 구현 (채팅)<br />- 글 작성자를 누르면 서로 채팅 가능하게 |
| Req 6  |       커뮤니티​<br />​자랑:mega:        | 회원을 위한 동물의 숲 커뮤니티 (2)<br />내 섬의 컨텐츠를 단순히 자랑만 할 수 있는 게시판 |
|        |               주요 기능               | - 글 작성<br />- 댓글 작성 가능<br />- 좋아요 기능 **있음**<br />- 게임 내 컨텐츠 캡처 이미지 업로드 기능 구현 필수 (Firebase)<br />- *(필요시 네이버 텍스트 에디터 오픈소스 사용해서 구현)* |
| Req 7  |           커뮤니티:couple:            | 회원을 위한 동물의 숲 커뮤니티 (3)<br />같은 지역 기반 동물의 숲 유저 찾기<br />게임친구 :arrow_right: 동네친구 (동네친구 찾기 '위피' 어플에서 착안) |
|        |               주요 기능               | - 구글 지도 API 사용<br />- 같은 지역 기반 동물의 숲 유저 찾기<br />- 다른 지역 기반 동물의 숲 유저 찾기 |
| Req 8  |              커뮤니티 DB              | ** **CRUD 기능 제공** **<br /><br />- 게시글 카테고리 (IntField): 거래, 자랑, 친구<br />- 게시글 제목 (CharField)<br />- 게시글 내용 (TextField)<br />- 작성자 (CharField): 고유 ip로 형성된 랜덤 닉네임<br />- 이미지 (CharField): Firebase 이미지 URL<br />- 비밀번호 (​CharField): 게시글 작성 시마다 입력<br />- 작성 시간 (DateTimeField, auto_now_add=True)<br />- 수정 시간 (DateTimeField, auto_add=True)<br />- 댓글 (CharField)<br />- 게시글 좋아요 기능 (ManyToManyField) |
| Req 9  |       서비스 UX/UI 커스터마이징       | - Web: 동물의 숲 컨셉 + 싸이월드 감성<br />- Mobile: 프로그레시브웹앱(PWA) |



## 3-2. 요구사항 정의 (ERD, Architecture)

- ERD

  ![](README_image/ERD.PNG)

- Architecture

  ![](README_image/Project Architecture.PNG)