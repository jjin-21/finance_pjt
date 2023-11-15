<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board">
      <p>제목 : {{ board.title }}</p>
      <p>내용 : {{ board.content }}</p>
      <p>작성일 : {{ board.created_at }}</p>
      <p>수정일 : {{ board.updated_at }}</p>
      <hr>
      <form @submit.prevent="createComment">
        <input type="text" v-model="comment">
        <input type="submit">
      </form>
      <hr>
      <div v-for="comment in commentLst">
        <span>{{ comment.username }}</span>
        <span> - </span>
        <span>{{ comment.content }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const board = ref(null)
const comment = ref(null)
const commentLst = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      board.value = res.data
      commentLst.value = res.data.comment_set
    })
    .catch((err) => {
      console.log(err)
    })
})

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: comment.value,
    }
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
}


</script>

<style>

</style>
