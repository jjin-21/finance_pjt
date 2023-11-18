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
          // 사용자가 "아니오"를 선택한 경우 또는 창을 닫은 경우
          // 추가적인 처리가 필요한 경우 여기에 코드를 추가
        }
})
  
  

</script>

<style scoped>

</style>