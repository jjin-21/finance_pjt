<template>
  <v-divider class="my-4"></v-divider>
  <v-row align="end">
    <v-col>
      <v-card>
        <v-card-text>
          <v-row>
            <v-col v-if="!isUpdating" class="d-flex justify-space-between align-center">
              <div>
                작성자: {{ comment.username }} 작성시간: {{ formatDateTime(comment.created_at) }}
              </div>
            </v-col>
            <v-col v-if="isUpdating">
              <form @submit.prevent="updateComment">
                <v-text-field
                  v-model="commentContent"
                  label="댓글을 수정하세요"
                ></v-text-field>
                <v-btn type="submit">댓글 수정</v-btn>
              </form>
            </v-col>
          </v-row>
          <v-row>
            <v-col v-if="!isUpdating" class="d-flex justify-space-between align-center">
              <p>{{ comment.content }}</p>
              <v-col v-if="store.userId === comment.user" class="d-flex justify-end align-center">
                <v-btn @click.prevent="updateState">
                  수정
                </v-btn>
                <v-btn class="m-0" @click.prevent="deleteComment">
                  삭제
                </v-btn>
              </v-col>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>



<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const props = defineProps({
  comment: Object,
});

const store = useCounterStore();
const router = useRouter();
const isUpdating = ref(false);
const commentContent = ref(props.comment.content);

const formatDateTime = (dateTimeString) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  return new Date(dateTimeString).toLocaleString('en-US', options).replace(/(\d+)\/(\d+)\/(\d+), (\d+:\d+:\d+)/, '$3-$1-$2 $4');
};

const updateState = function () {
  isUpdating.value = true;
};

const updateComment = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/comment/${props.comment.id}/`,
    data: {
      content: commentContent.value,
    },
  })
    .then((res) => {
      commentContent.value = res.data.content;
      isUpdating.value = false;
      // router.push({ name: 'DetailView', params: { id: props.comment.board.id } });
      router.go(0)
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteComment = function () {
  const userConfirmed = window.confirm('삭제하시겠습니까?');

  if (userConfirmed) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/boards/comment/${props.comment.id}/`,
    })
      .then((res) => {
        console.log(res);
        router.go(0);
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>

<style scoped>
/* Add custom styling if needed */
</style>