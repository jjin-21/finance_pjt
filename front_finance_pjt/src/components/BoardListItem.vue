<template>
  <v-list>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h5 mb-2">
          <span @click.prevent="navigateToDetailView">
            <a href="" class="text-decoration-none">
              {{ board.title }} [{{ board.comment_set.length }}]
            </a>
          </span>
        </v-list-item-title>
        <v-list-item-subtitle>글쓴이: {{ board.username }} | 추천수: {{ board.like_users.length }}</v-list-item-subtitle>
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

const navigateToDetailView = () => {
  // Optional: Add logic if needed before navigating
  router.push({ name: 'DetailView', params: { id: props.board.id } })
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


</style>


