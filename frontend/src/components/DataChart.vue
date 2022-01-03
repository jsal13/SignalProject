<template>
  <div class="data-chart">
    <canvas id="signal-chart"></canvas>
  </div>
</template>

<script>
import axios from "axios";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default {
  name: "DataChart",
  methods: {
    CreateChartDataset(label, data) {
      return {
        label: label,
        data: data,
        fill: false,
      };
    },

    GetUpdatedData() {
      console.log("Updating data...");
      axios.get("http://localhost:8000/sensors/1").then((response) => {
        var data = Object.freeze(response.data["data"]);
        var signal1Data = data
          .filter((obj) => obj.sensor == 1)
          .map((obj) => obj.value);
        var chartLabels = data
          .filter((obj) => obj.sensor == 1)
          .map((obj) => obj.id);

        var chartDatasets = [
          this.CreateChartDataset("Signal 1 Data", signal1Data),
        ];

        var chartData = {
          type: "line",
          data: {
            labels: chartLabels,
            datasets: chartDatasets,
          },
        };

        const ctx = document.getElementById("signal-chart");

        if (this.myChart !== undefined) {
          this.myChart.destroy();
        }
        this.myChart = new Chart(ctx, chartData);
      });
    },
  },
  mounted() {
    setInterval(this.GetUpdatedData, 10000);
  },
  data: function () {
    return {
      myChart: undefined,
    };
  },
};
</script>
