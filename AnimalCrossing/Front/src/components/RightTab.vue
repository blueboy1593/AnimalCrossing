<template>
  <v-container>
    <v-row class="text-center">
      <ul>
        <router-link to="/info">
          <li id="illustratedBook">
            도감
          </li>
        </router-link>
        <router-link to="/moocalculator">
          <li id="calculator">
            무 계산기
          </li>
        </router-link>
        <router-link to="/community">
          <li id="exchange">
            거래소
          </li>
        </router-link>
        <router-link to="/community">
          <li id="board">
            게시판
          </li>
        </router-link>
        <li class="blank"></li>
        <li class="blank"></li>
        <router-link to="/community">
          <li id="signin">
            로그인
          </li>
        </router-link>
        <router-link to="/community">
          <li id="signup">
            회원가입
          </li>
        </router-link>
      </ul>
    </v-row>
  </v-container>
</template>

<script></script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

html,
body {
  font-size: 16px;
  background: #d1d1d1;
  text-align: center;
  /* font-family: "Cabin", cursive; */
  /* font-family: 'Jua', sans-serif; */
  overflow: hidden;
}

/* 밑줄 제거, 폰트 */
.v-application a {
  color: rgba(255, 255, 255, 0);
  font-family: "Jua", sans-serif;
  text-align: center;
}

ul {
  position: absolute;
  /* right: -212px; */
  /* padding: 0; */
  list-style-type: none;
  text-align: left;
  white-space: nowrap;
  font-size: 150%;
  line-height: 2.2;
  /* color: #2d2d2d; */
  color: #000000;
  width: 150px;
  text-transform: capitalize;
}
/* 오른쪽 사이드 메뉴 */
li {
  /* padding-left: 5%; */
  color: black;
  height: 50px;
  transition: all 0.3s ease-out, color 0.2s 0.4s ease-out;
  background: #f3f8f8;
  margin-bottom: 5px;
  /* border-left: 4px solid #2d2d2d; */
  /* box-shadow: 1px 1px 2px 2px rgba(0, 0, 0, 0.4); */
  border-radius: 13px;
}
li:hover {
  margin-right: -3%;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.815);

  /* border-left: 4px solid #f4df48; */
  /* color: #ffffff; */
}
.blank {
  visibility: hidden;
}
#illustratedBook {
  background: #7a194a;
  /* background: #f0c2d9dc; */
}
#illustratedBook:hover {
  background: #b13472be;
  /* background: #7a194a; */
}
#calculator {
  background: #607a19;
  /* background: #e2f0c2dc; */
}
#calculator:hover {
  background: #94b33ece;
  /* background: #607a19; */
}
#exchange {
  background: #195e7a;
  /* background: #c2dff0dc; */
}
#exchange:hover {
  background: #368eb1c9;
  /* background: #195e7a; */
}
#board {
  background: #807e14;
  /* background: #c2dff0dc; */
}
#board:hover {
  background: #b1af3b;
  /* background: #195e7a; */
}
li:hover > span {
  color: #ffffff;
  transform: rotate(-5deg);
}
/* span {
  position: relative;
  display: block;
  width: 60px;
  height: 60px;
  text-align: center;
  float: left;
  line-height: 2.1;
  transition: all 0.2s 0.4s ease-out;
  font-size: 120%;
  margin: 0 3px;
  font-size: 95%;
} */
</style>
