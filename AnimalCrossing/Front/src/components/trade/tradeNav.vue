<template>
  <nav class="board__nav">
    <router-link to="/trade">
      <img
        src="../../assets/images/nav_neighbor.png"
        alt="neighbor"
        class="nav-img"
      />
    </router-link>
    <router-link to="/trade">
      <img
        src="../../assets/images/nav_painting.png"
        alt="painting"
        class="nav-img"
      />
    </router-link>
    <router-link to="/trade">
      <img src="../../assets/images/fossil.png" alt="fossil" class="nav-img" />
    </router-link>
    <router-link to="/trade">
      <img src="../../assets/images/nav_etc.png" alt="기타" class="nav-img" />
    </router-link>
    <router-link to="/trade/write">
      <img src="../../assets/images/write.png" alt="글쓰기" class="nav-img" />
    </router-link>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
/* navigation displaying the items evenly in a non-wrapping row */
.board__nav {
  display: flex;
  margin: 1rem 1rem;
  justify-content: space-evenly;
  width: 90%;
  justify-self: center;
}

/* navbar 이미지 사이즈 및 설정 */
.nav-img {
  height: 60px;
}

/* style the buttons to have a bit of whitespace around the text
a background is specified in the script */
.nav--item {
  border: none;
  background: none;
  color: inherit;
  font-size: 0.85rem;
  /* font-family: inherit; */
  font-family: "Jua", sans-serif;
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
