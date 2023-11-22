<template>
  <v-container>
    <h1 class="text-h2 mb-4">QnA Page</h1>
    <v-row class="mb-4">
      <v-col>
        <RouterLink :to="{ name: 'ConsultingBoardCreateView' }">
          <v-btn color="primary">CREATE</v-btn>
        </RouterLink>
      </v-col>
    </v-row>
    <ConsultingBoardList />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ConsultingBoardList from '@/components/ConsultingBoardList.vue';
const store = useCounterStore()

onMounted(() => {
  store.getConsultingBoards()
})
</script>

<style scoped>
.text-h2 {
  font-size: 24px;
}

.mb-4 {
  margin-bottom: 16px;
}
</style>
