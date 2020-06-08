<template>
  <div class="container">
    <div class="face-wrap">
      <div class="ear ear--left"></div>
      <div class="ear ear--right"></div>
      <div class="face">
        <div class="eyes">
          <div class="eye eye--left"></div>
          <div class="eye eye--right"></div>
          <div class="eyes-btm"></div>
        </div>
        <div class="nose"></div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
}

body {
  box-sizing: border-box;
}

$blue: #4349a1;
$brown: #d68438;
$darkBrown: #4c2a20;
$darkPink: #bb4d4c;
$lightBrown: #b6662b;
$mediumBrown: #7e442c;
$pink: #df686a;

.container {
  background: url("https://preview.redd.it/nfil94odgxe41.png?width=960&crop=smart&auto=webp&s=250a84bd12b8565ba3262c9b99e4b8ddc9b999b0");
  height: 100vh;
  overflow: hidden;
  position: relative;
  width: 100vw;
}

.face-wrap {
  border-radius: 45%;
  left: 50%;
  height: 20rem;
  position: absolute;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  width: 20rem;
}

.face {
  background-color: $brown;
  border-radius: 48%;
  bottom: 3.5rem;
  left: 50%;
  position: absolute;
  transform: translateX(-50%);
  height: 10.5rem;
  width: 14rem;
}

.nose {
  background-color: $darkBrown;
  border-radius: 50%;
  bottom: 2.5rem;
  box-shadow: 0 0.25rem 0 0.25rem $mediumBrown, 0 0.5rem 0 0.5rem $lightBrown;
  height: 2rem;
  left: 50%;
  position: absolute;
  transform: translateX(-50%);
  width: 2.5rem;
  z-index: 3;

  &:before {
    border-left: 1rem solid transparent;
    border-right: 1rem solid transparent;
    border-bottom: 0.5rem solid $darkBrown;
    content: "";
    height: 0;
    left: 0.25rem;
    position: absolute;
    top: -0.15rem;
    width: 0;
  }
}

.eyes {
  background-color: $darkBrown;
  border-radius: 50% 50% 1rem 1rem;
  height: 4.95rem;
  left: 2rem;
  position: absolute;
  top: 0.8rem;
  width: 10rem;
  z-index: 2;

  &:before {
    background-color: $darkBrown;
    border-radius: 50% 1rem 50% 50%;
    bottom: -2.2rem;
    content: "";
    height: 7rem;
    position: absolute;
    left: -0.725rem;
    width: 4rem;
    transform: rotate(32deg);
  }
  &:after {
    background-color: $darkBrown;
    border-radius: 50% 50% 50% 50%;
    bottom: -2.2rem;
    content: "";
    height: 7rem;
    position: absolute;
    right: -0.725rem;
    width: 4rem;
    transform: rotate(-32deg);
  }

  .eyes-btm {
    background-color: $brown;
    border-radius: 50%;
    bottom: -1.9rem;
    height: 2.8rem;
    left: 50%;
    position: absolute;
    transform: translateX(-50%);
    width: 4.7rem;
    z-index: 3;
  }
}

.eye {
  background-color: #fff;
  border-radius: 45%;
  height: 3.5rem;
  overflow: hidden;
  position: absolute;
  top: 2rem;
  width: 2.5rem;
  will-change: transform;
  z-index: 5;

  &:before {
    background-color: $blue;
    border-radius: 45%;
    content: "";
    height: 1.75rem;
    left: 50%;
    position: absolute;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
    width: 1.25rem;
  }

  &:after {
    background-color: $brown;
    content: "";
    height: 5rem;
    position: absolute;
    top: 0;
    width: 4rem;
  }
}

.eye--left {
  left: 0;

  &:after {
    // animation: dozeLeft 1.5s linear infinite alternate;
    left: -1.75rem;
    transform: translateY(-3.5rem) rotate(-35deg);
  }
}

.eye--right {
  right: 0;

  &:after {
    // animation: dozeRight 1.5s linear infinite alternate;
    right: -1.75rem;
    transform: translateY(-3.5rem) rotate(35deg);
  }
}

.ear {
  background-color: $brown;
  content: "";
  height: 3.25rem;
  overflow: hidden;
  position: absolute;
  top: 4.75rem;
  width: 2.5rem;
  z-index: 4;

  &:after {
    background-color: $pink;
    content: "";
    height: 2rem;
    overflow: hidden;
    position: absolute;
    width: 1.5rem;
  }
}

.ear--left {
  background: linear-gradient(
    90deg,
    $darkBrown 0%,
    $darkBrown 40%,
    $brown 40%,
    $brown 100%
  );
  border-radius: 50% 0 0 50%;
  left: 4.25rem;
  transform: rotate(65deg);

  &:after {
    border-radius: 50% 0 0 50%;
    box-shadow: inset 0.2rem 0 0 $darkPink;
    left: 0.35rem;
    top: 0.6rem;
  }
}

.ear--right {
  background: linear-gradient(
    270deg,
    $darkBrown 0%,
    $darkBrown 40%,
    $brown 40%,
    $brown 100%
  );
  border-radius: 0 50% 50% 0;
  right: 4.25rem;
  transform: rotate(-65deg);

  &:after {
    border-radius: 0 50% 50% 0;
    box-shadow: inset -0.2rem 0 0 $darkPink;
    right: 0.35rem;
    bottom: 0.6rem;
  }
}

//keyframes

@keyframes dozeLeft {
  0% {
    transform: translateY(-3.5rem) rotate(-35deg);
  }
  50%,
  60% {
    transform: translateY(-3rem) rotate(-35deg);
  }
  55% {
    transform: translateY(-2rem) rotate(-35deg);
  }
  70% {
    transform: translateY(-1.75rem) rotate(-35deg);
  }
}

@keyframes dozeRight {
  0% {
    transform: translateY(-3.5rem) rotate(35deg);
  }
  50%,
  60% {
    transform: translateY(-3rem) rotate(35deg);
  }
  55% {
    transform: translateY(-2rem) rotate(35deg);
  }
  70% {
    transform: translateY(-1.75rem) rotate(35deg);
  }
}
</style>
