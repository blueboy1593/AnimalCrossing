<template>
  <div class="container" id="back">
    <div class="row">
      <div id="login-form" class="col-md-6 mx-auto box">
        <div class="mt-4 box">
          <div class="form-group">
            <label for="email">email</label>
            <input
              type="text"
              class="form-control"
              id="login-email"
              v-model="user.email"
              placeholder="이메일"
            />
          </div>
          <div class="form-group">
            <label for="password">비밀번호</label>
            <input
              type="password"
              class="form-control "
              id="login-password"
              v-model="user.password"
              placeholder="비밀번호"
            />
          </div>
          <button type="submit" class="btn btn-primary" v-on:click="login">
            로그인
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { login } from "../api/user.js";

export default {
  data() {
    return {
      user: {
        email: "",
        password: ""
      }
    };
  }
};
</script>

<style>
.box {
  /* transform: translate(-50%, -50%); */
  background: #e9a1df;
  text-align: center;
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}

#login-email,
#login-password {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #df49cb;
  padding: 14px 10px;
  width: 200px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
}

#login-email:focus,
#login-password:focus {
  width: 280px;
  border-color: #d15977;
}

.box button[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #d15977;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

.box button[type="submit"]:hover {
  background: #d15977;
}
</style>
