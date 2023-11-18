<template>
  <v-card 
    class="mx-auto"
    style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);"
    min-width="450"
    min-height="350"
    title="User Login"
  >
    <v-container>
      <v-text-field
        v-model="username"
        color="primary"
        label="Username"
        variant="underlined"
        @keyup.enter="logIn"
      ></v-text-field>

      <v-text-field
        v-model="password"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
        type="password"
        @keyup.enter="logIn"
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

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }

  store.logIn(payload)
}


</script>

<style>

</style>
