<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateBoard">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()
const route = useRoute()

onMounted(() => {
  const boardId = route.params.id
  // console.log(typeof boardId)
  const updateBoard = store.boards.find((board) => String(board.id) === boardId)
  // console.log(updateBoard)
  title.value = updateBoard.title
  content.value = updateBoard.content
})

const updateBoard = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'BoardView' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
