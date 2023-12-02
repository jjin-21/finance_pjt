<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h3 class="text-h6 font-weight-bold">적금 상품 상세 정보</h3>
        <v-divider class="mb-4"></v-divider>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="elevation-2" v-theme="{ dark: $vuetify.theme.dark }">
          <v-card-title class="text-h6 font-weight-bold">{{ productDetail.kor_co_nm }}</v-card-title>
          <v-card-subtitle>{{ productDetail.fin_prdt_nm }}</v-card-subtitle>

          <div class="card-text">
            <p>가입대상: {{ productDetail.join_member }}</p>
            <p>가입방법: {{ productDetail.join_way }}</p>
            <v-divider class="my-2"></v-divider>
            <p>상품특징</p>
            <div v-if="productDetail.etc_note || productDetail.spcl_cnd">
              <p v-if="productDetail.etc_note" class="mb-2" v-html="productDetail.etc_note"></p>
              <p v-if="productDetail.spcl_cnd" class="mb-2" v-html="productDetail.spcl_cnd"></p>
              <v-divider class="my-2"></v-divider>
            </div>
          </div>

          <v-card-actions>
            <v-btn class="ma-2 custom-btn" icon color="blue-lighten-2" @click="addProductToCart" v-if="!likedProductState">
              <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
            <v-btn class="ma-2 custom-btn" icon color="red" @click="addDislikeToCart" v-if="likedProductState">
              <v-icon>mdi-thumb-down</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore();
const route = useRoute();
const productDetail = ref({});
const userProfileData = ref({})

const likedProductState = ref(null)

const fetchProductDetails = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finances/saving-product/${route.params.id}/`);
    productDetail.value = response.data;

    const userProfileResponse = await axios.get(`${store.API_URL}/accounts/profile/${store.userId}`);
    userProfileData.value = userProfileResponse.data;
    console.log(userProfileData.value)

    likedProductState.value = userProfileData.value.saving.includes(response.data.id);
    console.log(likedProductState.value)
  } catch (error) {
    console.error('Error fetching product details:', error);
    // Additional error handling or user notification can be implemented here
  }
};

onMounted(fetchProductDetails);

const addProductToCart = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/finances/saving-product/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    console.log('Product added to cart:', response);
    likedProductState.value = true
    // Additional success handling or user notification can be implemented here
  } catch (error) {
    console.error('Error adding product to cart:', error);
    // Additional error handling or user notification can be implemented here
  }
}

const addDislikeToCart = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/finances/saving-product/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    console.log('Product added to cart:', response);
    likedProductState.value = false
    // Additional success handling or user notification can be implemented here
  } catch (error) {
    console.error('Error adding product to cart:', error);
    // Additional error handling or user notification can be implemented here
  }
}


</script>

<style scoped>
/* Basic font and color settings */
body {
  font-family: 'Google Sans', sans-serif;
  color: #333;
}

/* Custom card styling */
.custom-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
}

/* Custom button styling */
.custom-btn {
  background-color: rgb(202, 204, 202);
  color: #fff;
}
</style>
