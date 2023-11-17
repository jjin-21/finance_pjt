<template>
  <div>
    <h3>UserProfile View!</h3>
    
    <p>Username: {{ profileData.username }}</p>
    <p>Nickname: {{ profileData.nickname }}</p>
    <p>Email: {{ profileData.email }}</p>
    <p>PhoneNumber: {{ profileData.phone_num }}</p>
    <p>Gender: {{profileData.gender }}</p>
    <p>Asset: {{ profileData.asset }}</p>
    <p>Salary: {{ profileData.salary }}</p>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const profileData = ref([])


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/${store.userId}`
  })
    .then((res) => {
      console.log(res)
      console.log(res.data)
      profileData.value = res.data
      
    })
    .catch((err) => {
      console.log(err)
    })
})

// const genderType = computed(() => {
//   if (profileData.value && profileData.value.gender === 0) {
//     return 'Male';
//   } else if (profileData.value && profileData.value.gender === 1) {
//     return 'Female';
//   }
// })

</script>

<style scoped>

</style>



