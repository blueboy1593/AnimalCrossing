import Vue from "vue";
import Vuex from "vuex";
import jwtDecode from "jwt-decode";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isSigned: false,
    token: "",
    user: {
      id: 0, // 사용자 아이디 저장
      email: "",
      password: "",
      username: ""
    }
  },
  mutations: {
    saveToken(state, token) {
      state.token = token;
      const decoded_token = jwtDecode(token);
      state.user.id = decoded_token.user_id;
      state.user.username = decoded_token.username;
      state.user.email = decoded_token.email;
      console.log(decoded_token);
    },
    setIsSigned(state, isSigned) {
      state.isSigned = isSigned;
    },
    // setUserId(state, id) {
    //   state.user.id = id;
    // },
    logout(state) {
      state.isSigned = false;
      state.user.id = 0;
      state.user.email = "";
      state.user.username = "";
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      localStorage.removeItem("password");
    }
  },
  actions: {},
  modules: {}
});
