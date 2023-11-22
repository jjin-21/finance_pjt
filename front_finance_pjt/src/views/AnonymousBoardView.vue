<template>
  <v-container>
    <h1 class="text-h2 mb-4">Free Board</h1>
    <v-row class="mb-4">
      <v-col>
        <RouterLink :to="{ name: 'AnonymousBoardCreateView' }">
          <v-btn color="primary">CREATE</v-btn>
        </RouterLink>
      </v-col>
    </v-row>
    <AnonymousBoardList />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/BoardList.vue'
import AnonymousBoardList from '@/components/AnonymousBoardList.vue';

const store = useCounterStore()

onMounted(() => {
  store.getAnonymousBoards()
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
