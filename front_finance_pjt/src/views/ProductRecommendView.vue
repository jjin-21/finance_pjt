<template>
  <div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const data = ref(null)
const store = useCounterStore()

onMounted(() => {
  axios({
  method: 'get',
  url: `${store.API_URL}/recommends/${store.userId}/`,
  headers: {
      Authorization: `Token ${store.token}`,
    }
})
  .then((res) => {
    console.log(res)
  })
  .catch((err) => {
    console.log(err)
  })
})


</script>

<style scoped>

</style>