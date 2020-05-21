<template>
  <v-app>
    <RightTab />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>
<script>
import RightTab from "@/components/RightTab.vue";
export default {
  name: "App",
  components: {
    RightTab
  }
};
</script>
