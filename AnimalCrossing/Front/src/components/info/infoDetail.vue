<template>
  <div class="container infoDetail">
    <div class="">
      <span>{{ infoCard.name }}</span>
      <span>
        <v-icon large dark @click="close()">mdi-close-circle-outline</v-icon>
      </span>
    </div>
    <div>
      <img
        :src="getPatingImagPath(infoCard.engname)"
        alt=""
        style="width:100%; height:70%"
      />
    </div>
    <div>
      <span class="detailReal">진품: {{ infoCard.real }}</span> <br />
      <span class="detailMemo">가품: {{ infoCard.memo }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "paintingDetail",
  props: ["infoCard", "routePath"],
  methods: {
    close() {
      this.$emit("close");
    },
    getPatingImagPath(engname) {
      let images = require(`@/assets/images/image_painting/${engname}.jpg`);
      return images;
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.infoDetail {
  background-image: url("../../assets/images/light.png");
}

.paintingDetailCon {
  transform: scale(0.8);
}

.paintingDetail {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(8, 1fr);
  grid-template-areas:
    ". . . . . ."
    ". photo photo photo . ."
    ". photo photo photo . ."
    ". photo photo photo . ."
    ". photo photo photo name name"
    ". photo photo photo real real"
    ". photo photo photo memo memo"
    ". . . . . .";
  height: 100vh;
  border-radius: 15px;

  background-size: cover;

  overflow: hidden;
  font-family: 고딕;
  color: white;
}

.painting {
  display: grid;
  grid-area: photo;
  margin-left: 5%;
  margin-top: 5%;
}

.detailName {
  display: grid;
  grid-area: name;
  text-align: right;
  padding-right: 2rem;
  font-family: 돋움;
  font-weight: bolder;
  font-size: 2.2rem;
}

.textBox {
}

.detailReal {
  display: grid;
  grid-area: real;
  font-size: 1.5rem;
  text-align: right;
  padding-right: 2rem;
  padding-top: 1.5rem;
}

.detailMemo {
  display: grid;
  grid-area: memo;
  font-size: 1.5rem;
  text-align: right;
  padding-right: 2rem;
}

.v-application {
  line-height: 0;
}

#detailImg {
  height: 60vh;
}

.detailPhoto:hover {
  transform: scale(1.2);
  animation: photo 1s forwards;
}

@keyframes photo {
  0% {
    transform: scale(0.95);
  }

  50% {
    transform: scale(1.1);
  }

  100% {
    transform: scale(1.08);
  }
}

.detailPhoto {
  margin-top: 1rem;
  position: absolute;
  box-shadow: 0 10px 20px rgba(146, 193, 219, 0.5);
  overflow: hidden;
  line-height: 0;
}

.detailPhoto:before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  bottom: 2px;
  width: 50%;
  background: rgba(255, 255, 255, 0.05);
}

.detailPhoto span:nth-child(1) {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  /* background: linear-gradient(to right, #0c002b, #1779ff); */
  background: linear-gradient(to right, #002b07, #7fb8a0);
  animation: animate1 2s linear infinite;
}

@keyframes animate1 {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}

.detailPhoto span:nth-child(2) {
  position: absolute;
  top: 0;
  right: 0;
  width: 2px;
  height: 100%;
  /* background: linear-gradient(to bottom, #0c002b, #1779ff); */
  background: linear-gradient(to bottom, #002b04, #7fb8a0);
  animation: animate2 2s linear infinite;
  animation-delay: 1s;
}

@keyframes animate2 {
  0% {
    transform: translateY(-100%);
  }

  100% {
    transform: translateY(100%);
  }
}

.detailPhoto span:nth-child(3) {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  /* background: linear-gradient(to left, #0c002b, #1779ff); */
  background: linear-gradient(to left, #012b00, #7fb8a0);
  animation: animate3 2s linear infinite;
}

@keyframes animate3 {
  0% {
    transform: translateX(100%);
  }

  100% {
    transform: translateX(-100%);
  }
}

.detailPhoto span:nth-child(4) {
  position: absolute;
  top: 0;
  left: 0;
  width: 2px;
  height: 100%;
  /* background: linear-gradient(to top, #0c002b, #1779ff); */
  background: linear-gradient(to top, #042b00, #7fb8a0);
  animation: animate4 2s linear infinite;
  animation-delay: 1s;
}

@keyframes animate4 {
  0% {
    transform: translateY(100%);
  }

  100% {
    transform: translateY(-100%);
  }
}

@media (max-width: 1400px) {
  /* .paintingDetail {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-template-areas:
      ". . . . . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". . . . . ."
      ". name name name name ."
      ". real real real real ."
      ". memo memo memo memo .";
    height: 100vh;
    border-radius: 15px;
  } */

  #detailImg {
    height: 40vh;
  }
}

@media (max-width: 700px) {
  /* .paintingDetail {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(9, 1fr);
    grid-template-areas:
      ". . . . . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". . . . . ."
      ". name name name name name"
      ". real real real real real"
      ". memo memo memo memo memo"
      ". . . . . .";
  } */

  #detailImg {
    height: 35vh;
  }

  .detailName {
    font-size: 2rem;
  }

  .detailReal {
    font-size: 1.5rem;
  }

  .detailMemo {
    font-size: 1.5rem;
  }
}

@media (max-width: 560px) {
  /* .paintingDetail {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-template-areas:
      ". . . . . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". name name name name name"
      ". real real real real real"
      ". memo memo memo memo memo"
      ". . . . . .";
  } */

  #detailImg {
    height: 30vh;
  }

  .detailName {
    font-size: 2rem;
  }

  .detailReal {
    font-size: 1.5rem;
  }

  .detailMemo {
    font-size: 1.5rem;
  }
}

@media (max-width: 460px) {
  /* .paintingDetail {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-template-areas:
      ". . . . . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". name name name name name"
      ". real real real real real"
      ". memo memo memo memo memo"
      ". . . . . .";
  } */

  #detailImg {
    height: 25vh;
  }

  .detailName {
    font-size: 1.5rem;
  }

  .detailReal {
    font-size: 1rem;
  }

  .detailMemo {
    font-size: 1rem;
  }
}

@media (max-width: 375px) {
  /* .paintingDetail {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-template-areas:
      ". . . . . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". photo photo photo . ."
      ". name name name name name"
      ". real real real real real"
      ". memo memo memo memo memo"
      ". . . . . .";
  } */

  #detailImg {
    height: 20vh;
  }

  .detailName {
    font-size: 1.5rem;
  }

  .detailReal {
    font-size: 1rem;
  }

  .detailMemo {
    font-size: 1rem;
  }
}
</style>
