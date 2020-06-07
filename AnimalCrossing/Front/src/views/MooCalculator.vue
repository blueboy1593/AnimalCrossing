<template>
  <div class="back">
    <div class="cal_head">
      <h1>동물의숲 무계산기</h1>
    </div>
    <div class="buy_price">
      <div class="buy_price_form">
        무파니 구매 가격
        <div>
          <img
            src="../assets/images/bells.svg"
            alt="Bag of bells"
            class="bell"
          />
          <input
            type="text"
            class="buy_price_input"
            placeholder="구입가"
            v-model="moo[0]"
          />벨
        </div>
      </div>
    </div>
    <div class="weekly_price_box">
      <div class="weekly_price">
        <h4>월요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              placeholder="벨"
              v-model="moo[1]"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              placeholder="벨"
              v-model="moo[2]"
            />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>화요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[3]"
              placeholder="벨"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[4]"
              placeholder="벨"
            />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>수요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[5]"
              placeholder="벨"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[6]"
              placeholder="벨"
            />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>목요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[7]"
              placeholder="벨"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[8]"
              placeholder="벨"
            />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>금요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[9]"
              placeholder="벨"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[10]"
              placeholder="벨"
            />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>토요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[11]"
              placeholder="벨"
            />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input
              type="text"
              class="weekly_price_input"
              v-model="moo[12]"
              placeholder="벨"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="button_box">
      <button
        type="submit"
        id="moocal_btn_initialize"
        class="moocal_btn btn btn-primary"
        v-on:click="initialize"
      >
        입력값 초기화
      </button>
      <button
        type="submit"
        id="moocal_btn_predict"
        class="moocal_btn btn btn-primary"
        v-on:click="moocalcul"
      >
        무트코인 예측하기
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      moo: [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    };
  },
  methods: {
    moocalcul: async function() {
      const scope = this;
      const moo_info = scope.moo;
      localStorage.setItem("moo_info", JSON.stringify(moo_info));
      let percentage = 40;
      // 2차원 배열 만들기.
      let price_input = this.moo.map(x => {
        return parseInt(x);
      });
      let price_calculated = new Array();
      price_calculated.push([price_input[0], price_input[0]]);
      for (let i = 1; i < 13; i++) {
        if (price_input[i] === 0) {
          const pre_input = price_calculated[i - 1];
          const min_input = Math.round(
            (pre_input[0] * (100 - percentage)) / 100
          );
          const max_input = Math.round(
            (pre_input[1] * (100 + percentage)) / 100
          );
          percentage = percentage * (2 / 3);
          price_calculated.push([min_input, Math.min(600, max_input)]);
        } else {
          price_calculated.push([price_input[i], price_input[i]]);
        }
      }
      alert("무값 계산중 계산중");
      scope.$router.push({
        name: "MooCalculated",
        params: { price_calculated }
      });
    },
    initialize: function() {
      localStorage.removeItem("moo_info");
      this.moo = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      alert("무 입력값이 초기화 되었습니다.");
    }
  },
  mounted: function() {
    if (localStorage.getItem("moo_info")) {
      this.moo = JSON.parse(localStorage.getItem("moo_info"));
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
}

.cal_head {
  font-size: 20px;
  text-align: center;
  margin-top: 15px;
}

/* 벨 사진 사이즈 조정 */
.bell {
  width: 30px;
  margin-right: 15px;
}

.weekly_bell {
  width: 20px;
  margin-right: 5px;
}

/* 초기 무파니 구매 가격 */
.buy_price {
  display: flex;
  background-color: rgb(248, 248, 240);
  margin: 16px 16px;
  padding: 16px;
  border-radius: 16px;
  font-size: 20px;
  text-align: center;
  justify-content: center;
}

.buy_price_input {
  color: #6e661b;
  cursor: text;
  display: inline-flex;
  position: relative;
  font-size: 20px;
  box-sizing: border-box;
  align-items: center;
  font-weight: 400;
  line-height: 1.1876em;
  text-align: center;
}

/* 중간 몸통 부분 */
.weekly_price_box {
  display: flex;
  flex-wrap: wrap;
  /* align-items: stretch; */
  justify-content: space-between;
  margin: 16px 16px;
}

h4 {
  text-align: center;
  margin-bottom: 8px;
}

.weekly_price {
  width: 13%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: rgb(248, 248, 240);
  padding: 16px;
  border-radius: 16px;
}

.weekly_price_input {
  color: #6e661b;
  cursor: text;
  display: inline-flex;
  position: absolute;
  font-size: 15px;
  align-items: center;
  font-weight: 400;
  line-height: 1.1876em;
  box-sizing: inherit;
  width: 5%;

  transition: border-bottom-color 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-bottom: 1px solid rgba(0, 0, 0, 0.42);
  text-align: center;
}

/* 버튼 관리 파트 */
.button_box {
  display: flex;
  justify-content: space-between;
}

/* 버튼 공통!!! */
.moocal_btn {
  border: 0;
  background: none;
  display: inline-block;
  margin: 10px auto 0px;
  text-align: center;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: black;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

#moocal_btn_initialize {
  border: 2px solid #e9a87d;
}

#moocal_btn_initialize:hover {
  background: #e9a87d;
}

#moocal_btn_predict {
  border: 2px solid #84e9b6;
}

#moocal_btn_predict:hover {
  /* background: #96e985; */
  background: #84e9b6;
}
</style>
