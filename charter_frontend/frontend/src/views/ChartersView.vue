<template>
  <div class="charters">
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
        <div class="card-header"><h2>Charters</h2></div>
        <div class="card-body">
          <h5 class="card-title">Search for a charter</h5>
          <div class="card-text">
            <!-- Create search bar for charters-->
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter charter number"
                aria-label="Charter number"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Search
              </button>
            </div>
            <!-- Create update bar for charters-->
            <h5 class="card-title">Update a charter</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter charter number"
                aria-label="Update Charter"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Update
              </button>
            </div>
            <!-- Create delete bar for charters-->
            <h5 class="card-title">Delete a charter</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter charter number"
                aria-label="Delete Charter"
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
    <table class="table table-bordered">
      <thead>
        <tr>
          <th scope="col">Charter Number</th>
          <th scope="col">Departure Airport</th>
          <th scope="col">Destination Airport</th>
          <th scope="col">Departure Date</th>
          <th scope="col">Return Date</th>
          <th scope="col">Departure Time</th>
          <th scope="col">Return Time</th>
          <th scope="col">Wait Hours</th>
          <th scope="col">Flight Hours</th>
          <th scope="col">Number Pax</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Info</th>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
        </tr>
        <tr>
          <th scope="row">Info</th>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
        </tr>
        <tr>
          <th scope="row">Info</th>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
        </tr>
        <tr>
          <th scope="row">Info</th>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
