<template>
  <div class="paintingDetailCon">
    <div class="paintingDetail">
      <div class="painting">
        <div class="detailPhoto">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <img
            id="detailImg"
            src="../../assets/images/nav_painting.png"
            alt=""
          />
        </div>
      </div>

      <div class="detailName">
        <div class="textBox">
          모성이 느껴지는 조각
        </div>
      </div>
      <div class="detailReal">
        작자 미상카피톨리나 늑대상
      </div>
      <div class="detailMemo">
        늑대가 혀를 내밀고 있음
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "paintingDetail"
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.paintingDetailCon {
  transform: scale(0.8);
}

.paintingDetail {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(8, 1fr);
  grid-template-areas:
    ". photo photo photo . ."
    ". photo photo photo . ."
    ". photo photo photo . ."
    ". photo photo photo . ."
    ". photo photo photo name name"
    ". photo photo photo name name"
    ". . real real real ."
    ". . memo memo memo .";
  height: 100vh;
  border-radius: 15px;
  background-color: #2f3652ec;
  overflow: hidden;
  font-family: "Jua", sans-serif;
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
}

.textBox {
  font-family: 궁서;
  font-size: 2rem;
  padding-top: 1.7rem;
  margin: 0 auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  border-radius: 5px;
  color: rgba(255, 255, 255, 0.877);
}

.detailReal {
  display: grid;
  grid-area: real;
  font-size: 2rem;
}

.detailMemo {
  display: grid;
  grid-area: memo;
  font-size: 2rem;
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
  background: linear-gradient(to right, #0c002b, #1779ff);
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
  background: linear-gradient(to bottom, #0c002b, #1779ff);
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
  background: linear-gradient(to left, #0c002b, #1779ff);
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
  background: linear-gradient(to top, #0c002b, #1779ff);
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
</style>
