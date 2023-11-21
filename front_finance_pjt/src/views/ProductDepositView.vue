<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h3 class="text-h6 font-weight-bold">Deposit Detail View</h3>
        <v-divider class="mb-4"></v-divider>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="custom-card">
          <v-card-title class="text-h6 font-weight-bold">{{ productDetail.kor_co_nm }}</v-card-title>
          <v-card-title>{{ productDetail.fin_prdt_nm }}</v-card-title>
          
          <div class="card-text">
            <p>가입대상: {{ productDetail.join_member }}</p>
            <p>가입방법: {{ productDetail.join_way }}</p>
            <v-divider class="my-2"></v-divider>
            <div v-if="productDetail.etc_note || productDetail.spcl_cnd">
              <p v-if="productDetail.etc_note" class="mb-2" v-html="productDetail.etc_note"></p>
              <p v-if="productDetail.spcl_cnd" class="mb-2" v-html="productDetail.spcl_cnd"></p>
              <v-divider class="my-2"></v-divider>
            </div>
          </div>
          
          <v-card-actions>
            <v-btn class="ma-2 custom-btn" icon color="blue-lighten-2" @click="addProductToCart">
              <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <template>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google+Sans&display=swap">
    </template>
  </v-container>

</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore();
const route = useRoute();
const productDetail = ref({});

const fetchProductDetails = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finances/deposit-product/${route.params.id}/`);
    productDetail.value = response.data;
  } catch (error) {
    console.error('Error fetching product details:', error);
    // 추가적인 오류 처리 또는 사용자 알림 구현
  }
};

onMounted(fetchProductDetails);

const addProductToCart = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/finances/deposit-product/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    console.log('Product added to cart:', response);
    // 추가적인 성공 처리 또는 사용자 알림 구현
  } catch (error) {
    console.error('Error adding product to cart:', error);
    // 추가적인 오류 처리 또는 사용자 알림 구현
  }
}
</script>

<style scoped>
/* 기본 폰트 및 색상 설정 */
body {
  font-family: 'Open Sans', sans-serif;
  color: #333;
}


</style>
