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
import { useDarkModeStore } from "@/stores/dark-mode";
import { useColorSchemeStore } from "@/stores/color-scheme";
import { colors } from "@/utils/colors";

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

const darkMode = computed(() => useDarkModeStore().darkMode);
const colorScheme = computed(() => useColorSchemeStore().colorScheme);

const data = computed(() => {
  return {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    datasets: [
      {
        label: "Html Template",
        barThickness: 8,
        maxBarThickness: 6,
        data: [60, 150, 30, 200, 180, 50, 180, 120, 230, 180, 250, 270],
        backgroundColor: colorScheme.value ? colors.primary() : "",
      },
      {
        label: "VueJs Template",
        barThickness: 8,
        maxBarThickness: 6,
        data: [50, 135, 40, 180, 190, 60, 150, 90, 250, 170, 240, 250],
        backgroundColor: darkMode.value
          ? colors.darkmode["400"]()
          : colors.slate["300"](),
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
        ticks: {
          font: {
            size: 11,
          },
          color: colors.slate["500"](0.8),
        },
        grid: {
          display: false,
          drawBorder: false,
        },
      },
      y: {
        ticks: {
          display: false,
        },
        grid: {
          color: darkMode.value
            ? colors.darkmode["300"](0.8)
            : colors.slate["300"](),
          borderDash: [2, 2],
          drawBorder: false,
        },
      },
    },
  };
});
</script>
