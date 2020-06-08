<template>
  <div class="back">
    <div class="top_container">
      <div class="graph_box">
        <!-- <MooGraph :moo_graph_info="moo_graph_info" /> -->
        <MooGraphMin :moo_graph_info="graph_min" class="moo" />
        <MooGraphMax :moo_graph_info="graph_max" class="moo" />
      </div>
      <div class="moopany_box">
        <button
          type="submit"
          id="moocal_btn"
          class="btn btn-primary"
          v-on:click="moocalcul"
        >
          다시 입력하기
        </button>
        <img
          src="../assets/images/moopany.png"
          alt="무파니 사진"
          id="moopany"
        />
      </div>
    </div>
    <div class="weekly_price_box">
      <div class="weekly_price" style="text-align:center">
        <h4>요일</h4>
        <div class="weekly_price_time">
          오전
          <img src="../assets/images/bells.svg" class="weekly_bell" />
        </div>
        <div class="weekly_price_time">
          오후
          <img src="../assets/images/bells.svg" class="weekly_bell" />
        </div>
      </div>
      <div class="weekly_price">
        <h4>월요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[0] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[1] }}
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>화요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[2] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[3] }}
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>수요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[4] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[5] }}
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>목요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[6] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[7] }}
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>금요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[8] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[9] }}
          </div>
        </div>
      </div>
      <div class="weekly_price">
        <h4>토요일</h4>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[10] }}
          </div>
        </div>
        <div class="weekly_price_time">
          <div>
            {{ this.moo[11] }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MooGraphMin from "../components/MooGraphMin.vue";
import MooGraphMax from "../components/MooGraphMax.vue";

export default {
  data() {
    return {
      moo: [],
      graph_max: [],
      graph_min: []
    };
  },
  components: {
    MooGraphMin,
    MooGraphMax
  },
  methods: {
    moocalcul: function() {
      alert("다시 무값 입력하구리!");
      this.$router.push("/moocalculator");
    }
  },
  mounted: function() {
    const moo_info = this.$route.params.price_calculated;
    const moo_price = new Array();
    const moo_graph_max = new Array();
    const moo_graph_min = new Array();
    moo_info.forEach(element => {
      if (element[0] === element[1]) {
        moo_price.push(element[0]);
      } else {
        moo_price.push(`${element[0]} ~ ${element[1]}`);
      }
    });
    moo_info.forEach(element => {
      moo_graph_max.push(element[1]);
      moo_graph_min.push(element[0]);
    });
    moo_graph_max.push(600);
    moo_graph_min.push(600);
    moo_graph_max.unshift(0);
    moo_graph_min.unshift(0);
    // moo_graph_max.unshift(600);
    // moo_graph_min.unshift(600);
    // console.log(moo_graph_max);
    // console.log(moo_graph_min);
    moo_price.shift();
    this.moo = moo_price;
    this.graph_max = moo_graph_max;
    this.graph_min = moo_graph_min;
    // console.log(this.moo);
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

/* 그래프와 헤더, 그리고 무파니까지 */
.moo {
  /* display: flex; */
  position: absolute;
  width: 55%;
}

.top_container {
  height: 60%;
  margin-bottom: 30px;
}

.graph_box {
  width: 70%;
  height: 50%;
  margin: 1rem;
  display: inline-block;
  margin-bottom: 40px;
}

#moo_chart {
  width: 100%;
}

.moopany_box {
  /* display: inline-block; */
  display: inline-block;
  width: 20%;
  text-align: center;
  margin-left: 30px;
}

#moopany {
  width: 75%;
  /* margin-bottom: 20px; */
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
  padding: 10px;
  border-radius: 16px;
}

.weekly_price_time {
  padding: 4px;
  color: #6e661b;
  font-size: 1.1rem;
  font-weight: 400;
  line-height: 1.1876em;
  text-align: center;
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
  margin: 10px auto 10px;
  text-align: center;
  border: 2px solid #7273e0;
  padding: 0px 30px;
  height: 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

#moocal_btn[type="submit"]:hover {
  background: #7273e0;
}
</style>
