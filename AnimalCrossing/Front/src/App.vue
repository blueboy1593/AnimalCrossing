<template>
  <v-app>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>
<script>
import { login } from "@/api/user.js";
export default {
  name: "App",
  methods: {
    reloadSetting() {
      const scope = this;
      if (localStorage.getItem("user")) {
        login(
          (scope.$store.state.user.email = localStorage.getItem("user")),
          (scope.$store.state.user.password = localStorage.getItem("password")),
          function(response) {
            scope.$store.commit("setIsSigned", true);
            // scope.$store.commit("setUserId", response.data.id);
            scope.$store.commit("saveToken", response.data.token);
            // scope.$router.push("/");
          },
          function(error) {
            alert("유저 이메일 혹은 비밀번호가 일치하지 않습니다.");
            console.error(error);
          }
        );
      }
    }
  },
  mounted() {
    // 로컬스토리지에 저장된 유저정보가 있으면 store의 isSigned true로 유지.
    // const scope = this;
    this.reloadSetting();
  }
};
</script>
