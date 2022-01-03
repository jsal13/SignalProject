<template>
  <div class="data-table">
    <table class="table" id="datatable">
      <thead>
        <tr>
          <th>id</th>
          <th>Datetime</th>
          <th>Sensor</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in data" :key="row.id">
          <td>{{row.id}}</td>
          <td>{{row.datetime}}</td>
          <td>{{row.sensor}}</td>
          <td>{{row.value}}</td>
        </tr>
      </tbody>
    </table>
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
    axios.get("http://localhost:8000/sensors/1").then((response) => {
      this.data = response.data["data"];
      $("#datatable").DataTable();
    });
  },
  data: function () {
    return {
      data: {},
    };
  },
};
</script>
