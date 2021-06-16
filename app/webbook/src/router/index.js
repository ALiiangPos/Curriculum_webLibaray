import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import webindex from '../views/webindex.vue'
import hello from '../views/hello.vue'
import login from "../views/login.vue"
import user from "../views/user.vue"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path:'/hello',
      name :"Hello" ,
      component:hello
    },
    {
      path:'/index' ,
      name:"Webindex" ,
      component:webindex
    },
    {
      path:"/login" ,
      name :"login",
      component:login
    },
    {
      path:"/userpage" ,
      name:"user",
      component:user ,
    }

  ]

})
