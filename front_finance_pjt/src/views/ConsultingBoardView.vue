<template>
  <v-container>
    <h2 class="text-h3 mb-4">QnA 게시판</h2>
    <v-row class="mb-4">
      <v-col>
        <RouterLink :to="{ name: 'ConsultingBoardCreateView' }">
          <v-btn color="primary"><h3>글작성</h3></v-btn>
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
  font-size: px;
}

.mb-4 {
  margin-bottom: 16px;
}
</style>
