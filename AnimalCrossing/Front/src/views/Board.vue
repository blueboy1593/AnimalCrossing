<template>
  <div>
    <div class="boardContainer">
      <logoImage></logoImage>
      <div class="boardGreen">
        <ring></ring>
        <div class="boardGray">
          <!-- <h1 class="board__heading">
            동물의숲 게시판
          </h1> -->
          <section class="board__news">
            <router-view />
            <!-- ! news items added through the script according to 1. the latest date and 1. the selected category -->
            <!-- <a class="news--item" href="#">
                <p class="date">
                    Apr 26, 2019
                </p>
                <p class="title">
                    Lorem inpsum
                </p>
            </a> -->
          </section>
          <div class="right_tab">
            <RightTab />
          </div>
        </div>
      </div>
      <music></music>
    </div>
  </div>
</template>

<script>
import RightTab from "@/components/RightTab.vue";
import ring from "@/components/ring.vue";
import logoImage from "@/components/logoImage.vue";
import music from "@/components/music.vue";

export default {
  components: {
    RightTab,
    ring,
    logoImage,
    music
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.boardContainer {
  background-image: url("../../public/img/background.png");
  background-size: cover;
  height: 100vh;
}

body {
  margin: 0;
  background-color: #f2f2f2;
}

/* * {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
} */

.right_tab {
  position: absolute;
  top: 10%;
  right: 3.8%;
}

body {
  color: hsl(0, 0%, 0%);
  font-family: "Jua", sans-serif;
}

/* include the board in the center of the viewport */
.boardContainer {
  max-width: 100%;
  height: 100vh;
  display: grid;
  /* position: relative; */
  grid-template-columns: 1fr 20fr 1fr;
  grid-template-rows: 1fr 20fr 1fr;
  grid-template-areas:
    ". logoImage ."
    ". boardGreen ."
    ". . .";
}

/* include a slightly rotated rectangle of the same size of the board, right behind it */
.board:before {
  position: absolute;
  content: "";
  background: hsl(180, 90%, 2%);
  width: 100%;
  height: 100%;
  transform: rotate(-2deg) scale(1.02);
  z-index: -5;
}

.rings {
  margin-top: 20%;
  display: grid;
  grid-area: rings;
  background-image: none;
  grid-template-rows: 2fr 1fr 1fr 5fr 1fr 1fr 2fr;
  grid-template-areas:
    "."
    "ring1"
    "ring2"
    "."
    "ring3"
    "ring4"
    ".";
}

.boardGreen {
  top: 5%;
  left: 2%;
  grid-area: boardGreen;
  max-width: 90%;
  max-height: 90%;
  display: grid;
  background: rgba(10, 85, 10, 0.425);
  box-shadow: 0 2px 5px hsla(0, 0%, 0%, 0.3);
  position: relative;
  border-radius: 15px;

  grid-template-columns: 1fr 25fr 1fr;
  grid-template-rows: 2fr 20fr 2fr;
  grid-template-areas:
    "rings . ."
    "rings boardGray ."
    "rings . .";
}

.boardGray {
  background: rgba(255, 255, 255, 0.705);
  border-radius: 15px;
  display: grid;
  grid-area: boardGray;
}

/* for the heading include a slightly darker background */
.board__heading {
  margin-bottom: 1.75rem;
  font-family: "Jua", sans-serif;
  font-size: 1.25rem;
  color: #fff;
  background: hsl(200, 100%, 10%);
  padding: 0.75rem;
  padding-left: 1.5rem;
}

/* for the section describing the news items, display the items in a single column layout */
.board__news {
  display: flex;
  margin: 1rem 0 2rem;
  flex-direction: column;
  width: 80%;
  justify-self: center;
  /* dictate a maximum height to allow for vertical scroll */
  max-height: 500px;
  height: 435px;
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

/* on smaller viewports */
@media (max-width: 700px) {
  /* change the grid layout to have the heading atop the navigation and section elements */
  .board {
    grid-template-areas: "heading heading" "nav section";
    grid-template-columns: 1fr 2fr;
    grid-template-rows: auto 1fr;
  }

  .board__heading {
    grid-area: heading;
  }

  /* position the navigation items atop one another instead of side by side */
  .board__nav {
    /* grid-area: nav; */
    flex-direction: column;
    /* at the top of the container */
    align-self: start;
  }

  .board__nav .nav--item {
    text-align: left;
    margin: 0.75rem 0;
  }

  /* slightly increase the height of the container to include a taller board */
  .board__news {
    /* grid-area: section; */
    width: 90%;
    max-height: 380px;
  }
}
</style>
