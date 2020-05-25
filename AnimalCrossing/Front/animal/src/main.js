import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "@fortawesome/fontawesome-free/css/all.css";
<<<<<<< HEAD
import "@fortawesome/fontawesome-free/js/all.js"; 
=======
import "@fortawesome/fontawesome-free/js/all.js";
>>>>>>> 404page

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
