<template>
  <div>
    <h1>
      내가 담은 금융상품
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

          <ProductChart 
          :props="likedDepositList"
          />

          <h3>예금 상품 리스트</h3>
          <v-data-table
            :headers="headers"
            :items="likedDepositList"
            density="compact"
            item-key="name"
            >
            <template v-slot:item="{ item }">
              <tr @click="navigateToSavingDetails(item.fin_prdt_cd)">
                <td>{{ item.kor_co_nm }}</td>
                <td>{{ item.fin_prdt_nm }}</td>
                <td>{{ item.term_6 }}</td>
                <td>{{ item.term_12 }}</td>
                <td>{{ item.term_24 }}</td>
                <td>{{ item.term_36 }}</td>
              </tr>
            </template>
          </v-data-table>  
        </v-col>
        <v-col v-if="showSaving">
          
          <ProductChart 
          :props="likedSavingList"
          />
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
                <td>{{ item.term_6 }}</td>
                <td>{{ item.term_12 }}</td>
                <td>{{ item.term_24 }}</td>
                <td>{{ item.term_36 }}</td>
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
        { title: '6개월 금리', align: 'start', sortable: true, key: 'term_6' },
        { title: '12개월 금리', align: 'start', sortable: true, key: 'term_12' },
        { title: '24개월 금리', align: 'start', sortable: true, key: 'term_24' },
        { title: '36개월 금리', align: 'start', sortable: true, key: 'term_36' }
      ]

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/${store.userId}`
  })
    .then((res) => {
      console.log(res)
      console.log(res.data)
      profileData.value = res.data
      
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

const navigateToSavingDetails = (productId) => {
  console.log(productId)
  router.push({name: 'ProductSavingView', params:{id: productId}})
}

watch(profileData, (newProfileData) => {
  likedSavingList.value = store.sProducts.filter(product => newProfileData.saving.includes(product.id));
  likedDepositList.value = store.dProducts.filter(product => newProfileData.deposit.includes(product.id));
})



</script>

<style scoped>

</style>