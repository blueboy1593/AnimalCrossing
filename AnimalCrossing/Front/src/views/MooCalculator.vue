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
            placeholder="bell을 입력하세요"
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
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>화요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>수요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>목요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>금요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>토요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>일요일</h4>
        <div class="weekly_price_time">
          오전
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
        <div class="weekly_price_time">
          오후
          <div>
            <img src="../assets/images/bells.svg" class="weekly_bell" />
            <input type="text" class="weekly_price_input" placeholder="벨" />
          </div>
        </div>
      </div>
    </div>
    <button
      type="submit"
      id="moocal_btn"
      class="btn btn-primary"
      v-on:click="moocalcul"
    >
      무트코인 예측하기
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    moocalcul: function() {
      alert("계산코드는 쪼금 있다가..");
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
  font-size: 22px;
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

#moocal_btn[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto 10px;
  text-align: center;
  border: 2px solid #84e9b6;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

#moocal_btn[type="submit"]:hover {
  /* background: #96e985; */
  background: #84e9b6;
}
</style>
