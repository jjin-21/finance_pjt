import { createRouter, createWebHistory } from 'vue-router'
import BoardView from '@/views/BoardView.vue'
import DetailView from '@/views/BoardDetailView.vue'
import CreateView from '@/views/BoardCreateView.vue'
import SignUpView from '@/views/UserSignUpView.vue'
import LogInView from '@/views/UserLogInView.vue'
import LogOutView from '@/views/UserLogOutView.vue'
import HomeView from '@/views/Home.vue'
import KaKaoMapView from '@/views/KaKaoMapView.vue'
import ExChangeView from '@/views/ExChangeView.vue'
import ProductView from '@/views/ProductView.vue'
import UpdateView from '@/views/BoardUpdateView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import UserProfileEditView from '@/views/UserProfileEditView.vue'
import UserProfileDeleteView from '@/views/UserProfileDeleteView.vue'
import NewsView from '@/views/NewsView.vue'
import ProductDepositView from '@/views/ProductDepositView.vue'
import ProductSavingView from '@/views/ProductSavingView.vue'
import UserProfileChangePasswordView from '@/views/UserProfileChangePasswordView.vue'
import UserProfileProductView from '@/views/UserProfileProductView.vue'

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
      path: '/',
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
    },
    {
      path: '/product',
      name: 'ProductView',
      component: ProductView
    },
    {
      path: '/boards/:id/update/',
      name: 'UpdateView',
      component: UpdateView
    },
    {
      path: '/users/',
      name: 'UserProfileView',
      component: UserProfileView
    },
    {
      path: '/users/:id/edit',
      name: 'UserProfileEditView',
      component: UserProfileEditView
    },
    {
      path: '/users/:id/delete',
      name: 'UserProfileDeleteView',
      component: UserProfileDeleteView
    },
    {
      path: '/users/:id/change-password',
      name: 'UserProfileChangePasswordView',
      component: UserProfileChangePasswordView
    },
    {
      path: '/users/:id/product',
      name: 'UserProfileProductView',
      component: UserProfileProductView
    },
    {
      path: '/news/',
      name: 'NewsView',
      component: NewsView
    },
    {
      path: '/product/deposit/:id/',
      name: 'ProductDepositView',
      component: ProductDepositView
    },
    {
      path: '/product/saving/:id/',
      name: 'ProductSavingView',
      component: ProductSavingView
    }
  ]
})

import { useCounterStore } from '../stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if(
    (to.name === 'CreateView' || to.name === 'DetailView' ||
    to.name === 'ProductDepositView' || to.name === 'ProductSavingView')
    && !store.isLogin ) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다')
    return { name: 'BoardView'}
  }
  
})

export default router
