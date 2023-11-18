<template>
  <div>
    <h2>예금 뉴스</h2>
    <br>
    <NewsDepositListItem 
    v-for="dNews in store.dNewses.items"
    :key="dNews.id"
    :dNews="dNews"
    />

  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import NewsDepositListItem from './NewsDepositListItem.vue';

const store = useCounterStore()
onMounted(() => {
  store.getDepositNews()
})
</script>

<style scoped>

</style>