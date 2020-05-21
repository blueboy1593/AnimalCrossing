<template>
  <div>
    <div class="board">
      <h1 class="board__heading">
        동물의숲 게시판
      </h1>
      <nav class="board__nav">
        <!-- ! the buttons added in the script, to include a background color for the specific category  -->
        <!-- <button class="nav--item active" data-item="all">All</button>
        <button class="nav--item" data-item="news">News</button>
        <button class="nav--item" data-item="updates">Updates</button>
        <button class="nav--item" data-item="maintenance">Maintenance</button>
        <button class="nav--item" data-item="events">Events</button>
        <button class="nav--item" data-item="important">Important</button> -->
      </nav>
      <section class="board__news">
        <router-view />
        <!-- ! news items added through the script according to 1. the latest date and 1. the selected category -->
        <!--
        <a class="news--item" href="#">
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
</template>

<script>
import RightTab from "@/components/RightTab.vue";
export default {
  components: {
    RightTab
  }
};
</script>

<style scoped>
/* * {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
} */
.right_tab {
  position: absolute;
  top: 30%;
  right: 9%;
}

body {
  color: hsl(0, 0%, 0%);
  font-family: "Open Sans", sans-serif;
}

/* include the board in the center of the viewport */
.board {
  max-width: 1000px;
  max-height: 2000px;
  width: 90vw;
  margin: 4rem auto;
  /* display grid without specifying any structure, at least beyond the media query
  this is mostly helpful for alignment purposes
  */
  display: grid;
  border: 4px solid hsl(207, 79%, 21%);
  background: #fff;
  box-shadow: 0 2px 5px hsla(0, 0%, 0%, 0.3);
  /* position relative to absolute position the pseudo element */
  position: relative;
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

/* for the heading include a slightly darker background */
.board__heading {
  /* margin to have the heading overlap on the surrounding border */
  margin: -4px;
  margin-bottom: 1.75rem;
  font-family: "Chivo", sans-serif;
  font-size: 1.25rem;
  color: #fff;
  background: hsl(200, 100%, 10%);
  padding: 0.75rem;
  padding-left: 1.5rem;
}

/* navigation displaying the items evenly in a non-wrapping row */
.board__nav {
  display: flex;
  margin: 1rem 2rem;
  justify-content: space-evenly;
  width: 80%;
  justify-self: center;
}
/* style the buttons to have a bit of whitespace around the text
a background is specified in the script */
.nav--item {
  border: none;
  background: none;
  color: inherit;
  font-size: 0.85rem;
  font-family: inherit;
  text-transform: capitalize;
  border-radius: 30px;
  letter-spacing: 0.05rem;
  padding: 0.3rem 0.75rem;
  cursor: pointer;
}

/* on hover and focused slightly decrease the color of the button and add an underline */
.nav--item:hover,
.nav--item:focus {
  color: hsl(0, 0%, 35%);
  text-decoration: underline;
}

/* for the section describing the news items, display the items in a single column layout */
.board__news {
  display: flex;
  margin: 1rem 0 3rem;
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

/* remove the default properties of the anchor links describing the news items */
.news--item {
  text-decoration: none;
  color: inherit;
  margin: 1.25rem 0;
  padding-left: 0.75rem;
}
/* on hover and when focused slightly decrease the weight of the anchor links */
.news--item:hover,
.news--item:focus {
  color: hsl(0, 0%, 35%);
}
.news--item .date {
  font-size: 0.8rem;
}
.news--item .brief {
  font-size: 0.9rem;
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
    grid-area: nav;
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
    grid-area: section;
    width: 90%;
    max-height: 380px;
  }
}
</style>
