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

    <v-main class="bg-grey-lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
             
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="80vh"
              rounded="lg"
            >
              <router-view />
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  const links = [
    'Dashboard',
    'Messages',
    'Profile',
    'Updates',
  ]

  import { useTheme } from 'vuetify'

  const theme = useTheme()

  function toggleTheme () {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
  }
</script>

<script>
  export default {
    data: () => ({
      links: [
        'HomeView',
        'Messages',
        'Profile',
        'Updates',
      ],
    }),
  }
</script>