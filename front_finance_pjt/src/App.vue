<template>
  <v-app id="inspire">
    <v-app-bar flat>
      <v-container class="mx-auto d-flex align-center justify-center">
        
        <v-img
          src="@/assets/finsight.png"
          alt="Logo"
          contain
          class="me-4"
          max-width="80"
          max-height="80"
          @click.prevent="goHome"
          style="cursor: pointer;"
        ></v-img>
              

        <v-btn @click="toggleDropdown1">Board</v-btn>

        <v-dialog v-model="dropdown1" max-width="500">
          <v-card>
            <v-list>
              <v-list-item @click="navigateTo('BoardView')">
                <v-list-item-title>Board</v-list-item-title>
              </v-list-item>
              <v-list-item @click="navigateTo('AnonymousBoardView')">
                <v-list-item-title>Anonymous</v-list-item-title>
              </v-list-item>
              <v-list-item @click="navigateTo('ConsultingBoardView')">
                <v-list-item-title>QnA</v-list-item-title>
              </v-list-item>
              <!-- Add more items as needed -->
            </v-list>
          </v-card>
        </v-dialog>


        <v-btn @click="toggleDropdown2">UTILITY</v-btn>

        <v-dialog v-model="dropdown2" max-width="500">
          <v-card>
            <v-list>
              <v-list-item @click="navigateTo('KaKaoMapView')">
                <v-list-item-title>Map</v-list-item-title>
              </v-list-item>
              <v-list-item @click="navigateTo('ExChangeView')">
                <v-list-item-title>ExChange</v-list-item-title>
              </v-list-item>
              <!-- Add more items as needed -->
            </v-list>
          </v-card>
        </v-dialog>
        
        <v-btn @click="toggleDropdown3">PRODUCT</v-btn>
        
        <v-dialog v-model="dropdown3" max-width="500">
          <v-card>
            <v-list>
              <v-list-item @click="navigateTo('ProductView')">
                <v-list-item-title>Finance Product</v-list-item-title>
              </v-list-item>
              <v-list-item @click="navigateTo('NewsView')">
                <v-list-item-title>Finance News</v-list-item-title>
              </v-list-item>
              <!-- Add more items as needed -->
            </v-list>
          </v-card>
        </v-dialog>

        

        <v-spacer></v-spacer>

        <v-btn @click="toggleTheme">{{ store.themeColor }} Mode</v-btn>

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

    <v-main >
      <v-container fluid class="pa-0">
        <v-row no-gutters>
          <v-col cols="2">
            <v-sheet min-height="200vh"  rounded="0">
              <!-- ... (좌측 컬럼 내용) ... -->
              
            </v-sheet>
          </v-col>

          <v-col  cols="8">
            <v-sheet min-height="200vh" rounded="0">
              <router-view />
            </v-sheet>
          </v-col>

          <v-col cols="2">
            <v-sheet min-height="200vh" rounded="0">
              <!-- ... (우측 컬럼 내용) ... -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
      <v-footer :color="store.themeColor === 'dark' ? 'grey-darken-3' : 'grey-lighten-4'">
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
  import { onMounted, ref } from 'vue';
  import { useRouter } from 'vue-router';

  const router = useRouter()
  const dropdown1 = ref(false);
  const dropdown2 = ref(false);
  const dropdown3 = ref(false);

  const goHome = function () {
    router.push({name: 'HomeView'})
  }

  const navigateTo = function (routeName) {
    router.push({ name: routeName });
    dropdown1.value = false
    dropdown2.value = false
    dropdown3.value = false
  };

  const toggleDropdown1 = function () {
    dropdown1.value = !dropdown1.value;
  };
  const toggleDropdown2 = function () {
    dropdown2.value = !dropdown2.value;
  };
  const toggleDropdown3 = function () {
    dropdown3.value = !dropdown3.value;
  };


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

