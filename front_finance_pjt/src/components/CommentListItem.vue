<template>
  <div>
    <hr>
    {{ comment.username }}
     - 
    {{ comment.content }}
  </div>
</template>

<script setup>
const props = defineProps({
  comment: Object
})
</script>

<style scoped>

</style>