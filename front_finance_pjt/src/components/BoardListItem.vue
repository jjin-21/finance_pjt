<template>
  <div>
    <h5>{{ board.id }}</h5>
    <p>글쓴이 : {{ board.username }}</p>
    <p>제목 : {{ board.title }}</p>
    <p>내용 : {{ board.content }}</p>
    
    <RouterLink :to="{ name: 'DetailView', params: { id: board.id }}">
      [상세보기]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { useRouter, RouterLink } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

const router = useRouter()

const props = defineProps({
                board: Object
              })



</script>
