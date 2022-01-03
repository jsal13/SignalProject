<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <DataTable />
      </div>
    </div>
  </div>
</template>

<script>
import DataTable from "./components/DataTable.vue";

export default {
  name: "App",
  components: { DataTable },
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
