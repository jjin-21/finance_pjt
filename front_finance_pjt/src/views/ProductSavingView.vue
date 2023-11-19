<template>
  <div>
    <h3>deposit detail view</h3>
    <hr>
    <p>{{ productDetail.kor_co_nm }}</p>
    <p>{{ productDetail.fin_prdt_nm }}</p>
    <p>{{ productDetail.join_member }}</p>
    <p>{{ productDetail.join_way }}</p>
    <div v-if="productDetail.etc_note" v-html="productDetail.etc_note"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'

const store = useCounterStore()
const route = useRoute()
const productDetail = ref([])




onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finances/saving-product/${route.params.id}/`);
    console.log(response)
    productDetail.value = response.data;

  } catch (error) {
    console.error(error);
  }
});

</script>

<style scoped>

</style>