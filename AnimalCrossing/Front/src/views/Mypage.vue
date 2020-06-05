<template>
  <div class="mypage">
    <div class="profile">
      <img :src="neighbor_url" alt="나의 주민" class="my_neighbor" />
      <button
        class="change_neighbor btn btn-primary"
        v-on:click="changeNeighbor"
      >
        내 주민 바꾸기
      </button>
      <hr />
      <br />
      이메일: {{ this.email }}<br />
      이름: {{ this.username }}
    </div>
    <div class="mydata">
      <div class="mypost">
        내가 쓴 글
      </div>
      <div class="mytrade">
        내 거래내역
      </div>
    </div>
  </div>
</template>

<script>
import { getNeighbors } from "@/api/info.js";

export default {
  data: function() {
    return {
      username: "",
      email: "",
      neighbor_url: "",
      infoCards: []
    };
  },
  async mounted() {
    // 여기는 유저 정보를 스토어에서 받아서 저장하는 코드
    const user = this.$store.state.user;
    this.username = user.username;
    this.email = user.email;

    // 로컬 스토리지에 오늘의 주민 정보가 있을 때.
    if (localStorage.getItem("myneighbor_time")) {
      const myneighbor_url = localStorage.getItem("myneighbor_url");
      this.neighbor_url = myneighbor_url;
    } else {
      const infoCards = await getNeighbors(infoCards);
      const random_info =
        infoCards[Math.floor(Math.random() * infoCards.length)];
      const neighbor_url = await this.getAnimalImgPath(random_info.engname);
      this.neighbor_url = neighbor_url;

      // 오늘의 첫 시간 저장.
      const now_time = new Date().toLocaleDateString();
      localStorage.setItem("myneighbor_time", now_time);
      localStorage.setItem("myneighbor_url", neighbor_url);
    }
  },
  methods: {
    getAnimalImgPath(engname) {
      let images = require(`@/assets/images/image_animal/${engname}.png`);
      console.log(images);
      return images;
    },
    changeNeighbor: async function() {
      // 현재 시간 잡아내는 코드
      const now_time = new Date().toLocaleDateString();
      if (now_time === localStorage.getItem("myneighbor_time")) {
        alert("주민 변경은 하루에 한번만 된다구리!");
      } else {
        const infoCards = await getNeighbors(infoCards);
        const random_info =
          infoCards[Math.floor(Math.random() * infoCards.length)];
        const neighbor_url = await this.getAnimalImgPath(random_info.engname);
        this.neighbor_url = neighbor_url;

        localStorage.setItem("myneighbor_time", now_time);
        localStorage.setItem("myneighbor_url", neighbor_url);
        alert("주민 변경에 성공했다구리!");
      }
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
}

.mypage {
  display: flex;
  height: 100%;
}

.profile {
  display: inline-block;
  width: 40%;
  text-align: center;
  font-size: 18px;
}

.my_neighbor {
  display: block;
  margin: 10px auto;
  height: 50%;
}

/* 주민바꾸기 버튼 */
.change_neighbor {
  background: none;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #d15959;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: black;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
  font-family: "Gamja Flower";
}

.change_neighbor:hover {
  background: #d15977;
  color: rgb(243, 227, 227);
}

.mydata {
  display: inline-block;
  width: 60%;
  font-size: 20px;
  text-align: center;
}

.mypost {
  height: 50%;
  border: 2px solid lavender;
  border-radius: 24px;
}

.mytrade {
  height: 50%;
  border: 2px solid lavender;
  border-radius: 24px;
}
</style>
