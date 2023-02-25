<template>
    <header class="nav-bar">
      <div class="menu-item">
          <a href="HomePage.vue">Home</a>
      </div>
      <div class="menu-item">
          <a href="CustomersPage.vue">Customers</a>
      </div>
      <div class="menu-item">
          <a href="ChartersPage.vue">Charters</a>
      </div>
      <div class = "menu-item">
          <a href="PilotsPage.vue">Pilots</a>
      </div>
      <div class="menu-item">
          <a href="AircraftsPage.vue">Aircrafts</a>
      </div>
  </header>

  <h1>This is the Customers Page!</h1>
  <div v-for="p in post" :key="p.id">
      <h2>{{ p.id }} - {{ p.title }}</h2>
      <p>{{ p.body }}</p>
  </div>
</template>

<script>
// import axios from 'axios';

// export default {
//   data() {
//     return {
//       customers: []
//     };
//   },
//   methods: {
//     getCustomers() {
//       const path = 'https://jsonplaceholder.typicode.com/todos/1';
//     axios.get(path)
//     .then((res) => {
//       this.customers = res.data.customers;
//     })
//     .catch((error) => {
//       //eslint-disable-next-line
//       console.error(error);
//     });
//     },
//   },
//   created(){
//     this.getCustomers();
//   },
// };

export default {
  data() {
    return {
      post: []
    }
  },
  methods: {
    getPosts() {
      fetch('https://jsonplaceholder.typicode.com/posts/')
        .then(response => response.json())
        .then(data => this.post = data)
    }
  },
  mounted() {
    this.getPosts()
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

/* Nav bar style */
.nav-bar {
  position: fixed;
  width: 100%;
  top: 0px;
  margin-left: -8px;
  background-color: #333;
}
.menu-item {
  float: left;
}

.menu-item a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
.menu-item a:hover {
  background-color: #1434A4;
}
.active {
  background-color: gray;
}
</style>
