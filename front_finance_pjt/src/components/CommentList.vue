<template>
  <div>
    <h3>CommentList</h3>
    <form @submit.prevent="createComment">
      <textarea v-model="comment" style="width: 300px;" @keydown.enter="handleEnter" placeholder="댓글을 작성하세요"></textarea>
      <button type="submit">댓글 작성</button>
    </form>
    <hr>
    <hr>
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

// 쉬프트 엔터와 엔터의 구분 함수
const handleEnter = (event) => {
  // 엔터 키를 눌렀을 때의 로직을 수행합니다.
  if (event.shiftKey) {
    // 쉬프트 키가 눌려진 경우 줄바꿈을 수행합니다.
    comment.value += '\n';
  } else {
    // 쉬프트 키가 눌리지 않은 경우 (엔터만 눌린 경우) 폼을 제출합니다.
    createComment();
  }
};

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