import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
// import CustomersView from "../views/CustomersView.vue";
// import ChartersView from "../views/ChartersView.vue";
// import PilotsView from "../views/ChartersView.vue";
// import AircraftsView from "../views/ChartersView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/customers",
    name: "customers",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "customers" */ "../views/CustomersView.vue"),
  },
  {
    path: "/charters",
    name: "charters",
    component: () =>
      import(/* webpackChunkName: "charters" */ "../views/ChartersView.vue"),
  },
  {
    path: "/pilots",
    name: "pilots",
    component: () =>
      import(/* webpackChunkName: "pilots" */ "../views/PilotsView.vue"),
  },
  {
    path: "/aircrafts",
    name: "aircrafts",
    component: () =>
      import(/* webpackChunkName: "aircrafts" */ "../views/AircraftsView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
