import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../views/MainPage.vue";
import UserPage from "../views/UserPage.vue";

const routes = [
  { path: "/", component: MainPage },
  { path: "/user/:id", component: UserPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
