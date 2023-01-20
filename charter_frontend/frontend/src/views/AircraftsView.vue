<template>
  <div class="aircrafts">
    <div class="container">
      <!-- bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.
      jsdelivr.net/npm/bootswatch@4.5.2/dist/simplex/bootstrap.min.css"
        integrity="sha384-FYrl2Nk72fpV6+l3Bymt1zZhnQFK75ipDqPXK0sOR
      0f/zeOSZ45/tKlsKucQyjSp"
        crossorigin="anonymous"
      />
      <!-- This is a container for text -->
      <div class="card bg-light mb-3 mx-auto" style="max-width: 30rem">
        <div class="card-header"><h2>Charter Aircrafts</h2></div>
        <div class="card-body">
          <h5 class="card-title">Search for an aircraft</h5>
          <div class="card-text">
            <!-- Create search bar for tailnumber-->
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter aircraft tail number"
                aria-label="Aircraft's tail number"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Search
              </button>
            </div>
            <!-- Create update bar for aircraft-->
            <h5 class="card-title">Update an aircraft</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter aircraft tail number"
                aria-label="Update Aircraft"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Update
              </button>
            </div>
            <!-- Create delete bar for aircraft-->
            <h5 class="card-title">Delete an aircraft</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter aircraft tail number"
                aria-label="Delete Aircraft"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Delete
              </button>
            </div>
            <!-- Create button-->
            <button class="btn btn-primary" type="button">Create New</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Creating a table -->
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Tailnumber</th>
          <th scope="col">Aircraft Name</th>
          <th scope="col">Capacity</th>
          <th scope="col">Hourly Rate</th>
          <th scope="col">Wait Time Rate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in post" :key="p.tail_number">
          <th scope="row">{{ p.tail_number }}</th>
          <td>{{ p.aircraft_name }}</td>
          <td>{{ p.capacity }}</td>
          <td>{{ p.hourly_rate }}</td>
          <td>{{ p.wait_time_rate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: [],
    };
  },

  methods: {
    getInfo() {
      fetch("http://localhost:5000/aircrafts")
        .then((response) => response.json())
        .then((data) => (this.post = data));
    },
  },
  mounted() {
    this.getInfo();
  },
};
</script>
