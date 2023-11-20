<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <div class="header-container">
            <h3>ExChangeList</h3>
          </div>
        </v-col>
        <v-col class="text-right">
          <div class="header-container">
            <v-btn @click="refreshData" variant="outlined">환율 갱신하기</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-container>
    
    <div>
      <v-data-table
        :headers="headers"
        :items="exchangeList"
        density="compact"
        item-key="name"
      ></v-data-table>
    
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

export default {
  data() {
    return {
    
      exchangeList: [],
      headers: [
        { title: '화폐', align: 'start', sortable: false, key: 'cur_nm' },
        { title: '통화 단위', align: 'end', key: 'cur_unit' },
        { title: '팔때 가격', align: 'end', key: 'ttb' },
        { title: '살때 가격', align: 'end', key: 'tts' },
        { title: '기준가', align: 'end', key: 'deal_bas_r' },
      ],
      
    };
  },
  methods: {
    refreshData() {
      const store = useCounterStore();
      store.updateExChange();
      this.exchangeList = store.exchanges.filter(exchange => exchange.cur_unit !== 'KRW');
      
    },
  },
  mounted() {
    const store = useCounterStore();
    this.exchangeList = store.exchanges.filter(exchange => exchange.cur_unit !== 'KRW');
  },

 
};
</script>

<style scoped>
   
</style>