<template>
  <div id="info">
    <!-- <sequential-entrance fromLeft> -->
    <InfoNav />
    <!-- </sequential-entrance> -->
    <router-view />
  </div>
</template>

<script>
import InfoNav from "../components/info/InfoNav.vue";
export default {
  components: {
    InfoNav
  }
};
</script>

<style scoped>
#info {
  background-color: none;
}
</style>
