<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="dark" v-if="notIsLoginPage">
      <b-navbar-brand>Travel App</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/list">List</b-nav-item>
          <b-nav-item to="/form">Form</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <template #button-content>
              <i class="fas fa-user"></i>
            </template>
            <b-dropdown-item @click="goToLogin">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
      </b-navbar-nav> 
    </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default{
    computed:{
      notIsLoginPage(){
        return this.$route.name !== "login" && this.$route.name !== 'register';
      }
    }, 

    methods: {
      goToLogin(){
        this.$router.push({name: 'login'})
        localStorage.removeItem('token');
      }
    }
}

</script>

<style>
</style>