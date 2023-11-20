<template>
  <v-card 
    class="mx-auto"
    style="position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%);"
    min-width="450"
    min-height="350"
    title="User Login"
  >
    <v-container>
      <v-text-field
        v-model="username"
        ref="usernameField"
        color="primary"
        label="Username"
        variant="underlined"
        @keyup.enter="logIn"
        hide-details="auto"
        :rules="[usernameCheck]"
        :error-messages="usernameError"
      ></v-text-field>

      <v-text-field
        v-model="password"
        ref="passwordField"
        color="primary"
        label="Password"
        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show1 ? 'text' : 'password'"
        @click:append="show1 = !show1"
        placeholder="Enter your password"
        variant="underlined"
        type="password"
        @keyup.enter="logIn"
        hide-details="auto"
        :rules="[passwordCheck]"
        :error-messages="passwordError"
      ></v-text-field>

     
    </v-container>
    

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn color="success" @click.prevent="logIn">
        LOGIN

        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()
const username = ref(null)
const password = ref(null)
const show1 = ref(false)

const usernameError = ref('')
const passwordError = ref('')


const usernameField = ref(null)
const passwordField = ref(null)


const usernameCheck = () => {
  usernameError.value = !username.value
    ? 'Username is required.'
    : '';
  
  return true
}

const passwordCheck = () => {
  passwordError.value = !password.value
    ? 'Password is required.'
    : '';
  
  return true
}

const logIn = function () {

  const payload = {
    username: username.value,
    password: password.value
  }

  store.logIn(payload);
}





</script>

<style>

</style>
