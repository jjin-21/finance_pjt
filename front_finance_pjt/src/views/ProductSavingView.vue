<template>
  <div>
    <h3>saving detail view</h3>
    <hr>
    <p>{{ productDetail.kor_co_nm }}</p>
    <p>{{ productDetail.fin_prdt_nm }}</p>
    <p>{{ productDetail.join_member }}</p>
    <p>{{ productDetail.join_way }}</p>
    <div v-if="productDetail.etc_note" v-html="productDetail.etc_note"></div>
    <v-btn
        class="ma-2"
        variant="text"
        icon="mdi-thumb-up"
        color="blue-lighten-2"
        @click="addProductToCart"
      ></v-btn>
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

const addProductToCart = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/finances/saving-product/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>