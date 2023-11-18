<template>
  <div>
    <h1>적금 목록!!</h1>
    <ProductSavingListItem
      v-for="sProduct in store.sProducts"
      :key="sProduct.id"
      :sProduct="sProduct"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import ProductSavingListItem from './ProductSavingListItem.vue';



const store = useCounterStore()
onMounted(() => {
  store.getDeposits()
})


</script>

<style scoped>

</style>