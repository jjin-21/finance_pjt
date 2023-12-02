<template>
  <div>

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';
import axios from 'axios'

const store = useCounterStore()


onMounted(() => {
  const userConfirmed = window.confirm('회원탈퇴하시겠습니까?');

    if (userConfirmed) {
        
        axios({
            method: 'delete',
            url: `${store.API_URL}/accounts/profile/${store.userId}`,
            // headers: {
            //   Authorization: `Token ${token.value}`
            // }
        })
            .then((res) => {
                window.alert('회원탈퇴가 완료 되었습니다.');
                console.log(res);
                store.logOut()
            })
            .catch((err) => {
                console.log(err);
            });
      } else {
         window.history.back()
        }
})
  
  

</script>

<style scoped>

</style>