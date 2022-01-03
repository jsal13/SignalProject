<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <DataChart />
      </div>
    </div>
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <DataTable />
      </div>
    </div>
  </div>
</template>

<script>
import DataTable from "./components/DataTable.vue";
import DataChart from "./components/DataChart.vue";

export default {
  name: "App",
  components: { DataTable, DataChart },
};
</script>

<style>
#app {
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
