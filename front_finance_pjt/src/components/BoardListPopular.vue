<template>
  <div>
    <h3>인기 게시글</h3>
    <BoardListItem
      v-for="board in paginatedBoards"
      :key="board.id"
      :board="board"
    />
    <v-pagination
      v-if="totalPages > 1"
      v-model="currentPage"
      :length="totalPages"
      @input="loadPage"
    ></v-pagination>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import BoardListItem from '@/components/BoardListItem.vue'

const store = useCounterStore()
const currentPage = ref(1)
const itemsPerPage = 7

const paginatedBoards = ref([])
const totalPages = ref(1)

const updatePagination = () => {
  // Filter boards with like count greater than or equal to 1
  const filteredBoards = store.boards.filter(board => board.like_users.length >= 1)

  // Reverse the order of the boards and then slice them
  const reversedBoards = filteredBoards.slice().reverse()
  totalPages.value = Math.ceil(reversedBoards.length / itemsPerPage)
  const startIndex = (currentPage.value - 1) * itemsPerPage
  const endIndex = startIndex + itemsPerPage
  paginatedBoards.value = reversedBoards.slice(startIndex, endIndex)
}

watch(() => store.boards, updatePagination)
watch(currentPage, updatePagination)

const loadPage = (page) => {
  currentPage.value = page
}

updatePagination() // Initial setup

console.log(store.boards)
console.log(paginatedBoards)
</script>
