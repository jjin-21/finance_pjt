<template>
  <v-card
    class="mx-auto"
    max-width="700"
    title="User Profile Edit"
  >
    <v-container>
      <v-text-field
        v-model="username"
        color="primary"
        label="Username"
        variant="underlined"
      ></v-text-field>

      <v-text-field
      v-model="email"
      color="primary"
      label="Email"
      placeholder="Enter your email"
      variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="phonenum"
        color="primary"
        label="PhoneNumber"
        variant="underlined"
      ></v-text-field>
        
      <v-text-field
        v-model="nickname"
        color="primary"
        label="Nickname"
        variant="underlined"
      ></v-text-field>
      
      <v-select
        v-model="genderSelected"
        :items="genderOptions"
        color="primary"
        label="Gender"
        placeholder="Select Gender"
        variant="underlined"
      ></v-select>

      <v-text-field
        v-model="age"
        color="primary"
        label="Age"
        placeholder="숫자만 입력해주세요"
        variant="underlined"
        type="number"
      ></v-text-field>
      

      <v-text-field
      v-model="asset"
      color="primary"
      label="Asset"
      placeholder="숫자만 입력해주세요"
      variant="underlined"
      type="number"
      ></v-text-field>
      
      <v-text-field
      v-model="salary"
      color="primary"
      label="Salary"
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

const nickname = ref(null)
const age = ref(null)
const gender = ref(null)
const asset = ref(null)
const salary = ref(null)
const email = ref(null)
const phonenum = ref(null)

const genderSelected = ref(null)

const genderOptions = ref([
  'Male', 'Female'
])



const signUp = function () {
  const payload = {
    username: username.value,
    nickname: nickname.value,
    age: age.value,
    gender: gender.value,
    asset: asset.value,
    salary: salary.value,
    email: email.value,
    phone_num: phonenum.value
  }
  
  store.signUp(payload)
}

watch(genderSelected, (newGenderSelected) => {
  gender.value = newGenderSelected === 'Male' ? 0 : 1;
})


</script>

<style>

</style>
