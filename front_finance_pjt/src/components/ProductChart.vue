<template>
  <div>
    <Bar
      v-if="chartData && chartData.datasets.length > 0"
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, watch } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref(null)
const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false, 
  aspectRatio: 1,
  scales: {
    x: {
      title: {
        display: true,
        text: 'Bank and Product'
      }
    },
    y: {
      title: {
        display: true,
        text: 'Interest Rate'
      }
    }
  }
})

const { props } = defineProps(['props'])

const transformData = (rawData) => {
  return rawData.map(product => {
    return {
      label: `${product.kor_co_nm} - ${product.fin_prdt_nm}`,
      data: [
        product.term_6 !== undefined ? product.term_6 : 0,
        product.term_12 !== undefined ? product.term_12 : 0,
        product.term_24 !== undefined ? product.term_24 : 0,
        product.term_36 !== undefined ? product.term_36 : 0
      ]
    }
  })
}

const updateChart = () => {
  const rawData = props && Array.isArray(props) ? props : []
  chartData.value = {
    labels: ['Term 6', 'Term 12', 'Term 24', 'Term 36'],
    datasets: transformData(rawData).map(product => ({
      label: product.label,
      data: product.data
    }))
  }
}

watch(() => props, () => {
  updateChart()
})

onMounted(() => {
  updateChart()
})
</script>
