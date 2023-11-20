<template>
  <div>
    <h3>UserProfile View!</h3>
    
    <p>Username: {{ profileData.username }}</p>
    <p>Nickname: {{ profileData.nickname }}</p>
    <p>Email: {{ profileData.email }}</p>
    <p>PhoneNumber: {{ profileData.phone_num }}</p>
    <p>Gender: {{ genderType }}</p>
    <p>Asset: {{ profileData.asset }}</p>
    <p>Salary: {{ profileData.salary }}</p>
    <hr>
    <div>
      <span>
        <button @click.prevent="editProfile">[Edit]</button>
      </span>
      <span> || </span>
      <span>
        <button @click.prevnet="deleteProfile">[Delete]</button>
      </span>
    </div>
    <div>
      <span>
        <button @click.prevent="changePassword">[Change Password]</button>
      </span>
    </div>
    <hr>
    <br>
    <v-btn :to="({name: 'UserProfileProductView', params: {id: store.userId}})">
      <h3>내가 담은 상품</h3>
    </v-btn>
    


  </div>
  
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
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

const genderType = computed(() => {
  if (profileData.value && profileData.value.gender === 0) {
    return 'Male';
  } else if (profileData.value && profileData.value.gender === 1) {
    return 'Female';
  }
})


const editProfile = function () {
  router.push({
    name: 'UserProfileEditView',
    params: {
      id: store.userId
    }
  })
}

const deleteProfile = function () {
  router.push({
    name: 'UserProfileDeleteView',
    params: {
      id: store.userId
    }
  })
}

const changePassword = function () {
  router.push({
    name: 'UserProfileChangePasswordView',
    params: {
      id: store.userId
    }
  })
}




</script>

<style scoped>

</style>




