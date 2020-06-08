<template>
  <v-container>
    <v-row class="text-center">
      <ul>
        <router-link to="/info/fish">
          <li id="illustratedBook">
            도감
          </li>
        </router-link>
        <router-link to="/moocalculator">
          <li id="calculator">
            무 계산기
          </li>
        </router-link>
        <router-link to="/trade/etc">
          <li id="exchange">
            거래소
          </li>
        </router-link>
        <router-link to="/community/list">
          <li id="board">
            게시판
          </li>
        </router-link>
        <li class="blank"></li>
        <li class="blank"></li>

        <li id="signin" v-if="!$store.state.isSigned">
          <router-link to="/login">
            <div class="signin">
              <img src="../assets/images/dog.png" alt="" />
              로그인
            </div>
          </router-link>
        </li>

        <li id="signin" v-if="$store.state.isSigned">
          <router-link to="/logout">
            <div class="signin">
              <img src="../assets/images/dog.png" alt="" />
              로그아웃
            </div>
          </router-link>
        </li>

        <li id="signup" v-if="!$store.state.isSigned">
          <router-link to="/signup">
            <div class="signup">
              <img src="../assets/images/neogul.png" alt="" />
              회원가입
            </div>
          </router-link>
        </li>

        <li id="signup" v-if="$store.state.isSigned">
          <router-link to="/mypage">
            <div class="signup">
              <img src="../assets/images/neogul.png" alt="" />
              마이페이지
            </div>
          </router-link>
        </li>
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
  list-style-type: none;
  text-align: left;
  white-space: nowrap;
  font-size: 150%;
  line-height: 2.2;
  color: #000000;
  width: 150px;
  text-transform: capitalize;
}
/* 오른쪽 사이드 메뉴 */
li {
  color: black;
  height: 50px;
  transition: all 0.3s ease-out, color 0.2s 0.4s ease-out;
  background: #f3f8f8;
  margin-bottom: 5px;
  border-radius: 13px;
}
li:hover {
  margin-right: -3%;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.815);
}
.blank {
  visibility: hidden;
}
#illustratedBook {
  background: #7a194a;
}
#illustratedBook:hover {
  background: #b13472be;
}
#calculator {
  background: #607a19;
}
#calculator:hover {
  background: #94b33ece;
}
#exchange {
  background: #195e7a;
}
#exchange:hover {
  background: #368eb1c9;
}
#board {
  background: #924460;
}
#board:hover {
  background: #d4648cc9;
}
li:hover > span {
  color: #ffffff;
  transform: rotate(-5deg);
}

#signin {
  background: none;
  color: white;
  text-align: left;
}

.signin {
  color: white;
  text-align: left;
}

#signin img {
  float: left;
  margin-left: 0.4rem;
  width: 35%;
}

#signup {
  /* width: 150px; */
  background: none;
  color: white;
}

.signup {
  color: white;
}

#signup img {
  float: left;
  margin-top: 0.2rem;
  margin-left: 0.4rem;
  width: 35%;
}

#signup:hover {
  color: #86b3eebb;
}
</style>
