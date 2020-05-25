<template>
  <v-container>
    <v-row class="text-center">
      <ul>
        <router-link to="/">
          <li>
            <span>
              <i class="fa fa-users"></i>
            </span>
            홈
          </li>
        </router-link>
        <router-link to="/info">
          <li>
            <span>
              <i class="fa fa-graduation-cap"></i>
            </span>
            정보
          </li>
        </router-link>
        <router-link to="/community">
          <li>
            <span>
              <i class="fa fa-cogs"></i>
            </span>
            커뮤니티
          </li>
        </router-link>
        <li>
          <span>
            <i class="fa fa-magic"></i>
          </span>
          기타 등등
        </li>
      </ul>
    </v-row>
  </v-container>
</template>

<script></script>

<style scoped>
html,
body {
  font-size: 16px;
  background: #d1d1d1;
  text-align: center;
  font-family: "Cabin", cursive;
  overflow: hidden;
}

ul {
  position: absolute;
  right: -212px;
  padding: 0;
  list-style-type: none;
  text-align: left;
  white-space: nowrap;
  font-size: 200%;
  line-height: 1.9;
  color: #2d2d2d;
  width: 280px;
  text-transform: capitalize;
}
li {
  height: 60px;
  transition: all 0.3s ease-out, color 0.2s 0.4s ease-out;
  background: #0d0d0d;
  margin-bottom: 2px;
  border-left: 4px solid #2d2d2d;
  box-shadow: 1px 1px 2px 2px rgba(0, 0, 0, 0.4);
}
li:hover {
  margin-left: -50%;
  cursor: pointer;
  border-left: 4px solid #f4df48;
  color: #ffffff;
}
li:hover > span {
  color: #ffffff;
  transform: rotate(-5deg);
}
span {
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
}
</style>
