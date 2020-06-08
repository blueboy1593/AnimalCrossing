<template>
  <v-app>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>
<script>
import { findById } from "@/api/user.js";
import jwtDecode from "jwt-decode";
export default {
  name: "App",
  methods: {
    async reloadSetting() {
      const scope = this;
      const token = localStorage.getItem("token");
      if (!token) return;
      const decodedToken = jwtDecode(token);
      scope.$store.commit("setIsSigned", true);
      scope.$store.commit("saveToken", token);
      const userId = decodedToken.user_id;
      await findById(userId, function(response) {
        scope.$store.commit("setUserName", response.data.username);
      });
    }
  },
  mounted() {
    // 로컬스토리지에 저장된 유저정보가 있으면 store의 isSigned true로 유지.
    this.reloadSetting();
  }
};
</script>
