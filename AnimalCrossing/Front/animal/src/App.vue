<template>
  <v-app>
    <v-content>
      <Home />
      <Board />
    </v-content>
  </v-app>
</template>
<script>
// import RightTab from "@/components/RightTab.vue";
import Board from "./views/Board.vue";
import Home from './views/Home.vue';

export default {
  name: "App",
  components: {
    // RightTab,
    Board,
    Home
  }
};
</script>
<style scoped>
* {
  background-image: url("../public/img/background.png");
  background-size: cover;
}
</style>
