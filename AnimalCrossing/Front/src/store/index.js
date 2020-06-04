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
      password: ""
    }
  },
  mutations: {
    saveToken(state, token) {
      state.token = token;
      const decoded_token = jwtDecode(token);
      state.user.id = decoded_token.user_id;
      console.log(state.user.id);
    },
    setIsSigned(state, isSigned) {
      state.isSigned = isSigned;
    },
    setUserId(state, id) {
      state.user.id = id;
    },
    // setUserHasWallet(state, hasWallet) {
    //   state.user.hasWallet = hasWallet;
    // },
    logout(state) {
      state.isSigned = false;
      state.user.id = 0;
      localStorage.removeItem("user");
      localStorage.removeItem("password");
      localStorage.removeItem("token");
    }
  },
  actions: {},
  modules: {}
});
