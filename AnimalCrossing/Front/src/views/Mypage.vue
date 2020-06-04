<template>
  <div class="mypage">
    <div class="profile">
      <img
        src="../assets/images/moopany.png"
        alt="나의 주민"
        class="my_neighbor"
      />
      <button class="change_neighbor btn btn-primary">
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
export default {
  data: function() {
    return {
      username: "",
      email: ""
    };
  },
  changeNeighbor: () => {
    console.log("안해");
  },
  mounted() {
    const user = this.$store.state.user;
    console.log(user);
    this.username = user.username;
    this.email = user.email;
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
  /* height: 100%; */
  text-align: center;
  /* padding-top: 20%; */
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
