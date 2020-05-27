import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Info from "../views/Info.vue";
import Community from "../views/Community.vue";
import NotFound from "../views/404Page.vue";
// import Board from '../views/Board.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  // {
  //   path: "/",
  //   name: "Board",
  //   component: Board
  // },
  {
    path: "/info",
    name: "Info",
    component: Info,
    children: [
      {
        path: "fish",
        component: () => import("../components/info/Fish.vue")
      },
      {
        path: "flower",
        component: () => import("../components/info/Flower.vue")
      },
      {
        path: "fossil",
        component: () => import("../components/info/Fossil.vue")
      },
      {
        path: "insect",
        component: () => import("../components/info/Insect.vue")
      },
      {
        path: "painting",
        component: () => import("../components/info/Painting.vue")
      }
    ]
  },
  {
    path: "/community",
    name: "Community",
    component: Community,
    children: [
      {
        path: "trade",
        component: () => import("../components/community/Trade.vue")
      },
      {
        path: "show",
        component: () => import("../components/community/Show.vue")
      },
      {
        path: "friend",
        component: () => import("../components/community/Friend.vue")
      }
    ]
  },

  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },

  // 404 page redirect
  {
    path: "/pageNotFound",
    name: "NotFound",
    component: NotFound
  },
  {
    path: "*",
    redirect: { name: "NotFound" }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
