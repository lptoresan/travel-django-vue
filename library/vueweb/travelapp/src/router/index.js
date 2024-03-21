import Vue from 'vue'
import VueRouter from 'vue-router'
import List from '../views/List.vue'
import FormView from '../views/FormView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/form',
    name: 'form',
    component: FormView, 
    beforeEnter: (to, from, next) => {
      // Check if token exists in local storage
      if (!localStorage.getItem('token')) {
        next({ name: 'login'});
      } else {
        next();
      }
    }
  },
  {
    path: '/list',
    name: 'list',
    component: List, 
    beforeEnter: (to, from, next) => {
      if (!localStorage.getItem('token')) {
        next({ name : 'login'});
      } else {
        next();
      }
    }
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router