<template>
  <div>
    <h1> ProductView </h1>
    
    
    <v-container>
      <v-row>
        <v-col>
          <v-btn @click="showDepositList">예금 목록</v-btn>
        </v-col>
        <v-col>
          <v-btn @click="showSavingList">적금 목록</v-btn>
        </v-col>
        <v-col>
          <v-btn @click="store.saveProducts">예적금 목록 불러오기</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col v-if="showDeposit">
          <ProductDepositList />
        </v-col>
        <v-col v-if="showSaving">
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

const showDeposit = ref(false);
const showSaving = ref(false);
const store = useCounterStore()

onMounted(() => {
  showDeposit.value = false
  showSaving.value = false
  // store.saveProducts()
  store.getDeposits()
  store.getSavings()

})


const showDepositList = () => {
  showDeposit.value = true;
  showSaving.value = false;
};

const showSavingList = () => {
  showDeposit.value = false;
  showSaving.value = true;
};

</script>

<style scoped>

</style>