<template>
  <v-container>
    <v-row>
      <v-col >
        <v-btn variant="outlined" class=" my-3" @click.prevent="showMyProfile"><h3>내 프로필 보기</h3></v-btn>

        
        <!-- Profile Data Section -->
        <v-dialog v-model="showUserProfileDialog" max-width="600">
          <v-card>
            <v-card-title>User Profile</v-card-title>
            <v-card-text>
              <!-- Display user profile data here -->
              <v-list>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Username: {{ profileData.username }}</v-list-item-title>
                    <v-list-item-title>닉네임: {{ profileData.nickname }}</v-list-item-title>
                    <v-list-item-title>E-mail: {{ profileData.email }}</v-list-item-title>
                    <v-list-item-title>전화번호: {{ profileData.phone_num }}</v-list-item-title>
                    <v-list-item-title>성별: {{ genderType }}</v-list-item-title>
                    <v-list-item-title>회사: {{ profileData.company }}</v-list-item-title>
                    <v-list-item-title>자산: {{ profileData.asset }}</v-list-item-title>
                    <v-list-item-title>연봉: {{ profileData.salary }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="showUserProfileDialog = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <hr>

        <!-- Profile Actions Section -->
        <v-row class="my-1">
          <v-col>
            <v-btn class="mr-2" variant="outlined" :to="({ name: 'UserProfileProductView', params: { id: store.userId } })">
              <h3>내가 담은 상품</h3>
            </v-btn>
            <v-btn variant="outlined" :to="({ name: 'ProductRecommendView', params: { id: store.userId } })">
              <h3>상품 추천 받기</h3>
            </v-btn>
          </v-col>
          <v-col>
            <v-btn variant="outlined" class="mx-1" @click.prevent="changePassword"><h3>비밀번호 변경</h3></v-btn>
            <v-btn variant="outlined" class="mx-1" @click.prevent="editProfile"><h3>회원정보수정</h3></v-btn>
            <v-btn variant="outlined" class="mx-1" @click.prevent="deleteProfile"><h3>회원탈퇴</h3></v-btn>
          </v-col>
        </v-row>
        <hr>

        <!-- User Posts Section -->
        <v-row>
          <v-col>
            <h3>내가 작성한 글</h3>
            <v-list>
              <v-list-item v-for="post in paginatedUserPosts" :key="post.id">
                <v-list-item-content>
                  <router-link :to="{ name: 'DetailView', params: { id: post.id } }">
                    {{ post.title }}
                  </router-link>
                  <p class="post-timestamp">{{ formatDateTime(post.created_at) }}</p>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-pagination
              v-if="userPosts.length > pageSize"
              v-model="userPostsPage"
              :length="Math.ceil(userPosts.length / pageSize)"
            ></v-pagination>
          </v-col>
        </v-row>
        <hr>

        <!-- User Comments Section -->
        <v-row>
          <v-col>
            <h3>내가 작성한 댓글</h3>
            <v-list>
              <v-list-item v-for="comment in paginatedUserComments" :key="comment.id">
                <v-list-item-content>
                  <router-link :to="{ name: 'DetailView', params: { id: comment.board.id } }">
                    {{ comment.content }}
                  </router-link>
                  <p class="post-timestamp">{{ formatDateTime(comment.created_at) }}</p>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-pagination
              v-if="userComments.length > pageSize"
              v-model="userCommentsPage"
              :length="Math.ceil(userComments.length / pageSize)"
            ></v-pagination>
          </v-col>
        </v-row>
        <hr>

        
        <br>
        <br>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const profileData = ref([])
const userPosts = ref([])
const userComments = ref([])
const userPostsPage = ref(1);
const userCommentsPage = ref(1);
const pageSize = 5;

const showUserProfileDialog = ref(false);

onMounted(() => {
  // Fetch user profile data
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/${store.userId}`
  })
    .then((res) => {
      profileData.value = res.data
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })

  // Fetch all posts
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/`
  })
    .then((res) => {
      // Filter and reverse the posts authored by the user
      userPosts.value = res.data.filter(post => post.user === store.userId).reverse()
    })
    .catch((err) => {
      console.log(err)
    })

  // Fetch all comments
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/comments/`
  })
    .then((res) => {
      console.log(res.data)
      // Filter and reverse the comments authored by the user
      userComments.value = res.data.filter(comment => comment.user === store.userId).reverse()
    })
    .catch((err) => {
      console.log(err)
    })
})

const genderType = computed(() => {
  if (profileData.value && profileData.value.gender === 0) {
    return 'Male';
  } else if (profileData.value && profileData.value.gender === 1) {
    return 'Female';
  }
})

// const 

const editProfile = function () {
  router.push({
    name: 'UserProfileEditView',
    params: {
      id: store.userId
    }
  })
}

const deleteProfile = function () {
  router.push({
    name: 'UserProfileDeleteView',
    params: {
      id: store.userId
    }
  })
}

const changePassword = function () {
  router.push({
    name: 'UserProfileChangePasswordView',
    params: {
      id: store.userId
    }
  })
}

const showMyProfile = function () {
  showUserProfileDialog.value = true
}


const paginatedUserPosts = computed(() => {
  const start = (userPostsPage.value - 1) * pageSize;
  const end = start + pageSize;
  return userPosts.value.slice(start, end);
});

const paginatedUserComments = computed(() => {
  const start = (userCommentsPage.value - 1) * pageSize;
  const end = start + pageSize;
  return userComments.value.slice(start, end);
});

const formatDateTime = (dateTimeString) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
  return new Date(dateTimeString).toLocaleString('en-US', options).replace(/(\d+)\/(\d+)\/(\d+), (\d+:\d+:\d+)/, '$3-$1-$2 $4');
}

</script>

<style scoped>
.post-timestamp {
  font-size: 12px; /* Adjust the font size as needed */
  color: gray; /* Optionally adjust the color */
}
</style>
