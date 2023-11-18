<template>
  <div>
    <h2>적금 뉴스</h2>
    <br>
    <NewsSavingListItem
    v-for="sNews in store.sNewses.items"
    :key="sNews.id"
    :sNews="sNews"
    />

  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import NewsSavingListItem from './NewsSavingListItem.vue';

const store = useCounterStore()
onMounted(() => {
  store.getSavingNews()
})
</script>

<style scoped>

</style>