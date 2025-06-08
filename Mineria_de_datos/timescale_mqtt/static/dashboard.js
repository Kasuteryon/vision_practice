const socket = io();

const charts = {
  realtime: createChart('realtimeChart', 'line'),
  history: createChart('historyChart', 'line'),
  scatter: createScatterChart('scatterChart')
};

function createChart(canvasId, type) {
  return new Chart(document.getElementById(canvasId), {
    type: type,
    data: {
      labels: [],
      datasets: [
        {
          label: 'Temperature (°C)',
          data: [],
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.3)',
          showLine: type !== 'scatter'
        },
        {
          label: 'Humidity (%)',
          data: [],
          borderColor: 'rgb(54, 162, 235)',
          backgroundColor: 'rgba(54, 162, 235, 0.3)',
          showLine: type !== 'scatter'
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: 'Time' }, type: 'category' },
        y: { beginAtZero: true, title: { display: true, text: 'Value' } }
      }
    }
  });
}

function createScatterChart(id) {
  const colors = ['#ff6384', '#36a2eb', '#cc65fe'];
  return new Chart(document.getElementById(id), {
    type: 'scatter',
    data: {
      datasets: colors.map((color, i) => ({
        label: 'Cluster ' + i,
        data: [],
        backgroundColor: color
      }))
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: 'Temperature (°C)' } },
        y: { title: { display: true, text: 'Humidity (%)' }, beginAtZero: true }
      }
    }
  });
}

socket.on('mqtt_message', function (data) {
  const time = new Date(data.timestamp).toLocaleTimeString();
  appendToChart(charts.realtime, time, data.temperature, data.humidity);
});

socket.on('history_data', function (entries) {
  updateChart(charts.history, entries);
});

socket.on('clustering_result', function (entries) {
  const scatter = [[], [], []];
  entries.forEach(e => {
    scatter[e.cluster].push({ x: e.temperature, y: e.humidity });
  });
  for (let i = 0; i < 3; i++) {
    charts.scatter.data.datasets[i].data = scatter[i];
  }
  charts.scatter.update();
});

function appendToChart(chart, label, temp, hum) {
  chart.data.labels.push(label);
  chart.data.datasets[0].data.push(temp);
  chart.data.datasets[1].data.push(hum);
  if (chart.data.labels.length > 20) {
    chart.data.labels.shift();
    chart.data.datasets[0].data.shift();
    chart.data.datasets[1].data.shift();
  }
  chart.update();
}

function updateChart(chart, entries) {
  chart.data.labels = [];
  chart.data.datasets[0].data = [];
  chart.data.datasets[1].data = [];
  entries.forEach(e => {
    const t = new Date(e.timestamp).toLocaleTimeString();
    chart.data.labels.push(t);
    chart.data.datasets[0].data.push(e.temperature);
    chart.data.datasets[1].data.push(e.humidity);
  });
  chart.update();
}

function loadHistoryChart() {
  socket.emit('load_history', 100);
}

function runClustering() {
  socket.emit('run_clustering', 3);
}

socket.emit('subscribe');
loadHistoryChart();