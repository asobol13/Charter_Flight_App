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

  <h1>This is the Pilots Page!</h1>

  <div>
    <VueyeTable :header-display="false" :data="pilots" :columns="columns" title="Pilots"></VueyeTable>
  </div>

</template>

<script>
// import employees from "@/data/employees.js";
// import Vueye from 'vueye-table'
export default {
  name: "PilotsPage",
  data: () => ({
      columns:[{
        key:"id",
        label: "ID",
        sortable: true,
        type: "number",
        display: true
      },
      {
        key: "pilot_name",
        label: "Pilot Name",
        sortable: true,
        display: true
      },
      {
        key: "pilot_charter",
        label: "Pilot Charter",
        sortable: true,
        display: true
      },
      { 
        key: "hourly_rate",
        label: "Pilot Hourly Rate",
        sortable: true,
        display: true
      }
    ]
  }),
  components:{
    VueyeTable
  }
};
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
