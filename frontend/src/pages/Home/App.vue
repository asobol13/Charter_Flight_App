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

  <h1>
    ~Here are the annoucements and events for the day!
      <!--<a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.-->
  </h1>
  <!-- Calendar container -->
  <div class="container" id="calendar">
    <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%239E69AF&ctz=America%2FLos_Angeles&showCalendars=1&showTabs=1&showPrint=1&showNav=1&showTitle=0&mode=WEEK&src=ZTAyNDJjOTJlMTcxNTJiYmUwNWI4NTIyNTFkODJkMmU1MGY4N2YxOWY0ZDA1MjAwMDBlOTMyNmJkYzAwZjcxZEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%237CB342&color=%230B8043" style="border:solid 1px #777" width="1000" height="600" frameborder="0" scrolling="no"></iframe>
  </div>
</template>

<script>

export default {
  name: 'HomePage'
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
