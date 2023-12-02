<template>
  <div>
    <h1>
      추천금융상품
    </h1>
    <v-container>
      <v-row>
        <v-col>
          <v-btn @click="showDepositList" variant="outlined">예금 목록</v-btn>
        </v-col>
        <v-col>
          <v-btn @click="showSavingList" variant="outlined">적금 목록</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col v-if="showDeposit">

          <h3>예금 상품 리스트</h3>
          <v-data-table
            :headers="headers"
            :items="likedDepositList"
            density="compact"
            item-key="name"
            >
            <template v-slot:item="{ item }">
              <tr @click="navigateToDepositDetails(item.fin_prdt_cd)">
                <td>{{ item.kor_co_nm }}</td>
                <td>{{ item.fin_prdt_nm }}</td>
              </tr>
            </template>
          </v-data-table>  
        </v-col>
        <v-col v-if="showSaving">
          
          <h3>적금 상품 리스트</h3>
          <v-data-table
            :headers="headers"
            :items="likedSavingList"
            density="compact"
            item-key="name"
            >
            <template v-slot:item="{ item }">
              <tr @click="navigateToSavingDetails(item.fin_prdt_cd)">
                <td>{{ item.kor_co_nm }}</td>
                <td>{{ item.fin_prdt_nm }}</td>
              </tr>
            </template>
          </v-data-table>  
          

        </v-col>
      </v-row>
    </v-container>

    
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
import ProductChart from '@/components/ProductChart.vue';

const router = useRouter()

const store = useCounterStore()
const profileData = ref([])

const showDeposit = ref(false)
const showSaving = ref(false)


const likedDepositList = ref([])
const likedSavingList = ref([])


console.log(likedSavingList)

const headers =  [
        { title: '은행', align: 'start', sortable: true, key: 'kor_co_nm' },
        { title: '상품', align: 'start', sortable: false, key: 'fin_prdt_nm' },
      ]

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/recommends/${store.userId}/`
  })
    .then((res) => {
      console.log(res)
      console.log(res.data)
      likedDepositList.value = res.data.deposit_recommends
      likedSavingList.value = res.data.saving_recommends
      console.log(likedDepositList.value)
      console.log(likedSavingList.value)
    })
    .catch((err) => {
      console.log(err)
    })

})

const showDepositList = () => {
  showDeposit.value = true
  showSaving.value = false
};

const showSavingList = () => {
  showSaving.value = true
  showDeposit.value = false
};

const navigateToDepositDetails = (productId) => {
  console.log(productId)
  router.push({name: 'ProductDepositView', params:{id: productId}})
}
const navigateToSavingDetails = (productId) => {
  console.log(productId)
  router.push({name: 'ProductSavingView', params:{id: productId}})
}




</script>

<style scoped>

</style>