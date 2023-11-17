<template>
  <v-app id="inspire">
    <v-app-bar flat>
      <v-container class="mx-auto d-flex align-center justify-center">
        <v-avatar
          class="me-4 "
          color="grey-darken-1"
          size="32"
        ></v-avatar>

        <v-btn
         :to="{name : 'HomeView'}"
        >Home</v-btn>

        <v-btn
         :to="{name : 'BoardView'}"
        >Board</v-btn>

        <v-btn
          :to="{name: 'KaKaoMapView'}"
        >Map</v-btn>

        <v-btn
          :to="{name: 'ExChangeView'}"
        >ExChange</v-btn>
        
        <v-btn
          :to="{name: 'ProductView'}"
        >Product</v-btn>
        

        <v-spacer></v-spacer>

        <v-btn @click="toggleTheme">toggle theme</v-btn>

        <v-btn
          v-show="store.isLogin"
          v-text="store.userName"
          :to="{name: 'UserProfileView'}"
        > </v-btn>

        <v-btn
          v-show="store.isLogin"
          :to="{name: 'LogOutView'}"
        >LogOut</v-btn>

        <v-btn
          v-show="!store.isLogin"
         :to="{name : 'LogInView'}"
        >LogIn</v-btn>

        <v-btn
          v-show="!store.isLogin"
         :to="{name : 'SignUpView'}"
        >SignUp</v-btn>

        <!-- <v-responsive max-width="160">
          <v-text-field
            density="compact"
            flat
            hide-details
            label="Search"
            rounded="lg"
            single-line
            variant="solo-filled"
          ></v-text-field>
        </v-responsive> -->
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-3" >
      <v-container fluid class="pa-0">
        <v-row no-gutters>
          <v-col cols="2">
            <v-sheet min-height="150vh" rounded="0">
              <!-- ... (좌측 컬럼 내용) ... -->
              
            </v-sheet>
          </v-col>

          <v-col cols="8">
            <v-sheet min-height="150vh" rounded="0">
              <router-view />
            </v-sheet>
          </v-col>

          <v-col cols="2">
            <v-sheet min-height="150vh" rounded="0">
              <!-- ... (우측 컬럼 내용) ... -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
      <v-footer app>
        <v-row justify="center" no-gutters>
          <v-btn
            v-for="link in links"
            :key="link"
            
            variant="text"
            class="mx-2"
            rounded="xl"
          >
            {{ link }}
          </v-btn>
          <v-col class="text-center mt-4" cols="12">
            {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
          </v-col>
        </v-row>
      </v-footer>

    </v-main>

    
  </v-app>
</template>

<script setup>
  import { useTheme } from 'vuetify'
  import { useCounterStore } from './stores/counter';
  import { onMounted } from 'vue';

  const links = [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ]


  // 다크모드 라이트모드 고정부분
  onMounted(() => {
    theme.global.name.value = store.themeColor
  })

  const theme = useTheme()
  const store = useCounterStore()

  function toggleTheme () {
    store.themeColor = theme.global.current.value.dark ? 'light' : 'dark'
    // console.log(store.themeColor)
    theme.global.name.value = store.themeColor
  }
</script>

