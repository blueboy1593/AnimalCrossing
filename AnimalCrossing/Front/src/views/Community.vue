<template>
  <div class="community">
    <!-- <v-btn>글쓰기</v-btn> -->
    <!-- <CommunityPost /> -->
    <!-- <input type="file" @change="onFileChange" /> -->
    <router-view />
  </div>
</template>

<script>
// import CommunityPost from "../components/community/CommunityPost.vue";
// import * as firebase from "firebase";

export default {
  // components: {
  //   CommunityPost
  // },
  // data() {
  //   return {
  //     imageUrl: null
  //   };
  // }
  // methods: {
  //   async onFileChange(e) {
  //     console.log("1번. async 드디어 알겠네.");
  //     console.log(e.target.files);
  //     const file = e.target.files[0];
  //     console.log(file);
  //     this.imageUrl = URL.createObjectURL(file);
  //     console.log(this.imageUrl);
  //     await firebase
  //       .storage()
  //       .ref()
  //       .child(file.name)
  //       .put(file)
  //       .then(response => {
  //         console.log(response);
  //         console.log("2번");
  //       });
  //     await firebase
  //       .storage()
  //       .ref()
  //       .child(file.name)
  //       .getDownloadURL()
  //       .then(response => {
  //         console.log(response);
  //         console.log("3번");
  //       });
  //     console.log("4번");
  //   }
  // }
};
</script>

<style></style>
