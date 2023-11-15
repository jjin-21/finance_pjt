import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const boards = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const user_name = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 board 조회 요청을 보내는 action
  const getBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/boards/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        console.log(res)
        boards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        // console.log(res)
        // console.log(res.data)
        token.value = res.data.key
        console.log(username)
        user_name.value = username
        router.push({ name : 'HomeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) => {
        token.value = null
        user_name.value = null
        window.alert('로그아웃이 완료 되었습니다.')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    
  }



  return { boards, API_URL, getBoards, signUp, logIn, token, isLogin, user_name, logOut}
}, { persist: true })
