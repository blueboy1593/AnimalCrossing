import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isSigned: false,
    user: {
      id: 0, // 사용자 아이디 저장
      // hasWallet: false, // 지갑을 가지고 있는지 여부 조회
      email: "",
      password: ""
    }
  },
  mutations: {
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
      state.user.hasWallet = false;
      localStorage.removeItem("user");
      localStorage.removeItem("password");
    }
  },
  actions: {},
  modules: {}
});
