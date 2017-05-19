import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Main from '@/components/Main'
import Card from '@/components/Card'
import Emoji from '@/components/Emoji'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main,
      children: [{
        path: '/Card',
        name: 'card',
        component: Card
      }, { path: '/Emoji', name: 'emoji', component: Emoji }]
    },
  ]
})
