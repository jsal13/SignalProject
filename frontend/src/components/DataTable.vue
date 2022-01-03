<template>
  <div class="data-table">
    <div class="card" style="width: 18rem;">
      <!-- <table class="table" id="datatable">
        <thead>
          <tr>
            <th>ID</th>
            <th>Product Title</th>
            <th>Product Price</th>
            <th>Created On</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.id">
            <td>{{item.datetime}}</td>
            <td>{{item.value}}</td>
          </tr>
        </tbody>
      </table>-->
      {{ data }}
      <div class="card-body">
        <h5 class="card-title">Data Table</h5>
      </div>
    </div>
  </div>
</template>


<script>
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import axios from "axios";
import $ from "jquery";

export default {
  name: "DataTable",
  mounted() {
    axios.get("http://127.0.0.1:8000/sesnors/1").then((response) => {
      this.data = response.data;
      $("#datatable").DataTable();
    });
  },
  data: function () {
    return {
      data: [],
    };
  },
};
</script>
