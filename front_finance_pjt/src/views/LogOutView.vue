<template>
  <div>

  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useCounterStore()

onMounted(() => {
  store.logOut()
  router.push({name : 'HomeView'})
})


</script>

<style scoped>

</style>