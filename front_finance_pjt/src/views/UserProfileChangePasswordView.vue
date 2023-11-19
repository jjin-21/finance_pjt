<template>
  <v-card
    class="mx-auto"
    max-width="700"
    title="User Change Password"
  >
    <v-container>

      <v-text-field
      v-model="newpassword1"
      color="primary"
      label="New Password"
      placeholder="Enter your new password"
      variant="underlined"
      type="password"
      @keyup.enter="changePassword"
      ></v-text-field>

      <v-text-field
        v-model="newpassword2"
        color="primary"
        label="Repeat New Password"
        placeholder="Enter your new password"
        variant="underlined"
        type="password"
        @keyup.enter="changePassword"

      ></v-text-field>
     
    </v-container>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn color="success" @click.prevent="changePassword">
        Change Password

        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore()
const router = useRouter()
const newpassword1 = ref('')
const newpassword2 = ref('')

const changePassword = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/password/change/`,
    data: {
      new_password1: newpassword1.value,
      new_password2: newpassword2.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push('/home')
      window.alert('비밀번호가 변경되었습니다다')
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style scoped>

</style>