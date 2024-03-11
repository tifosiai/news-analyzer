
const getChartOptions = () => {
  return {
    series: [35.1, 23.5, 2.4, 4, 1.4],
    colors: ["#1C64F2", "#16BDCA", "#FDBA8C", "#E74694", "#C42415"],
    chart: {
      height: 320,
      width: "100%",
      type: "donut",
    },
    title: {
      text: "Category Confidence", // Title text
      align: 'center', // Can be left, center, or right
      margin: 10,
      style: {
        fontSize: '15px',
        fontFamily: 'Inter, sans-serif',
      }
    },
    stroke: {
      colors: ["transparent"],
      lineCap: "",
    },
    plotOptions: {
      pie: {
        donut: {
          labels: {
            show: true,
            name: {
              show: true,
              fontFamily: "Inter, sans-serif",
              offsetY: 20,
            },
            total: {
              showAlways: true,
              show: true,
              label: "Unique visitors",
              fontFamily: "Inter, sans-serif",
              formatter: function (w) {
                const sum = w.globals.seriesTotals.reduce((a, b) => {
                  return a + b
                }, 0)
                return sum + '%'
              },
            },
            value: {
              show: true,
              fontFamily: "Inter, sans-serif",
              offsetY: -20,
              formatter: function (value) {
                return value + "%"
              },
            },
          },
          size: "70%",
        },
      },
    },
    grid: {
      padding: {
        top: -2,
      },
    },
    labels: ["Cat1", "Cat2", "Cat3", "Cat4", "Cat5"],
    dataLabels: {
      enabled: false,
    },
    legend: {
      position: "bottom",
      fontFamily: "Inter, sans-serif",
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
    },
    xaxis: {
      labels: {
        formatter: function (value) {
          return value  + "%"
        },
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
  }
}

if (document.getElementById("donut-chart") && typeof ApexCharts !== 'undefined') {
  const chart = new ApexCharts(document.getElementById("donut-chart"), getChartOptions());
  chart.render();

  // Get all the checkboxes by their class name
  const checkboxes = document.querySelectorAll('#devices input[type="checkbox"]');

  // Function to handle the checkbox change event
  function handleCheckboxChange(event, chart) {
      const checkbox = event.target;
      if (checkbox.checked) {
          switch(checkbox.value) {
            case 'desktop':
              chart.updateSeries([15.1, 22.5, 4.4, 8.4]);
              break;
            case 'tablet':
              chart.updateSeries([25.1, 26.5, 1.4, 3.4]);
              break;
            case 'mobile':
              chart.updateSeries([45.1, 27.5, 8.4, 2.4]);
              break;
            default:
              chart.updateSeries([55.1, 28.5, 1.4, 5.4]);
          }

      } else {
          chart.updateSeries([35.1, 23.5, 2.4, 5.4]);
      }
  }

  // Attach the event listener to each checkbox
  checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', (event) => handleCheckboxChange(event, chart));
  });
}


const getChartOptions1 = () => {
  return {
    series: [52.8, 26.8+20.4],
    colors: ["#1C64F2", "#16BDCA"],
    chart: {
      height: 420,
      width: "100%",
      type: "pie",
    },
    title: {
      text: "Sentiment Confidence", // Title text
      align: 'center', // Can be left, center, or right
      margin: 10,
      style: {
        fontSize: '15px',
        fontFamily: 'Inter, sans-serif',
      }
    },
    stroke: {
      colors: ["white"],
      lineCap: "",
    },
    plotOptions: {
      pie: {
        labels: {
          show: true,
        },
        size: "100%",
        dataLabels: {
          offset: -25
        }
      },
    },
    labels: ["Positive", "Negative"],
    dataLabels: {
      enabled: true,
      style: {
        fontFamily: "Inter, sans-serif",
      },
    },
    legend: {
      position: "bottom",
      fontFamily: "Inter, sans-serif",
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
    },
    xaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
  }
}

if (document.getElementById("pie-chart-1") && typeof ApexCharts !== 'undefined') {
  const chart1 = new ApexCharts(document.getElementById("pie-chart-1"), getChartOptions1());
  chart1.render();
}



const getChartOptions2 = () => {
  return {
    series: [52.8, 26.8+20.4],
    colors: ["#1C64F2", "#16BDCA", "#9061F9"],
    chart: {
      height: 420,
      width: "100%",
      type: "pie",
    },
    title: {
      text: "Lexicon Distribution", // Title text
      align: 'center', // Can be left, center, or right
      margin: 10,
      style: {
        fontSize: '15px',
        fontFamily: 'Inter, sans-serif',
      },
    },
    stroke: {
      colors: ["white"],
      lineCap: "",
    },
    plotOptions: {
      pie: {
        labels: {
          show: true,
        },
        size: "100%",
        dataLabels: {
          offset: -25
        }
      },
    },
    labels: ["Positive", "Negative"],
    dataLabels: {
      enabled: true,
      style: {
        fontFamily: "Inter, sans-serif",
      },
    },
    legend: {
      position: "bottom",
      fontFamily: "Inter, sans-serif",
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
    },
    xaxis: {
      labels: {
        formatter: function (value) {
          return value + "%"
        },
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
  }
}

if (document.getElementById("pie-chart-2") && typeof ApexCharts !== 'undefined') {
  const chart2 = new ApexCharts(document.getElementById("pie-chart-2"), getChartOptions2());
  chart2.render();
}



const options = {
  colors: ["#1A56DB", "#FDBA8C"],
  title: {
    text: "5 Most Frequent Words", // Title text
    align: 'center', // Can be left, center, or right
    margin: 10,
    style: {
      fontSize: '15px',
      fontFamily: 'Inter, sans-serif',
    },
  },
  series: [
    {
      name: "Positive",
      color: "#00FF00",
      data: [
        { x: "Word 1", y: 231 },
        { x: "Word 2", y: 122 },
        { x: "Word 3", y: 63 },
        { x: "Word 4", y: 421 },
        { x: "Word 5", y: 122 },
        { x: "Word 6", y: 231 },
        { x: "Word 7", y: 122 },
        { x: "Word 8", y: 63 },
        { x: "Word 9", y: 421 },
        { x: "Word 10", y: 122 },
      ],
    },
  ],
  chart: {
    type: "bar",
    height: "320px",
    fontFamily: "Inter, sans-serif",
    toolbar: {
      show: false,
    },
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: "70%",
      borderRadiusApplication: "end",
      borderRadius: 8,
    },
  },
  tooltip: {
    shared: true,
    intersect: false,
    style: {
      fontFamily: "Inter, sans-serif",
    },
  },
  states: {
    hover: {
      filter: {
        type: "darken",
        value: 1,
      },
    },
  },
  stroke: {
    show: true,
    width: 0,
    colors: ["transparent"],
  },
  grid: {
    show: false,
    strokeDashArray: 4,
    padding: {
      left: 2,
      right: 2,
      top: -14
    },
  },
  dataLabels: {
    enabled: false,
  },
  legend: {
    show: false,
  },
  xaxis: {
    floating: false,
    labels: {
      show: true,
      style: {
        fontFamily: "Inter, sans-serif",
        cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
      }
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    show: false,
  },
  fill: {
    opacity: 1,
  },
}

if (document.getElementById("column-chart") && typeof ApexCharts !== 'undefined') {
  const chart = new ApexCharts(document.getElementById("column-chart"), options);
  chart.render();
}
