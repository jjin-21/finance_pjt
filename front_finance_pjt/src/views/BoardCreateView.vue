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
                  <input type="file" @change="onFileSelected">
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
const image = ref(null)
const store = useCounterStore()
const router = useRouter()

const onFileSelected = event => {
  image.value = event.target.files[0]
}


const createBoard = function () {
  const formData = new FormData() // FormData 인스턴스 생성
  formData.append('title', title.value)
  formData.append('content', content.value)
  if (image.value) {
    formData.append('image', image.value) // 이미지 파일 추가
    console.log("IMAGE :", image)
  }

  axios({
    method: 'post',
    url: `${store.API_URL}/boards/`,
    data: formData,
    // {
    //   title: title.value,
    //   content: content.value
    // },
    headers: {
      Authorization: `Token ${store.token}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then((res) => {
      // console.log(res)
      const newBoardId = res.data.id
      router.push({ name: 'DetailView', params: { id: newBoardId } })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
/* Add custom styles if needed */
</style>
