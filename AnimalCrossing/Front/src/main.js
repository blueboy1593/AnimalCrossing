import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "@fortawesome/fontawesome-free/css/all.css";
import "@fortawesome/fontawesome-free/js/all.js";
import SequentialEntrance from "vue-sequential-entrance";
import "vue-sequential-entrance/vue-sequential-entrance.css";
Vue.use(SequentialEntrance);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

// firebase 사용
import * as firebase from "firebase";

var firebaseConfig = {
  apiKey: "AIzaSyDJ_cU7yM-78IESIAIj7Pj4d8iHkFqJxp4",
  authDomain: "modong-158aa.firebaseapp.com",
  databaseURL: "https://modong-158aa.firebaseio.com",
  projectId: "modong-158aa",
  storageBucket: "modong-158aa.appspot.com",
  messagingSenderId: "753568862888",
  appId: "1:753568862888:web:488d24c4bd8d67aa73a89d",
  measurementId: "G-3PWVWWLPVJ"
};

firebase.initializeApp(firebaseConfig);
firebase.analytics();
