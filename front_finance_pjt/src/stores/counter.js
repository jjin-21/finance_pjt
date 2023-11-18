import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const boards = ref([])
  const exchanges = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userName = ref(null)
  const userNickname = ref(null)
  const userId = ref(null)
  const userEmail = ref(null)
  const themeColor = ref('light')
  const router = useRouter()
  

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
  // 환율 정보를 백엔드 db에 저장하도록 하는 함수
  const updateExChange = function () {
    axios({
      url: `${API_URL}/exchange-rates/save/`
    })
      .then((res) => {
        console.log(res)
        router.push({name: 'ExChangeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 환율 정보를 db로 부터불러오는 action
  const getExChange = function () {
    axios({
      method: 'get',
      url: `${API_URL}/exchange-rates/calculator/`
    })
      .then((res) => {
        console.log(res)
        exchanges.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const {
      username, password1, password2, nickname, age, gender, asset, salary, email, phone_num
     } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, age, gender, asset, salary, email, phone_num
      },
      headers: {
        'Content-Type': 'application/json',
      }
    })
      .then((res) => {
        console.log(res)
        window.alert('회원 가입이 완료 되었습니다')
        router.push({name: 'LogInView'})
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
        console.log(res.data)
        token.value = res.data.key
        userName.value = res.data.username
        userNickname.value = res.data.nickname
        userId.value = res.data.user
        userEmail.value = res.data.email
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
            token.value = null;
            userName.value = null;
            userNickname.value = null;
            userEmail.value = null;
            userId.value = null;
            console.log(res);
            router.push('/home')
        })
        .catch((err) => {
            console.log(err);
        });
      

   
    }

    const editProfile = function (payload) {
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/${userId.value}/`,
        data: {
          username: payload.username,
          nickname: payload.nickname,
          age: payload.age,
          gender: payload.gender,
          asset: payload.asset,
          salary: payload.salary,
          email: payload.email,
          phone_num: payload.phone_num
        }
      })
        .then((res) => {
          console.log(res)
          userEmail.value = payload.email
          userNickname.value = payload.nickname
        })
        .catch((err) => {
          console.log(err)
        })
    }

  



  return { editProfile, userName, userNickname, userId, userEmail, boards, themeColor, exchanges, API_URL, getBoards, signUp, logIn, getExChange, token, isLogin, logOut, updateExChange}
}, { persist: true })
