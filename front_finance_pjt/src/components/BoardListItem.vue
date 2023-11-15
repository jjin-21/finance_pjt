<template>
  <div>
    <h5>{{ board.id }}</h5>
    <p>글쓴이 : {{ board.username }}</p>
    <p>제목 : {{ board.title }}</p>
    <p>내용 : {{ board.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: board.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  board: Object
})
</script>
