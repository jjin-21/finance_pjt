<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title class="text-h5">게시글 작성</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="createBoard">
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
              <v-row>
                <v-col>
                  <v-btn type="submit" color="primary">작성 완료</v-btn>
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
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createBoard = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'BoardView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
/* Add custom styles if needed */
</style>
