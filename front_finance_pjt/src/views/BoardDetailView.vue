<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board">
      <p>제목 : {{ board.title }}</p>
      <p>내용 : {{ board.content }}</p>
      <span>이미지: </span>
      <div v-if="board.image">
        <img :src="getImageUrl(board.image)" alt="">
      </div>
      <p>작성일 : {{ formatDateTime(board.created_at) }}</p>
      <p>수정일 : {{ formatDateTime(board.updated_at) }}</p>
      <hr>
      <p>
        <span>
          좋아요 수 : {{ likeCount }}
        </span>
        <span>
          | |
        </span>
        <span>
          <button @click.prevent="likeBoard">좋아요</button>
        </span>
      </p>
      <hr>
      <p>
        <span @click.prevent="updateBoard" style="cursor: pointer">
          [수정]
        </span>
        <span @click.prevent="deleteBoard" style="cursor: pointer">
          [삭제]
        </span>
      </p>
      <hr>
      <CommentList 
        :commentLst="commentLst"
        :boardId="boardId"
      />
      <hr>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommentList from '@/components/CommentList.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const board = ref(null)
const comment = ref(null)
const commentLst = ref([])
const likeCount = ref(0)
const boardId = ref(0)

boardId.value = route.params.id
// console.log(route.params.id)

const getImageUrl = (imagePath) => {
  return `http://localhost:8000${imagePath}`;
}

const formatDateTime = (dateTimeString) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  return new Date(dateTimeString).toLocaleString('en-US', options).replace(/(\d+)\/(\d+)\/(\d+), (\d+:\d+:\d+)/, '$3-$1-$2 $4');
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/${route.params.id}/`
  })
    .then((res) => {
      console.log("onMount: ",res.data)
      board.value = res.data
      commentLst.value = res.data.comment_set
    })
    .catch((err) => {
      console.log(err)
    })

  

})



const updateBoard = function () {
  router.push({
    name: 'UpdateView',
    params: { 
      id: route.params.id
    }
  })
}

const deleteBoard = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/boards/${route.params.id}/`
  })
    .then((res) => {
      console.log(res)
      router.push({name : 'BoardView'})
      
    })
    .catch((err) => {
      console.log(err)
    })
}

const likeBoard = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/${Number(route.params.id)}/likes/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      likeCount.value = res.data.like_users.length;
    })
    .catch((err) => {
      console.log(err)
      
    })
}

watch(board, (newBoard) => {
  likeCount.value = newBoard.like_users.length;
})


</script>

<style>

</style>
