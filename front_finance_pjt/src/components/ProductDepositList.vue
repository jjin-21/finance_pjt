<template>
  <div>
    <h3>예금 목록</h3>
    <v-data-table
        :headers="headers"
        :items="store.dProducts"
        density="compact"
        item-key="name"
        >
        <template v-slot:item="{ item }">
          <tr @click="navigateToProductDetails(item.fin_prdt_cd)">
            <td>{{ item.kor_co_nm }}</td>
            <td>{{ item.fin_prdt_nm }}</td>
            <td>{{ item.term_6 }}</td>
            <td>{{ item.term_12 }}</td>
            <td>{{ item.term_24 }}</td>
            <td>{{ item.term_36 }}</td>
          </tr>
        </template>
      </v-data-table>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()


console.log(store.dProducts)
const headers =  [
        { title: '은행', align: 'start', sortable: true, key: 'kor_co_nm' },
        { title: '상품', align: 'start', sortable: false, key: 'fin_prdt_nm' },
        { title: '6개월 금리', align: 'start', sortable: true, key: 'term_6' },
        { title: '12개월 금리', align: 'start', sortable: true, key: 'term_12' },
        { title: '24개월 금리', align: 'start', sortable: true, key: 'term_24' },
        { title: '36개월 금리', align: 'start', sortable: true, key: 'term_36' }
      ]


const depositProductList = ref([])

const navigateToProductDetails = (productId) => {
  console.log(productId)
  router.push({name: 'ProductDepositView', params:{id: productId}})
}


onMounted(() => {
  depositProductList.value = store.dProducts
})


</script>

<style scoped>

</style>