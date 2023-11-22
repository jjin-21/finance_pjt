<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-text>
            <div v-if="board">
              <!-- Board Details -->
              <v-row>
                <v-col>
                  <v-row>
                    <v-col>
                      <h2 class="headline">제목: {{ board.title }}</h2>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                  <p class="caption">작성자: {{ board.username }} 작성일: {{ formatDateTime(board.created_at) }}</p>
                  <v-divider></v-divider>
                  <div v-if="board.image">
                    <v-img :src="getImageUrl(board.image)" alt="" style="max-height: 300px;"></v-img>
                  </div>
                  <br>
                  <p class="body-1 custom-body-1">{{ board.content }}</p>
                  <br>
                  <v-divider></v-divider>
                  
                  <!-- Like Section -->
                  

                  <!-- Action Buttons -->
                  <v-divider></v-divider>
                  <v-row>
                    <v-col class="d-flex justify-start mb-1">
                      <v-btn
                        class="ma-2"
                        color="orange-darken-2"
                        @click.prevent="goBack"
                      >
                        <v-icon
                          start
                          icon="mdi-arrow-left"
                        ></v-icon>
                        뒤로가기
                      </v-btn>
                    </v-col>
                    <v-col v-if="board.user === store.userId" class="d-flex justify-end mb-1">
                      <v-btn class="my-2" @click.prevent="updateBoard" color="primary">수정</v-btn>
                      <v-btn class="ma-2" @click.prevent="deleteBoard" color="error">삭제</v-btn>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>

                  <!-- Comment Section -->
                  <ConsultingAnswerList :commentLst="commentLst" :boardId="boardId" />
                  <v-divider></v-divider>
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
import ConsultingAnswerList from '@/components/ConsultingAnswerList.vue'

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
    url: `${store.API_URL}/consultings/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      board.value = res.data
      commentLst.value = res.data.answer_set
    })
    .catch((err) => {
      console.log(err)
    })

  

})



const updateBoard = function () {
  router.push({
    name: 'ConsultingBoardUpdateView',
    params: { 
      id: route.params.id
    }
  })
}

const deleteBoard = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/consultings/${route.params.id}/`
  })
    .then((res) => {
      console.log(res)
      router.push({name : 'ConsultingBoardView'})
      
    })
    .catch((err) => {
      console.log(err)
    })
}

const goBack = function () {
  router.push({name: 'ConsultingBoardView'})
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




</script>

<style scoped>
.custom-body-1 {
  font-size: 18px; /* Adjust the font size as needed */
}

.ml-2 {
  font-size: 16px;
  margin-left: 8px;
  font-weight: 600;
}
</style>
