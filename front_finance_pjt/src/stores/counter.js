import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const boards = ref([])
  const consultingBoards = ref([])
  const anonymousBoards = ref([])
  const exchanges = ref([])
  const dProducts = ref([])
  const sProducts = ref([])
  const dNewses = ref([])
  const sNewses = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userName = ref(null)
  const userNickname = ref(null)
  const userId = ref(null)
  const userEmail = ref(null)
  const userCompany = ref(null)
  const userIsFinJob = ref(null)
  const themeColor = ref('light')

  // 예 적금 표기관련
  const showDeposit = ref(false)
  const showSaving = ref(false)
  const showDepositList = () => {
    showDeposit.value = true;
    showSaving.value = false;
  };
  const showSavingList = () => {
    showDeposit.value = false;
    showSaving.value = true;
  };
  //
  
  
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

  // DRF에 Consulting 조회 요청을 보내는 action
  const getConsultingBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/consultings/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        console.log(res)
        consultingBoards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // DRF에 Consulting 조회 요청을 보내는 action
  const getAnonymousBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/anonymous_boards/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        console.log(res)
        anonymousBoards.value = res.data
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
        window.alert("상품 정보를 불러왔습니다")
        router.push({name: 'ExChangeView'})
        getExChange()
        window.location.reload();

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

  // 백엔드 db에 api 불러와서 금융상품 저장
  const saveProducts = function() {
    axios({
      method: 'get',
      url: `${API_URL}/finances/save-products/`
    })
      .then((res) => {
        console.log(res)
        window.alert("상품 정보를 불러왔습니다")
        router.go(0)
      })
      .catch((res) => {
        console.log(err)
      })
  }

  // DRF에 deposit products 조회 요청 
  const getDeposits = function() {
    axios({
      method: 'get',
      url: `${API_URL}/finances/deposit-products/`      
    })
      .then((res) =>{
        console.log(res)
        dProducts.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // DRF에 saving products 조회 요청 
  const getSavings = function() {
    axios({
      method: 'get',
      url: `${API_URL}/finances/saving-products/`
      
    })
      .then((res) =>{
        console.log(res)
        sProducts.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 예금 뉴스 가져오는 함수
  const getDepositNews = function() {
    axios({
      method: 'get',
      url: `${API_URL}/news/deposit/`
    })
      .then((res) =>{
        console.log(res)
        dNewses.value = res.data
        console.log("dNewses")
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 적금 뉴스 가져오는 함수
  const getSavingNews = function() {
    axios({
      method: 'get',
      url: `${API_URL}/news/saving/`
    })
      .then((res) =>{
        console.log(res)
        sNewses.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const {
      username, password1, password2, nickname, age, gender, asset, salary, email, phone_num, company, is_fin_job
      } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, age, gender, asset, salary, email, phone_num, company, is_fin_job
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
        window.alert('정보 입력이 올바르지 않습니다.')
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
        userIsFinJob.value = res.data.is_fin_job
        userCompany.value = res.data.company
        router.push({ name : 'HomeView'})
      })
      .catch((err) => {
        console.log(err)
        window.alert("ID PASSWORD를 확인해 주세요")
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
            userIsFinJob.value = null;
            userCompany.value = null;
            console.log(res);
            router.push('/')
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
          phone_num: payload.phone_num,
          company: payload.company,
          is_fin_job: payload.is_fin_job
        }
      })
        .then((res) => {
          console.log(res)
          userEmail.value = payload.email
          userNickname.value = payload.nickname
          window.alert("유저정보가 변경되었습니다")
          router.push({name: 'UserProfileView'})
        })
        .catch((err) => {
          console.log(err)
        })
    }

  



  return { editProfile, userName, userNickname, userId, userEmail, userIsFinJob, userCompany, boards, themeColor, exchanges, API_URL, getBoards, signUp, logIn, getExChange, token, isLogin, logOut, updateExChange, 
    getDeposits, dProducts, getSavings, sProducts, saveProducts,
    getSavingNews, sNewses, getDepositNews, dNewses,
    showDeposit, showDepositList, showSaving, showSavingList,
    consultingBoards, getConsultingBoards, anonymousBoards, getAnonymousBoards
  }
}, { persist: true })
