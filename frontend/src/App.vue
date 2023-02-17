<template>
    <header class="nav-bar">
      <div class="menu-item">
          <a href="HomePage.vue">Customers</a>
      </div>
      <div class="menu-item">
          <a href="customers.html">Customers</a>
      </div>
      <div class="menu-item">
          <a href="charters.html">Charters</a>
      </div>
      <div class = "menu-item">
          <a href="pilots.html">Pilots</a>
      </div>
      <div class="menu-item">
          <a href="aircrafts.html">Aircrafts</a>
      </div>
  </header>
  <img alt="Vue logo" src="./assets/logo.png">
  <HomePage msg="Welcome to MyFlight!"/>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
