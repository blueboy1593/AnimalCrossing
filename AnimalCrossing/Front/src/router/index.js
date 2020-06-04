import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

import Home from "../views/Home.vue";
import Info from "../views/Info.vue";
import Community from "../views/Community.vue";
import NotFound from "../views/404Page.vue";
import Board from "../views/Board.vue";
import MooCalculator from "../views/MooCalculator.vue";
import MooCalculated from "../views/MooCalculated.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import infoDetail from "../components/info/infoDetail.vue";
import trade from "../views/trade.vue";
import Detail from "../views/Detail.vue";

Vue.use(VueRouter);
// const detail = () =>
//   import(
//     /* webpackChunkName: "c_detail" */ "../components/community/CommunityDetail.vue"
//   );

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
        path: "/detail",
        name: "detail",
        component: Detail
      },
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
            path: "list",
            component: () => import("../components/community/CommunityPost.vue")
          },
          {
            path: "cdetail/:id",
            name: "cdetail",
            component: () =>
              import("../components/community/CommunityDetail.vue")
          },
          {
            path: "write",
            component: () =>
              import("../components/community/CommunityWrite.vue")
          }
        ]
      },
      {
        path: "/moocalculator",
        name: "Moocalculator",
        component: MooCalculator,
        props: true
      },
      {
        path: "/mooCalculated",
        name: "MooCalculated",
        component: MooCalculated,
        props: true
        // 이거를 해줘야해...? 좀 천재적인거 아냐?
      },
      {
        path: "/login",
        name: "Login",
        component: Login
      },
      {
        path: "/logout",
        name: "logout",
        beforeEnter(to, from, next) {
          store.commit("logout");
          alert("로그아웃 되었습니다.");
          next("/info/fish");
        }
      },
      {
        path: "/signup",
        name: "Signup",
        component: Signup
      },
      {
        path: "/test2",
        name: "trade",
        component: trade
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
