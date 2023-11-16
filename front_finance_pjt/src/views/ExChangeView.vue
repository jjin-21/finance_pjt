<template>
  <div>
    <h1>ExChangeView</h1>
    <p>환율계산기 작성</p>
    <v-container>
      <v-row>
        <v-col>
          <v-select
            v-model="selectedFromCurrency"
            :items="currencies"
            label="From Currency"
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field v-model="amount" label="Amount"></v-text-field>
        </v-col>
        <v-col>
          <v-btn @click="calculateExchange" variant="outlined">Calculate</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-divider></v-divider>
        <v-col>
          <v-select
            v-model="selectedToCurrency"
            :items="currencies"
            label="To Currency"
          ></v-select>
        </v-col>
        <v-col>
          <p>Result: {{ result.toFixed(2) }}</p>
        </v-col>
      </v-row>
    </v-container>
    <br>
    <ExChangeList />
    
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import ExChangeList from '@/components/ExChangeList.vue';

const store = useCounterStore();

onMounted(() => {
  store.getExChange();
});

const exchangeInfo = store.exchanges;

const currencies = exchangeInfo.map(info => info.cur_nm);

const selectedFromCurrency = ref('');
const selectedToCurrency = ref('');
const amount = ref(0);
const result = ref(0);

const calculateExchange = () => {
  const fromRateString = exchangeInfo.find(info => info.cur_nm === selectedFromCurrency.value)?.deal_bas_r;
  const toRateString = exchangeInfo.find(info => info.cur_nm === selectedToCurrency.value)?.deal_bas_r;

  const fromRate = getExchangeRate(fromRateString, selectedFromCurrency.value);
  const toRate = getExchangeRate(toRateString, selectedToCurrency.value);

  result.value = (parseFloat(amount.value) * fromRate) / toRate;
};

const getExchangeRate = (rateString, currency) => {
  // 간단한 환율 계산 로직
  let rate = parseFloat(rateString.replace(',', '')) || 1;

  // 일본 옌이나 인도네시아 루피아인 경우 100으로 나누기
  if (currency === '일본 옌' || currency === '인도네시아 루피아') {
    rate /= 100;
  }

  return rate;
};
</script>

<style scoped>

</style>