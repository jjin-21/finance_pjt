<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title class="text-h5">게시글 수정</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="updateBoard">
              <v-row>
                <v-col>
                  <v-text-field
                    v-model.trim="title"
                    label="제목"
                    outlined
                    required
                    bg-color="grey-lighten-3"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-textarea
                    v-model.trim="content"
                    label="내용"
                    outlined
                    required
                    bg-color="grey-lighten-3"
                  ></v-textarea>
                </v-col>
              </v-row>
              <!-- <v-row>
                <v-col>
                  <input type="file" @change="onFileSelected">
                </v-col>
              </v-row>
              <v-row> -->
                <v-col>
                  <v-btn type="submit" color="primary">수정 완료</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const title = ref(null)
const content = ref(null)
const image = ref(null)
const store = useCounterStore()
const router = useRouter()
const route = useRoute()

onMounted(async () => {
  const boardId = route.params.id
  const response = await axios.get(`${store.API_URL}/boards/${boardId}/`, {
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data'
    }
  });
  
  title.value = response.data.title;
  content.value = response.data.content;
  console.log(title.value)
  console.log(content.value)
})

const updateBoard = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'DetailView', params: { id: route.params.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
/* Add custom styles if needed */
</style>
