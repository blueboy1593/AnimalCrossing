<template>
  <div class="container">
		<div class="row">
			<div id="register-form" class="col-md-6 mx-auto box2">
				<div class="mt-4 box2">
					<div class="form-group">
					<label for="email">email</label>
					<input
						type="text"
						class="form-control"
						id="signup-email"
						v-model="user.email"
						placeholder="이메일"
					/>
					</div>
					<div class="form-group">
					<label for="name">이름</label>
					<input
						type="text"
						class="form-control"
						id="signup-name"
						v-model="user.name"
						placeholder="이름"
					/>
					</div>
					<div class="form-group">
					<label for="password">비밀번호</label>
					<input
						type="password"
						class="form-control"
						id="signup-password"
						v-model="user.password"
						placeholder="비밀번호"
					/>
					</div>
					<div class="form-group">
					<label for="password-confirm">비밀번호 확인</label>
					<input
						type="password"
						class="form-control"
						id="signup-password-confirm"
						v-model="user.passwordConfirm"
						placeholder="비밀번호 확인"
					/>
					</div>
					<button type="submit" class="btn btn-primary" v-on:click="register">
					회원가입
					</button>
				</div>
			</div>
		</div>
  </div>
</template>

<script>
// import { signup } from "../api/user.js";

export default {
  data() {
	return {
	  user: {
		email: "",
		name: "",
		password: "",
		passwordConfirm: ""
	  }
	};
  },
	//   methods: {
	//     register() {
	//       var scope = this;
	//       if (this.user.password === this.user.passwordConfirm) {
	//         signup(
	//           this.user.email,
	//           this.user.name,
	//           this.user.password,
	//           function() {
	//             alert("회원가입이 완료되었습니다.");
	//             scope.$router.push("/");
	//           },
	//           function(error) {
	//             console.error(error);
	//           }
	//         );
	//       } else {
	//         alert("비밀번호가 일치하지 않습니다.");
	//       }
	//     }
	//   }
};
</script>

<style>
#register-form {
  /* margin-left: 40px !important; */
  margin-top: 60px;
}

.box2 {
  /* transform: translate(-50%, -50%); */
  background: orange;
  text-align: center;
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}

#signup-email, #signup-password, #signup-name, #signup-password-confirm {
  border:0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #ee7d6f;
  padding: 14px 10px;
  width: 200px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
}

#signup-email:focus, #signup-password:focus, #signup-name:focus, #signup-password-confirm:focus {
  width: 280px;
  border-color: #d6eb78;
}

.box2 button[type = "submit"]{
  border:0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #d6eb78;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

.box2 button[type = "submit"]:hover{
  background: #d6eb78;
}

</style>
