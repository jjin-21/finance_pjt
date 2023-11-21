<template>
  <div class="news-container">
    <a :href="sNews.link" target="_blank" class="news-link">
      <h2 class="news-title" v-html="sNews.title"></h2>
    </a>
    <div class="news-description" v-html="sNews.description"></div>
    <hr class="news-divider">
  </div>
</template>

<script setup>
const props = defineProps({
  sNews: Object,
});
</script>

<style scoped>
.news-container {
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 16px;
}

.news-link {
  text-decoration: none;
  color: #333;
}

.news-title {
  margin-bottom: 8px;
}

.news-description {
  color: #555;
}

.news-divider {
  margin-top: 16px;
  border: 0;
  border-top: 1px solid #eee;
}
</style>
