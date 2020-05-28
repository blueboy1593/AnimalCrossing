<template>
  <v-app>
    <v-content>
      <router-view />
      <!-- <div v-if="this.location.pathname == '/'"> -->
        <!-- <Home /> -->
      <!-- </div>> -->
      <!-- <Board /> -->
    </v-content>
  </v-app>
</template>
<script>
// import Board from "./views/Board.vue";
// import Home from './views/Home.vue';

export default {
  name: "App",
  // components: {
  //   Board,
  //   Home
  // }
};
</script>
<style scoped>
/* * {
  background-image: url("../public/img/background.png");
  background-size: cover;
} */
</style>
