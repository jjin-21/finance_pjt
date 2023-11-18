<template>
  <div>
    <h1>예금 목록!!</h1>
    <ProductDepositListItem
      v-for="dProduct in store.dProducts"
      :key="dProduct.id"
      :dProduct="dProduct"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import ProductDepositListItem from './ProductDepositListItem.vue';



const store = useCounterStore()
onMounted(() => {
  store.getDeposits()
})


</script>

<style scoped>

</style>