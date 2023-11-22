<template>
  <v-list>
    <v-list-item class="list-item-border">
      <v-list-item-content>
        <v-list-item-title class="text-h5 mb-2">
          <span @click.prevent="navigateToDetailView">
            <a href="" class="text-decoration-none">
              {{ board.title }} [{{ board.comment_set.length }}]
            </a>
          </span>
        </v-list-item-title>
        <v-list-item-subtitle>글쓴이: {{ board.username }} | 추천수: {{ board.like_users.length }} | 작성시간: {{ formatDateTime(board.created_at) }}</v-list-item-subtitle>
      </v-list-item-content>
      <v-divider></v-divider>
    </v-list-item>
  </v-list>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { defineProps } from 'vue'


const props = defineProps({
  board: Object
})

const router = useRouter()

const formatDateTime = (dateTimeString) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  return new Date(dateTimeString).toLocaleString('en-US', options).replace(/(\d+)\/(\d+)\/(\d+), (\d+:\d+:\d+)/, '$3-$1-$2 $4');
}

const navigateToDetailView = () => {
  // Optional: Add logic if needed before navigating
  router.push({ name: 'AnonymousBoardDetailView', params: { id: props.board.id } })
}
</script>

<style scoped>
.text-h5 {
  font-size: 1.25rem;
}

.mb-2 {
  margin-bottom: 8px;
}

/* Style for the clickable title */
.text-h5 .v-list-item__content span {
  cursor: pointer;
}

.list-item-border {
  border: 2px solid #ccc; /* Adjust the border style as needed */
  border-radius: 5px; /* Optional: Add border radius for rounded corners */
}


</style>


