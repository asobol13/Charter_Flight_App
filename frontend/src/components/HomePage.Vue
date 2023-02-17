<template>
    <div class="hello">
      <h1>{{ msg }}</h1>
      <p>
        ~Here are the annoucements and events for the day!
        <!--<a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.-->
      </p>
    </div>
    <!-- Calendar container -->
    <div class="container" id="calendar">
        <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%239E69AF&ctz=America%2FLos_Angeles&showCalendars=1&showTabs=1&showPrint=1&showNav=1&showTitle=0&mode=WEEK&src=ZTAyNDJjOTJlMTcxNTJiYmUwNWI4NTIyNTFkODJkMmU1MGY4N2YxOWY0ZDA1MjAwMDBlOTMyNmJkYzAwZjcxZEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%237CB342&color=%230B8043" style="border:solid 1px #777" width="1000" height="600" frameborder="0" scrolling="no"></iframe>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #6377dd;
  }
  </style>