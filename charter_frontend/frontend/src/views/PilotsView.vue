<template>
  <div class="pilots">
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
        <div class="card-header"><h2>Charter Pilots</h2></div>
        <div class="card-body">
          <h5 class="card-title">Search for a pilot</h5>
          <div class="card-text">
            <!-- Create search bar for pilot id-->
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter pilot id"
                aria-label="Pilot's id"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Search
              </button>
            </div>
            <!-- Create update bar for pilot-->
            <h5 class="card-title">Update a pilot</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter pilot id"
                aria-label="Update Pilot"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Update
              </button>
            </div>
            <!-- Create delete bar for pilots-->
            <h5 class="card-title">Delete a pilot</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter pilot id"
                aria-label="Delete Pilot"
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
    <!-- Creating a button -->
    <h1>Pilot Info</h1>
    {{ msg }}
    <button @click="msg">Count</button>
  </div>
</template>

<script setup>

</script>
