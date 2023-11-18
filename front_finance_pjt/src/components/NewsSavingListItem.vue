<template>
  <div>
    <a :href="sNews.link" target="_blank">
      <h2 v-html="sNews.title ">
      </h2>
    </a>
    <div v-html="sNews.description">
    </div>
    <hr>
  </div>
</template>

<script setup>


const props = defineProps({
  sNews: Object
})
</script>

<style scoped>

</style>