<template>
  <!-- 전체 -->
  <div id="writeWrap">
    <!-- 거래할 아이템 선택 -->
    <div id="tradeUpload" action="" method="">
      <!-- <input type="radio" name="trade" value="buy" id="buy" />
            <label for="buy">삽니다</label>
            <input type="radio" name="trade" value="sell" id="sell" />
            <label for="sell">팝니다</label> -->
      <v-radio-group id="buySell" v-model="trade.sort">
        <v-radio label="삽니다" value="buy"></v-radio>
        <v-radio label="팝니다" value="sell"></v-radio>
      </v-radio-group>

      <!-- 거래할 아이템 종류 -->
      <!-- <v-col id="tradeItem" class="d-flex" cols="12" sm="6">
        <v-select :items="items" label="Solo field" dense solo></v-select>
      </v-col> -->

      <!-- 거래할 아이템(+이미지 미리보기) -->
      <!-- 거래할 아이템 종류로 바꿈 -->
      <v-col id="tradeItem" class="d-flex" cols="12" sm="6">
        <v-select
          v-model="category"
          :items="items"
          label="종류"
          dense
          @click="init"
        ></v-select>
      </v-col>

      <!-- 아이템 검색으로 바꿔야할 부분 -->
      <!-- <v-col id="tradeSearch" class="d-flex" cols="12" sm="6">
        <v-select :items="items" label="아이템" dense></v-select>
      </v-col> -->
      <!--         :filter="customFilter" -->
      <v-autocomplete
        v-if="check"
        v-model="name"
        :items="selectedLists"
        color="white"
        item-text="name"
        label="아이템 검색"
        @click="update"
        loading
      ></v-autocomplete>
    </div>

    <!-- 제목과 내용 -->
    <div id="wantTrade" action="" method="">
      <div id="imgPreview">
        <input ref="imageInput" type="file" hidden @change="onChangeImages" />
        <button
          style="margin-left: 15px;"
          id="imgUploadButton"
          type="button"
          @click="onClickImageUpload"
        >
          거래 사진 업로드
        </button>
        <div class="imgCon">
          <img id="imgPreview" v-if="trade.image" :src="trade.image" /><img />
        </div>
      </div>

      <div class="bell">
        <input
          id="bellInput"
          type="text"
          placeholder="가격 제시"
          v-model="trade.price"
        />
        <img id="bellImg" src="../../assets/images/bell.png" alt="" />
      </div>
      <!-- <label for="bell">벨</label> -->

      <div id="write" action="">
        <button type="submit" v-on:click="tradeSubmit">
          <img class="writeButton" src="../../assets/images/write.png" alt="" />
        </button>
      </div>
    </div>
    <div id="textUpload" action="" method="">
      <input
        id="title"
        type="text"
        placeholder="제목을 입력해주세요"
        v-model="trade.title"
      />
      <textarea
        id="field"
        placeholder="내용을 입력해주세요"
        v-model="trade.content"
      ></textarea>
    </div>
  </div>
</template>

<script>
import * as infoService from "@/api/info.js";
import { tradePost } from "@/api/trade.js";
import * as firebase from "firebase";

export default {
  name: "write",
  data: () => ({
    items: ["이웃", "미술품", "화석", "기타"],
    fossils: [],
    neighbors: [],
    paintings: [],
    selectedLists: [],
    category: "",
    name: "",
    categoryEng: "",
    id: "",
    check: true,
    // post를 보내기 위해서 dict로 묶어서 사용!
    trade: {
      sort: "",
      price: "",
      title: "",
      content: "",
      image: null
    }
  }),
  watch: {
    category: function(newVal, oldVal) {
      if (newVal === "기타") {
        console.log(oldVal);
        this.check = false;
        this.categoryEng = "etc";
      } else {
        this.check = true;
      }
    }
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    async onChangeImages(e) {
      const file = e.target.files[0];
      this.trade.image = URL.createObjectURL(file);
      await firebase
        .storage()
        .ref()
        .child(file.name)
        .put(file)
        .then(response => {
          console.log(response);
        });
      let image = "";
      await firebase
        .storage()
        .ref()
        .child(file.name)
        .getDownloadURL()
        .then(response => {
          console.log(response);
          image = response;
        });
      this.trade.image = image;
    },
    init() {
      this.name = "";
    },

    update() {
      if (this.category === "이웃") {
        this.selectedLists = this.neighbors;
        this.categoryEng = "animal";
      } else if (this.category === "미술품") {
        this.selectedLists = this.paintings;
        this.categoryEng = "painting";
      } else if (this.category === "화석") {
        this.selectedLists = this.fossils;
        this.categoryEng = "fossil";
      } else {
        this.selectedLists = [];
        this.categoryEng = "etc";
      }
    },
    async tradeSubmit() {
      var scope = this;
      const token = this.$store.state.user.token;
      const user = this.$store.state.user;
      let image = "";
      if (this.trade.image === null) {
        image =
          "https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg";
      } else {
        image = this.trade.image;
      }
      let find = "",
        trade = "";
      const trade_info = this.trade;
      if (this.category === "기타") {
        trade = {
          title: trade_info.title,
          content: trade_info.content,
          user_id: user.id,
          username: user.username,
          image: image,
          category: this.categoryEng,
          name: "",
          sort: trade_info.sort,
          price: trade_info.price
        };
      } else {
        find = this.selectedLists.filter(list => list.name === this.name);
        const engname = find[0].engname;
        image = await this.getImgPath(engname);
        trade = {
          title: trade_info.title,
          content: trade_info.content,
          user_id: user.id,
          username: user.username,
          image: image,
          category: this.categoryEng,
          name: find[0].id.toString(),
          sort: trade_info.sort,
          price: trade_info.price
        };
      }
      await tradePost(trade, token, function(response) {
        scope.$router.push(`/trade/tradedetail/${response.data.id}`);
      });
    },
    getImgPath(engname) {
      let image = "";
      if (this.categoryEng === "fossil") {
        image = require(`@/assets/images/fossil.png`);
      } else if (this.categoryEng === "painting") {
        image = require(`@/assets/images/image_${this.categoryEng}/${engname}.jpg`);
      } else if (this.categoryEng === "animal") {
        image = require(`@/assets/images/image_${this.categoryEng}/${engname}.png`);
      }
      return image;
    }
  },
  async mounted() {
    this.fossils = await infoService.getFossils(this.fossils);
    this.neighbors = await infoService.getNeighbors(this.neighbors);
    this.paintings = await infoService.getPaintings(this.paintings);
    this.selectedLists = [];
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

#writeWrap {
  width: 90%;
  height: 350px;
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  grid-template-areas:
    "tradeUpload tradeUpload"
    "wantTrade textUpload"
    "wantTrade textUpload";
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

#tradeUpload {
  margin: 0 auto;
  max-width: 100%;
  display: grid;
  grid-area: tradeUpload;
  grid-template-columns: repeat(3, 1fr);
  grid-template-areas: "buySell tradeItem tradeSearch";
}

/* 여기서부터 communitywrite에서 가져온 부분. */
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
  height: 45px;
  border-radius: 13px;
  font-family: "Jua", sans-serif;
  text-align: center;
}

#field {
  background-color: rgba(210, 241, 31, 0.37);
  width: 90%;
  height: 120px;
  padding-top: 10px;
  border-radius: 13px;
  /* margin-top: 15px; */
  font-family: "Jua", sans-serif;
  text-align: center;
}
/* 는 여기까지 */

/* 이미지 업로드 하는 부분 community write에서 따옴 */
#imgUploadButton {
  background-color: rgba(210, 241, 31, 0.37);
  height: 1.8rem;
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
/* 여기까지 복사해온거 */

#imgPreview {
  margin: 0 auto;
  margin-left: 1rem;
  max-width: 15rem;
  padding-top: -15rem;
}

#buySell {
  margin: 0 auto;
  padding-left: 2rem;
  /* display: grid; */
  grid-area: buySell;
}

#tradeItem {
  margin: 0 auto;
  display: grid;
  grid-area: tradeItem;
}

#tradeSearch {
  margin: 0 auto;
  display: grid;
  grid-area: tradeSearch;
  margin-top: -0.3rem;
}

#wantTrade {
  display: grid;
  grid-area: wantTrade;
  padding-left: 2rem;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-template-areas:
    "imgPreview bell"
    "imgPreview write"
    "imgPreview write";
}

#imgPreview {
  /* display: grid; */
  /* grid-area: imgPreview; */
  width: 200px;
  margin-top: 10px;
  z-index: 1;
}

.bell {
  display: grid;
  grid-area: bell;
  grid-template-columns: repeat(4, 1fr);
  grid-template-areas: "bellInput bellInput bellInput bellImg";
}

#bellInput {
  display: grid;
  grid-area: bellInput;
  background-color: rgba(210, 241, 31, 0.37);
  border-radius: 13px;
  font-family: "Jua", sans-serif;
  margin-top: 4%;
  margin-right: 5%;
  margin-left: 5%;
  height: 40px;
  text-align: center;
}

#bellImg {
  display: grid;
  grid-area: bellImg;
  width: 50%;
}

#write {
  display: grid;
  grid-area: write;
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

@media screen and (max-width: 850px) {
  #writeWrap {
    height: auto;
    display: grid;
    grid-template-rows: repeat(2, 1fr);
    grid-template-areas:
      "tradeUpload"
      "wantTrade";
  }

  #tradeUpload {
    margin-left: 20%;
    display: grid;
    grid-area: tradeUpload;
    grid-template-rows: repeat(3, 1fr);
    grid-template-areas:
      "buySell"
      "tradeItem"
      "tradeSearch";
  }

  #wantTrade {
    margin-left: 22%;
    display: grid;
    grid-area: wantTrade;
    padding-left: 2rem;
    grid-template-rows: repeat(3, 1fr);
    grid-template-areas:
      "imgPreview"
      "bell"
      "write";
  }

  #buySell {
    width: 270px;
  }

  #bell {
    height: 50px;
  }
}

.board__news {
  max-height: 100% !important;
}
</style>
