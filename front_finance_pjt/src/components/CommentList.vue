<template>
  <div>
    <h3>CommentList</h3>
    <form @submit.prevent="createComment">
      <textarea v-model="comment" placeholder="댓글을 작성하세요"></textarea>
      <button type="submit">댓글 작성</button>
    </form>
    <CommentListItem
      v-for="comment in props.commentLst"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import CommentListItem from '@/components/CommentListItem.vue';
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const store = useCounterStore()
const comment = ref('');

const props = defineProps ({
  commentLst: Object
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
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>