<template>
  <!-- 전체 -->
  <div id="writeWrap">
    <!-- 사진 업로드 -->
    <form id="photoUpload" action="" method="">
      <input ref="imageInput" type="file" hidden @change="onChangeImages" />
      <button id="imgUploadButton" type="button" @click="onClickImageUpload">
        자랑할 사진 업로드
      </button>
      <div class="imgCon">
        <img id="imgPreview" v-if="imageUrl" :src="imageUrl" /><img />
      </div>
    </form>

    <!-- 제목과 내용 -->
    <form id="textUpload" action="" method="">
      <input id="title" type="text" placeholder="제목을 입력해주세요" />

      <textarea id="field" placeholder="내용을 입력해주세요"> </textarea>

      <form id="write" action="">
        <button type="submit">
          <img class="writeButton" src="../../assets/images/write.png" alt="" />
        </button>
      </form>
    </form>
  </div>
</template>

<script>
export default {
  name: "write",
  data() {
    return {
      imageUrl: null
    };
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      console.log(e.target.files);
      const file = e.target.files[0];
      this.imageUrl = URL.createObjectURL(file);
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

#writeWrap {
  width: 90%;
  height: 350px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-areas: "photoUpload textUpload";
  margin: 0 auto;
  margin-top: 20px;
  display: grid;
  background-color: rgba(53, 238, 29, 0.055);
  border-radius: 30px;
  padding-top: 2.5rem;
}

input:focus {
  outline: none;
}

textarea:focus {
  outline: none;
}

#photoUpload {
  margin: 0 auto;
  min-width: 20%;
  max-width: 50%;
  min-height: 3rem;
  display: grid;
  grid-area: photoUpload;
  grid-template-rows: repeat(4, 1fr);
  grid-template-areas:
    "imgUploadButton"
    "imgCon"
    "imgCon"
    "imgCon";
}

#imgUploadButton {
  background-color: rgba(210, 241, 31, 0.37);
  height: 1.6rem;
  border-radius: 10px;
  font-family: "Jua", sans-serif;
  display: grid;
  grid-area: imgUploadButton;
}

.imgCon {
  margin-top: -1rem;
  max-width: 10rem;
  display: grid;
  grid-area: imgCon;
  height: 100px;
  float: left;
}

#imgPreview {
  margin: 0 auto;
  margin-left: -2.5rem;
  max-width: 15rem;
  padding-top: -10rem;
}

#textUpload {
  min-width: 50%;
  display: grid;
  grid-area: textUpload;
  padding-left: 2rem;
}

#title {
  display: inline-block;
  background-color: rgba(210, 241, 31, 0.37);
  width: 90%;
  height: 50px;
  border-radius: 13px;
  font-family: "Jua", sans-serif;
}

#field {
  background-color: rgba(210, 241, 31, 0.37);
  width: 90%;
  height: 170px;
  border-radius: 13px;
  margin-top: 10px;
  font-family: "Jua", sans-serif;
}

#write {
  padding-top: 1rem;
  text-align: center;
}

button {
  outline: 0;
}

.writeButton {
  width: 60px;
}

.writeButton:hover {
  animation: writeButton-ani 1s forwards;
  transform: scale(1.2);
}

@keyframes writeButton-ani {
  0% {
    opacity: 0.8;
    transform: scale(0.95);
  }

  50% {
    opacity: 1;
    transform: scale(1.3);
  }

  100% {
    opacity: 1;
    transform: scale(1.1);
  }
}

@media screen and (max-width: 375px) {
  #writeWrap {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr);
    grid-template-areas:
      "photoUpload"
      "textUpload";
  }
}

@media screen and (max-width: 850px) {
  #writeWrap {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 250px);
    grid-template-areas:
      "photoUpload"
      "textUpload";
  }
}

.board__news {
  max-height: 100% !important;
}
</style>
