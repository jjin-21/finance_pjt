<template>
  <div>
    <a :href="dNews.link" target="_blank">
      <h2 v-html="dNews.title ">
      </h2>
    </a>
    <div v-html="dNews.description">
    </div>
    <hr>
  </div>
</template>

<script setup>


const props = defineProps({
  dNews: Object
})
</script>

<style scoped>

</style>