<template>
  <div>
    {{ dProduct.kor_co_nm }}
    {{ dProduct.fin_prdt_nm }}
    {{ dProduct.deposit_options }}
    <hr>
  </div>
</template>

<script setup>
defineProps ({
  dProduct: Object
})

</script>

<style scoped>

</style>