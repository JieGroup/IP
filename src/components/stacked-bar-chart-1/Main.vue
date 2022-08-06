<template>
  <Chart
    type="bar"
    :width="width"
    :height="height"
    :data="data"
    :options="options"
  />
</template>

<script setup>
import { computed } from "vue";
import { helper as $h } from "@/utils/helper";

const props = defineProps({
  width: {
    type: [Number, String],
    default: "auto",
  },
  height: {
    type: [Number, String],
    default: "auto",
  },
});

const data = computed(() => {
  return {
    labels: [...Array(16).keys()],
    datasets: [
      {
        label: "Html Template",
        barPercentage: 0.5,
        barThickness: 6,
        maxBarThickness: 8,
        minBarLength: 2,
        backgroundColor: "#3160D8",
        data: $h.randomNumbers(-100, 100, 16),
      },
      {
        label: "VueJs Template",
        barPercentage: 0.5,
        barThickness: 6,
        maxBarThickness: 8,
        minBarLength: 2,
        backgroundColor: "#cbd5e0",
        data: $h.randomNumbers(-100, 100, 16),
      },
    ],
  };
});

const options = computed(() => {
  return {
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
    },
    scales: {
      x: {
        stacked: true,
        ticks: {
          font: {
            size: 12,
          },
          color: "#777777",
        },
        grid: {
          display: false,
          drawBorder: false,
        },
      },
      y: {
        stacked: true,
        ticks: {
          font: {
            size: 12,
          },
          color: "#777777",
          callback: function (value) {
            return "$" + value;
          },
        },
        grid: {
          color: "#D8D8D8",
          borderDash: [2, 2],
          drawBorder: false,
        },
      },
    },
  };
});
</script>
