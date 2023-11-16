<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board">
      <p>제목 : {{ board.title }}</p>
      <p>내용 : {{ board.content }}</p>
      <p>작성일 : {{ board.created_at }}</p>
      <p>수정일 : {{ board.updated_at }}</p>
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
      />
      <hr>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommentList from '@/components/CommentList.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
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


</script>

<style>

</style>
