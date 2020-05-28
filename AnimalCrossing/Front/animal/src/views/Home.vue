<template>
  <div class="home">
    <router-link to="/info/fish">
    <div class="box box1" style="cursor:pointer">
      <div class="box1Con">
        <img class="box1IconImg" src="../assets/images/logo.png" alt="">
        <div class="box1Text">
          도감
        </div>
      </div>
    </div>
    </router-link>

    <div class="box box2" style="cursor:pointer">무 계산기</div>
    <router-link to="/community">
      <div class="box box3" style="cursor:pointer">거래소</div>
    </router-link>
    <div class="box box4" style="cursor:pointer">게시판</div>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>
<style scoped src="./Home.css" />
