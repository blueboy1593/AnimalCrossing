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
        <h4>나의 자랑 글</h4>
        <section class="board__news">
          <div>
            <MypageCardC
              v-for="MypageCard in CommunityCards"
              :key="MypageCard.id"
              :MypageCard="MypageCard"
              class="card_one"
            />
          </div>
        </section>
      </div>
      <div class="mytrade">
        <h4>나의 거래글</h4>
        <section class="board__news">
          <div>
            <MypageCardT
              v-for="MypageCard in TradeCards"
              :key="MypageCard.id"
              :MypageCard="MypageCard"
              class="card_one"
            />
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import { getNeighbors } from "@/api/info.js";
import { getShows } from "@/api/show.js";
import { getTrades } from "@/api/trade.js";
import MypageCardC from "../components/mypage/MypageCardC.vue";
import MypageCardT from "../components/mypage/MypageCardT.vue";

export default {
  components: {
    MypageCardC,
    MypageCardT
  },
  data: function() {
    return {
      username: "",
      email: "",
      neighbor_url: "",
      myid: 0,
      infoCards: [],
      CommunityCards: [],
      TradeCards: []
    };
  },
  async mounted() {
    // 여기는 유저 정보를 스토어에서 받아서 저장하는 코드
    const user = this.$store.state.user;
    this.username = user.username;
    this.email = user.email;
    this.myid = user.id;

    // 나의 자랑글, 거래글 불러와서 필터 사용할것!
    const CommunityCards = await getShows(this.CommunityCards);
    // console.log(CommunityCards);
    this.CommunityCards = CommunityCards.filter(
      element => element.user_id === this.myid
    );

    const TradeCards = await getTrades(this.TradeCards);
    // console.log(TradeCards);
    this.TradeCards = TradeCards.filter(
      element => element.user_id === this.myid
    );

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

.card_one {
  display: inline-block;
  width: 50%;
  height: auto;
  max-height: 165px;
  padding: 10px 0px;
}

/* board_new -  */
/* for the section describing the news items, display the items in a single column layout */
.board__news {
  display: flex;
  /* margin: 1rem 0 2rem; */
  flex-direction: column;
  width: 100%;
  justify-self: center;
  /* dictate a maximum height to allow for vertical scroll */
  /* max-height: 500px; */
  height: 80%;
  overflow-y: auto;
}

/* minor style changes for the scrollbar */
.board__news::-webkit-scrollbar {
  width: 0.25rem;
}

.board__news::-webkit-scrollbar-track {
  box-shadow: inset 0 0 6px hsla(200, 100%, 5%, 0.3);
}

.board__news::-webkit-scrollbar-thumb {
  background: hsl(200, 100%, 10%);
  border-radius: 5px;
}
</style>
