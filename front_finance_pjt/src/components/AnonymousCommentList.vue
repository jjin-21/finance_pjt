<template>
  <v-container>
    <v-row>
      <v-col>
        <h3 class="mb-4">Comment List</h3>
        <form @submit.prevent="createComment" class="d-flex">
          <v-textarea
            v-model="comment"
            label="댓글을 작성하세요"
            outlined
            rows="1"
            class="mb-1 mr-2"
            @keydown.enter="handleEnter"
          ></v-textarea>
          <v-btn type="submit" style="height: 56px;">댓글 작성</v-btn>
        </form>
        <AnonymousCommentListItem
          v-for="comment in paginatedComments"
          :key="comment.id"
          :comment="comment"
        />
        <v-pagination
          v-if="totalPages > 1"
          v-model="currentPage"
          :length="totalPages"
          @input="changePage"
        ></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import CommentListItem from '@/components/CommentListItem.vue';
import { ref, computed } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';
import AnonymousCommentListItem from './AnonymousCommentListItem.vue';

const route = useRoute();
const router = useRouter();
const store = useCounterStore();
const comment = ref('');
const commentsPerPage = 5;

const props = defineProps({
  commentLst: Object,
  boardId: String,
});

const totalPages = computed(() => Math.ceil(props.commentLst.length / commentsPerPage));

const currentPage = ref(1);

const changePage = (page) => {
  router.push({ query: { page } });
};

const handleEnter = (event) => {
  if (event.shiftKey) {
    comment.value += '\n';
  } else {
    createComment();
  }
};

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/anonymous_boards/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      content: comment.value,
    },
  })
    .then((res) => {
      console.log(res);
      router.go(0);
    })
    .catch((err) => {
      console.log(err);
    });
};

const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * commentsPerPage;
  const end = start + commentsPerPage;
  return props.commentLst.slice(start, end);
});

</script>

<style scoped>
/* Add custom styling if needed */
</style>
