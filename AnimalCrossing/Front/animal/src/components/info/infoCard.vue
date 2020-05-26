<template>
  <div class=infoCard> 
    <div class="photo">
        <img src="../../assets/images/fish.png" height="100%" class="photoImg" alt="">
    </div>
    <div class="infoName">
        이름
    </div>
    <div class="infoDetail">
        정보
    </div>
  </div>
</template>

<script>
export default {
    name: "infoCard",
};
</script>

<style>
    .infoCard {
        width: 120px;
        height: 150px;
        border-radius: 15px;
        background-color: #c1d2e1;
        overflow: hidden;
    }

    .photo {
        width: 120px;
        height: 100px;
        border-radius: 15px;
        background-color: #aac8e4;
        text-align: center;
    }

    .photoImg {
        /* display: block; */
        margin: 0 auto;
    }

    .infoName {
        text-align: center;
        font-weight: bolder;
        font-size: 1.1rem;
    }

    .infoDetail {
        text-align: center;
        font-weight: 100;
    }
</style>