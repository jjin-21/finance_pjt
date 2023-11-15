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
         :to="{name : 'ArticleView'}"
        >Article</v-btn>

        <v-btn
         :to="{name : 'SignUpView'}"
        >SignUp</v-btn>

        <v-spacer></v-spacer>

        <v-btn @click="toggleTheme">toggle theme</v-btn>

        <v-responsive max-width="160">
          <v-text-field
            density="compact"
            flat
            hide-details
            label="Search"
            rounded="lg"
            single-line
            variant="solo-filled"
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-3" p-0>
      <v-container fluid>
        <v-row no-gutters>
          <v-col cols="2">
            <v-sheet min-height="150vh" rounded="sm">
              <!-- ... (좌측 컬럼 내용) ... -->
              
            </v-sheet>
          </v-col>

          <v-col cols="8">
            <v-sheet min-height="150vh" rounded="sm">
              <router-view />
            </v-sheet>
          </v-col>

          <v-col cols="2">
            <v-sheet min-height="150vh" rounded="sm">
              <!-- ... (우측 컬럼 내용) ... -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import { useTheme } from 'vuetify'

  const theme = useTheme()

  function toggleTheme () {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
  }
</script>

