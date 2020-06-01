import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Info from "../views/Info.vue";
import Community from "../views/Community.vue";
import NotFound from "../views/404Page.vue";
import Board from "../views/Board.vue";
import MooCalculator from "../views/MooCalculator.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import infoDetail from "../components/info/infoDetail.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/test",
    name: "test",
    component: infoDetail
  },
  {
    path: "/",
    name: "Board",
    component: Board,
    children: [
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
          },
          {
            path: "neighbor",
            component: () => import("../components/info/Neighbor.vue")
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
        path: "/moocalculator",
        name: "Moocalculator",
        component: MooCalculator
      },
      {
        path: "/login",
        name: "Login",
        component: Login
      },
      {
        path: "/signup",
        name: "Signup",
        component: Signup
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
