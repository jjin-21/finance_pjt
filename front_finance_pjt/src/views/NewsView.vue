<template>
  <div>
    <h1> NewsView </h1>
    
    
    <v-container>
      <v-row>
        <v-col>
          <v-btn variant="outlined" @click="showDepositList">예금 상품 뉴스</v-btn>
        </v-col>
        <v-col>
          <v-btn variant="outlined" @click="showSavingList">적금 상품 뉴스</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col v-if="showDeposit">
          <NewsDepositList />
        </v-col>
        <v-col v-if="showSaving">
          <NewsSavingList />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import NewsDepositList from '@/components/NewsDepositList.vue';
import NewsSavingList from '@/components/NewsSavingList.vue';

const showDeposit = ref(false);
const showSaving = ref(false);
onMounted(() => {
  showDeposit.value = false
  showSaving.value = false
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