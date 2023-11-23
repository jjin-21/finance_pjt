<template>
  <div>
    <h1> ProductView </h1>
    
    
    <v-container>
      <v-row>
        <v-col>
          <v-btn variant="outlined" @click="showDepositList">예금 목록</v-btn>
        </v-col>
        <v-col>
          <v-btn variant="outlined" @click="showSavingList">적금 목록</v-btn>
        </v-col>
        <!-- <v-col>
          <v-btn variant="outlined" @click="store.saveProducts">예적금 목록 불러오기</v-btn>
        </v-col> -->
      </v-row>

      <v-row>
        <v-col v-if="store.showDeposit">
          <ProductDepositList />
        </v-col>
        <v-col v-if="store.showSaving">
          <ProductSavingList />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';

import ProductDepositList from "@/components/ProductDepositList.vue";
import ProductSavingList from "@/components/ProductSavingList.vue";


const store = useCounterStore()

onMounted(() => {
  // store.saveProducts()
  store.getDeposits()
  store.getSavings()

})


const showDepositList = () => {
  store.showDepositList()
};

const showSavingList = () => {
  store.showSavingList()
};

</script>

<style scoped>

</style>