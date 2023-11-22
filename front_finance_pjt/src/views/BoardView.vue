<template>
  <v-container>
    <h1 class="text-h3 mb-4">자유게시판</h1>
    <v-row class="mb-4" >
      <v-col>
        <v-btn v-if="showPopularPosts" @click="togglePopularPosts" color="deep-purple-lighten-1"><h3>전체글</h3></v-btn>
        <v-btn v-if="!showPopularPosts" @click="togglePopularPosts" color="deep-purple-lighten-1"><h3>인기글</h3></v-btn>
      </v-col>
      <v-col>
        <RouterLink :to="{ name: 'CreateView' }">
          <v-btn color="primary"><h3>글 작성</h3></v-btn>
        </RouterLink>
      </v-col>
    </v-row>
    <BoardList v-if="!showPopularPosts"/>
    <BoardListPopular v-if="showPopularPosts"/>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/BoardList.vue'
import BoardListPopular from '@/components/BoardListPopular.vue';

const store = useCounterStore()
const showPopularPosts = ref(false)

onMounted(() => {
  store.getBoards()
})

const togglePopularPosts = () => {
  showPopularPosts.value = !showPopularPosts.value
}
</script>

<style scoped>
.text-h2 {
  font-size: 24px;
}

.mb-4 {
  margin-bottom: 16px;
}
</style>
