<template>
  <v-card
    class="mx-auto"
    max-width="700"
    title="회원정보수정"
  >
    <v-container>
      <v-text-field
        v-model="username"
        color="primary"
        label="아이디"
        variant="underlined"
      ></v-text-field>

      <v-text-field
      v-model="email"
      color="primary"
      label="이메일"
      placeholder="이메일을 입력해 주세요"
      variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="phonenum"
        color="primary"
        label="전화번호"
        placeholder="전화번호를 입력해 주세요"
        variant="underlined"
      ></v-text-field>
        
      <v-text-field
        v-model="nickname"
        color="primary"
        label="별명"
        variant="underlined"
      ></v-text-field>
      
      <v-select
        v-model="genderSelected"
        :items="genderOptions"
        color="primary"
        label="성별"
        placeholder="Select Gender"
        variant="underlined"
      ></v-select>

      <v-text-field
        v-model="company"
        color="primary"
        label="회사"
        placeholder="회사명을 입력해주세요"
        variant="underlined"
      ></v-text-field>

      <v-select
        v-model="finSelected"
        :items="finOptions"
        color="primary"
        label="금융업 종사자 여부"
        placeholder="선택해주세요"
        variant="underlined"
      ></v-select>

      <v-text-field
        v-model="age"
        color="primary"
        label="나이"
        placeholder="숫자만 입력해주세요"
        variant="underlined"
        type="number"
      ></v-text-field>
      

      <v-text-field
      v-model="asset"
      color="primary"
      label="자산"
      placeholder="숫자만 입력해주세요"
      variant="underlined"
      type="number"
      ></v-text-field>
      
      <v-text-field
      v-model="salary"
      color="primary"
      label="월급"
      placeholder="숫자만 입력해주세요"
      variant="underlined"
      type="number"
      ></v-text-field>
      
     
    </v-container>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn color="success" @click.prevent="editProfile">
        Edit Profile

        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { storeToRefs } from 'pinia';
import axios from 'axios'

const store = useCounterStore()


const username = ref(null)
const nickname = ref(null)
const age = ref(null)
const gender = ref(null)
const asset = ref(null)
const salary = ref(null)
const email = ref(null)
const phonenum = ref(null)
const company = ref(null)
const is_fin_job = ref(null)

const genderSelected = ref(null)
const finSelected = ref(null)

const genderOptions = ref([
  'Male', 'Female'
])

const finOptions = ref([
 '금융업 비종사자', '금융업 종사자'
])


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/${store.userId}`
  })
    .then((res) => {
      console.log(res)
      console.log(res.data)
      username.value = res.data.username
      nickname.value = res.data.nickname
      email.value = res.data.email
      phonenum.value = res.data.phone_num
      gender.value = res.data.gender
      age.value = res.data.age
      asset.value = res.data.asset
      salary.value = res.data.salary
      company.value = res.data.company
      finSelected.value = res.data.is_fin_job === 0 ? '금융업 비종사자' : '금융업 종사자'
      genderSelected.value = res.data.gender === 0 ? 'Male' : 'Female'
      
    })
    .catch((err) => {
      console.log(err)
    })
})



const editProfile = function () {
  const payload = {
    username: username.value,
    nickname: nickname.value,
    age: age.value,
    gender: gender.value,
    asset: asset.value,
    salary: salary.value,
    email: email.value,
    phone_num: phonenum.value,
    company: company.value,
    is_fin_job: is_fin_job.value
  }
  console.log(payload.username)
  
  store.editProfile(payload)
}





watch(genderSelected, (newGenderSelected) => {
  gender.value = newGenderSelected === 'Male' ? 0 : 1;
})

watch(finSelected, (newFinSelected) => {
  is_fin_job.value = newFinSelected === '금융업 비종사자' ? 0 : 1;
})



</script>

<style>

</style>
