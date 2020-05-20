<template>
  <div class="404page">
    <NotFound />
  </div>
</template>

<script>
// @ is an alias to /src
import NotFound from "@/components/NotFound.vue";

export default {
  name: "NotFound",
  components: {
    NotFound
  }
};
</script>
