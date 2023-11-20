<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-text>
            <div v-if="board">
              <v-row>
                <v-col>
                  <v-row>
                    <v-col>
                      <v-divider></v-divider>
                      <v-row>
                        <v-col>
                          <h2 class="headline">제목: {{ board.title }}</h2>
                        </v-col>
                      </v-row>
                      <p class="caption">작성일: {{ formatDateTime(board.created_at) }}</p>
                      <div v-if="board.image">
                        <v-img :src="getImageUrl(board.image)" alt="" style="max-height: 300px;"></v-img>
                      </div>
                      <br>
                      <p class="body-1 custom-body-1">{{ board.content }}</p>
                      <v-divider></v-divider>
                      <v-row>
                        <v-col>
                          <v-row align="center">
                            <v-col>
                              <span class="body-2">좋아요 수 : {{ likeCount }}</span>
                              <v-btn @click.prevent="likeBoard" color="primary">좋아요</v-btn>
                            </v-col>
                          </v-row>
                        </v-col>
                      </v-row>
                      <v-divider></v-divider>
                      <v-row>
                        <v-col>
                          <v-btn @click.prevent="updateBoard" color="primary">수정</v-btn>
                          <v-btn @click.prevent="deleteBoard" color="error">삭제</v-btn>
                        </v-col>
                      </v-row>
                      <v-divider></v-divider>
                      <CommentList :commentLst="commentLst" :boardId="boardId" />
                      <v-divider></v-divider>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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

<style scoped>
.custom-body-1 {
  font-size: 18px; /* Adjust the font size as needed */
}

</style>
