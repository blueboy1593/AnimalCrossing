<template>
  <!-- 전체 -->
  <div id="writeWrap">
    <!-- 거래할 아이템 선택 -->
    <form id="tradeUpload" action="" method="">
      <!-- <input type="radio" name="trade" value="buy" id="buy" />
            <label for="buy">삽니다</label>
            <input type="radio" name="trade" value="sell" id="sell" />
            <label for="sell">팝니다</label> -->
      <v-radio-group id="buySell" v-model="row" row>
        <v-radio label="삽니다" value="radio-1"></v-radio>
        <v-radio label="팝니다" value="radio-2"></v-radio>
      </v-radio-group>

      <!-- 거래할 아이템 종류 -->
      <!-- <v-col id="tradeItem" class="d-flex" cols="12" sm="6">
        <v-select :items="items" label="Solo field" dense solo></v-select>
      </v-col> -->

      <!-- 거래할 아이템(+이미지 미리보기) -->
      <!-- 거래할 아이템 종류로 바꿈 -->
      <v-col id="tradeItem" class="d-flex" cols="12" sm="6">
        <v-select :items="items" label="아이템" dense></v-select>
      </v-col>

      <!-- 아이템 검색으로 바꿔야할 부분 -->
      <!-- <v-col id="tradeSearch" class="d-flex" cols="12" sm="6">
        <v-select :items="items" label="아이템" dense></v-select>
      </v-col> -->
      
      

        <v-autocomplete
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        color="white"
        hide-no-data
        hide-selected
        item-text="Description"
        item-value="API"
        label="거래할 아이템 검색"
        placeholder="Start typing to Search"
        prepend-icon="mdi-database-search"
        return-object
      ></v-autocomplete>
    <v-divider></v-divider>
    <v-expand-transition>
      <v-list v-if="model" class="red lighten-3">
        <v-list-item
          v-for="(field, i) in fields"
          :key="i"
        >
          <v-list-item-content>
            <v-list-item-title v-text="field.value"></v-list-item-title>
            <v-list-item-subtitle v-text="field.key"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-expand-transition>
    </form>

    <!-- 제목과 내용 -->
    <form id="wantTrade" action="" method="">
      <div id="imgPreview">이미지 미리보기</div>

      <input id="bell" type="text" placeholder="가격 제시" />
      <!-- <label for="bell">벨</label> -->

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
  data: () => ({
    items: ["이웃", "미술품", "화석", "기타"]
  }),
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
  grid-template-rows: repeat(3, 1fr);
  grid-template-areas:
    "tradeUpload"
    "wantTrade"
    "wantTrade";
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
  display: grid;
  grid-area: imgPreview;
}

#bell {
  display: grid;
  grid-area: bell;
  background-color: rgba(210, 241, 31, 0.37);
  border-radius: 13px;
  font-family: "Jua", sans-serif;
}

#bell {
  background-color: rgba(210, 241, 31, 0.37);
  border-radius: 13px;
  margin-right: 10%;
  margin-top: 10px;
  font-family: "Jua", sans-serif;
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

@media screen and (max-width: 375px) {
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
