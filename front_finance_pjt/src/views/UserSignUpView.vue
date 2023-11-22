<template>
  <v-card
    class="mx-auto"
    max-width="700"
    title="회원가입"
  >
    <v-container>
      <v-text-field
        v-model="username"
        color="primary"
        label="아이디"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password1"
        color="primary"
        label="비밀번호"
        placeholder="비밀번호를 입력해주세요"
        variant="underlined"
        type="password"
      ></v-text-field>

      <v-text-field
        v-model="password2"
        color="primary"
        label="비밀번호 재확인"
        placeholder="비밀번호를 재확인 해주세요"
        variant="underlined"
        type="password"
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

      <v-btn color="success" @click.prevent="signUp">
        Complete Registration

        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { storeToRefs } from 'pinia';

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const gender = ref(null)
const asset = ref(0)
const salary = ref(0)
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



const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
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
  
  store.signUp(payload)
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
