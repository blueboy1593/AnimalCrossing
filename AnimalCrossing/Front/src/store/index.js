import Vue from "vue";
import Vuex from "vuex";
import jwtDecode from "jwt-decode";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isSigned: false,
    user: {
      id: 0, // 사용자 아이디 저장
      email: "",
      password: "",
      username: ""
    }
  },
  mutations: {
    setUserName(state, username) {
      state.user.username = username;
    },
    saveToken(state, token) {
      const decoded_token = jwtDecode(token);
      state.user.id = decoded_token.user_id;
      state.user.email = decoded_token.email;
      state.user.token = token;
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
    }
  },
  actions: {},
  modules: {}
});
