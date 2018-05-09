const chartSeriesColors = {
  'primary': '#FF3860',
  'secondary': '#363636',
  'tertiary': '#3273DC',
  'fourth': '#00D1B2',
  'fifth': '#23D160',
  'sixth': '#FFDD57',
  'seventh': '#209CEE',
  'eight': '#7A7A7A',
  'ninth': '#363636',
  'last': '#DBDBDB'
}
const chartTextStyle = {
  color: '#FAFAFA'
}

// bar & line
const baseBarLineChart = {
  title: {
    text: '',
    textStyle: chartTextStyle
  },
  grid: {
    containLabel: true
  },
  legend: {
    data: [],
    bottom: '20px',
    textStyle: chartTextStyle
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      crossStyle: {
        color: '#999'
      }
    }
  },
  xAxis: [],
  yAxis: [],
  series: [],
  animationDuration: 1000,
  color: [],
  textStyle: chartTextStyle
}

// simple bar
const baseBarChart = {
  title: {
    text: '',
    textStyle: chartTextStyle
  },
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c}'
  },
  xAxis: {
    type: 'category',
    axisLabel: {
      interval: 0
    },
    data: []
  },
  yAxis: {
    type: 'value'
  },
  series: [],
  color: [],
  textStyle: chartTextStyle
}

// doughnut
const baseDoughnutChart = {
  title: {
    text: '',
    textStyle: chartTextStyle
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b}: {c} ({d}%)'
  },
  legend: {
    orient: 'vertical',
    x: 'left',
    data: [],
    textStyle: chartTextStyle
  },
  series: [
    {
      name: '',
      type: 'pie',
      radius: ['50%', '70%'],
      avoidLabelOverlap: false,
      label: {
        normal: {
          show: false,
          position: 'center'
        },
        emphasis: {
          show: true,
          textStyle: {
            fontSize: '30',
            fontWeight: 'bold'
          }
        }
      },
      labelLine: {
        normal: {
          show: false
        }
      },
      data: []
    }
  ],
  color: []
  // textStyle: chartTextStyle
}

export { chartSeriesColors, chartTextStyle, baseBarLineChart, baseBarChart, baseDoughnutChart }
