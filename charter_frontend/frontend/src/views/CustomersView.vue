<template>
  <div class="customers">
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
        <div class="card-header"><h2>Charter Customers</h2></div>
        <div class="card-body">
          <h5 class="card-title">Search for a customer</h5>
          <div class="card-text">
            <!-- Create search bar for customers-->
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter customer id"
                aria-label="Customers id"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Search
              </button>
            </div>
            <!-- Create update bar for customers-->
            <h5 class="card-title">Update a customer</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter customer id"
                aria-label="Update Customer"
                aria-describedby="button-addon2"
              />
              <button class="btn btn-primary" type="button" id="button-addon2">
                Update
              </button>
            </div>
            <!-- Create delete bar for customers-->
            <h5 class="card-title">Delete a customer</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Enter customer id"
                aria-label="Delete Customer"
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
          <th scope="col">Account Number</th>
          <th scope="col">Name</th>
          <th scope="col">Signed Agreement</th>
          <th scope="col">Username</th>
          <th scope="col">Password</th>
          <th scope="col">Phonenumber</th>
          <th scope="col">Email</th>
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
        </tr>
        <tr>
          <th scope="row">Info</th>
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
        </tr>
        <tr>
          <th scope="row">Info</th>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
          <td>Info</td>
        </tr>
      </tbody>
    </table>
    <div v-for="p in post" :key="p.account_number">
      <h2>{{ p.account_number }} - {{ p.name }}</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CustomersView",
  data() {
    return {
      post: [],
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/customers";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.post = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
