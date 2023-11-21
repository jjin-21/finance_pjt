<template>
  <div :style="{ backgroundColor: getBackgroundColor()}" class="news-container">
    <a :href="dNews.link" target="_blank" class="news-link">
      <h2 class="news-title" v-html="dNews.title"></h2>
    </a>
    <div class="news-description" v-html="dNews.description"></div>
    <hr class="news-divider">
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const props = defineProps({
  dNews: Object,
});

const getBackgroundColor = () => {
  return store.themeColor === 'dark' ? '#EEEEEE' : '#fff';
};
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
