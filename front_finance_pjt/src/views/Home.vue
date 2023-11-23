<template>
  <div class="background-image">
    <div class="overlay-head">
      <h1>Finsight</h1>
    </div>
    <div class="overlay-body">
      <h3>금융과 통찰력의 만남.</h3>
    </div>    
    <div class="overlay-sub">
      <h4>모두를 위한 공간에서 다양한 금융 상품에 대해 자유롭게 이야기하고, 서로의 경험과 지식을 나누세요.</h4>
    </div>
  </div>
  <!-- <h1>Board</h1> -->
  <div class="board">
    <v-window v-model="window_board" show-arrows>
      <v-window-item v-for="item in items_board" :key="item.id">
        <v-card height="200px" class="d-flex justify-center align-center">
          <div>
            <span class="text-h2">{{ item.title }}</span>
            <br><br>
            <p class="text-h5">{{ item.content }}</p>
          </div>
        </v-card>
      </v-window-item>
    </v-window>
  </div>
  <br>
  <!-- <h1>Product</h1> -->
  <div class="utility">
    <v-window v-model="window_product" show-arrows>
      <v-window-item v-for="item in items_product" :key="item.id">
        <v-card height="200px" class="d-flex justify-center align-center">
          <div>
            <span class="text-h2">{{ item.title }}</span>
            <br><br>
            <p class="text-h5">{{ item.content }}</p>
          </div>
        </v-card>
      </v-window-item>
    </v-window>
  </div>
  <br>
  <!-- <h1>Utility</h1> -->
  <div class="utility">
    <v-window v-model="window_utility" show-arrows>
      <v-window-item v-for="item in items_utility" :key="item.id">
        <v-card height="200px" class="d-flex justify-center align-center">
          <div>
            <span class="text-h2">{{ item.title }}</span>
            <br><br>
            <p class="text-h5">{{ item.content }}</p>
          </div>
        </v-card>
      </v-window-item>
    </v-window>
  </div>
  <br>
</template>

<script setup>
  import { ref } from 'vue'

  const window_board = ref(0)
  const items_board = ref([
    { id: 1, title: '컨설팅 게시판', content: '금융업 종사자들에게 질문하고 인증받은 사용들의 답변' },
    { id: 2, title: '자유 게시판', content: '자유로운 주제로 다양한 사람들과 소통' },
    { id: 3, title: '익명 게시판', content: '익명을 보장받고 편하게 소통' }
  ])
  
  const window_utility = ref(0)
  const items_utility = ref([
    { id: 1, title: '지도', content: '내 위치와 가까운 은행 찾기' },
    { id: 2, title: '환율', content: '다양한 국가의 환율 한눈에 검색' }
  ])

  const window_product = ref(0)
  const items_product = ref([
    { id: 1, title: '금융상품 정보', content: '시중 은행의 금융상품에 관한 정보' },
    { id: 2, title: '추천상품', content: '나에게 알맞는 금융상품 추천받기' }
  ])

</script>
<style scoped>
.background-image {
  background-image: url('@/assets/home.png');
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items_board: flex-start; /* 왼쪽 정렬을 위해 center 대신 flex-start 사용 */
  padding-left: 20%; /* 왼쪽 여백을 주어 중앙에서 살짝 왼쪽으로 */
  padding-bottom: 20%;
  text-align: left; /* 텍스트 왼쪽 정렬 */
  color: black
}

.overlay-head,
.overlay-body,
.overlay-sub {
  /* margin-left: auto; */
  margin-right: auto;
  max-width: 800px; /* 최대 너비 제한 */
}

.overlay-head h1,
.overlay-body h3,
.overlay-sub h4 {
  padding: 10px 20px;
}

.overlay-head{
  font-size: 60px;
  margin-top: 200px;
}
.overlay-body{
  font-size: 30px;
}
.overlay-sub{
  font-size: 25px;
}
/* text-h2 클래스에 대한 스타일 추가 */
.text-h2 {
  display: block; /* 블록 요소로 만들어주기 */
  text-align: center; /* 텍스트를 가운데 정렬 */
  width: 100%; /* 부모 요소의 전체 너비 차지 */
}

/* v-card 관련 스타일 */
.v-card {
  display: flex; /* Flexbox 컨테이너 설정 */
  flex-direction: column; /* 자식 요소들을 세로로 정렬 */
  justify-content: center; /* 세로축 가운데 정렬 */
  align-items: center; /* 가로축 가운데 정렬 */
  height: 200px; /* 카드의 높이 설정 */
}

</style>
