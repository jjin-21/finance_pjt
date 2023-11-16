import { createRouter, createWebHistory } from 'vue-router'
import BoardView from '@/views/BoardView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogOutView from '@/views/LogOutView.vue'
import HomeView from '@/views/Home.vue'
import KaKaoMapView from '@/views/KaKaoMapView.vue'
import ExChangeView from '@/views/ExChangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/boards/',
      name: 'BoardView',
      component: BoardView
    },
    {
      path: '/boards/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'LogOutView',
      component: LogOutView
    },
    {
      path: '/home',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/map',
      name: 'KaKaoMapView',
      component: KaKaoMapView
    },
    {
      path: '/exchange',
      name: 'ExChangeView',
      component: ExChangeView
    }
  ]
})

import { useCounterStore } from '../stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if(to.name === 'BoardView' && !store.isLogin ) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다')
    return { name: 'BoardView'}
  }
})

export default router
