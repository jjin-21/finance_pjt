<template>
  <div>
    <hr>
    <p v-if="!isUpdating">
      <div>
        작성자: {{ comment.username }}
      </div>
      <div>
        {{ comment.content }}
      </div>      
    </p>
    <p v-if="isUpdating">
      <form @submit.prevent="updateComment">
        <input type="text" style="width: 300px;" v-model="commentContent">
        <p>
          <button type="submit">댓글 수정</button>
        </p>
      </form>
    </p>
    <p v-if="!isUpdating">
      <span>
        작성시간 : {{ comment.created_at }}
      </span>
      <span @click.prevent="updateState" style="cursor: pointer">
        [수정]
      </span>
      <span @click.prevent="deleteComment"  style="cursor: pointer">
        [삭제]
      </span>
      </p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const props = defineProps({
  comment: Object
})

// console.log(props.comment)


const store = useCounterStore()
const router = useRouter()
const isUpdating = ref(false)
const commentContent = ref(props.comment.content)



// 댓글 수정 창 변경
const updateState = function () {
  isUpdating.value = true
}



// 댓글 수정 제출
const updateComment = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/comment/${props.comment.id}/`,
    data: {
      content: commentContent.value
    }
  })
    .then((res) => {
      console.log(res)
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}



// 댓글 삭제
const deleteComment = function () {
  const userConfirmed = window.confirm('삭제하시겠습니까?')

  if (userConfirmed) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/boards/comment/${props.comment.id}/`
    })
      .then((res) => {
        console.log(res)
        router.go(0)
      })
      .catch((err) => {
        console.log(err)
      })
  }
}



</script>

<style scoped>

</style>