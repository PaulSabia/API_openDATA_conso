function filiereCheck() {
    document.getElementById('region_check').style.display = 'none';
    document.getElementById('both_check').style.display = 'none';
    if (document.getElementById('filiere').checked) {
        document.getElementById('filiere_check').style.display = 'block';
    } else {
        document.getElementById('filiere_check').style.display = 'none';
    }
}

function regionCheck() {
    document.getElementById('filiere_check').style.display = 'none';
    document.getElementById('both_check').style.display = 'none';
    if (document.getElementById('region').checked) {
        document.getElementById('region_check').style.display = 'block';
    } else {
        document.getElementById('region_check').style.display = 'none';
    }
}

function bothCheck() {
    document.getElementById('filiere_check').style.display = 'none';
    document.getElementById('region_check').style.display = 'none';
    if (document.getElementById('both').checked) {
        document.getElementById('both_check').style.display = 'block';
    } else {
        document.getElementById('both_check').style.display = 'none';
    }
}

Highcharts.chart('container', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Consommation énergétique du 22 Décembre 2020'
    },
    subtitle: {
      text: ''
    },
    xAxis: {
      categories: region,
      crosshair: true
    },
    yAxis: {
      min: 0,
      title: {
        text: 'Consommation (Mwh)'
      }
    },
    tooltip: {
      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
        '<td style="padding:0"><b>{point.y:.1f} kwh</b></td></tr>',
      footerFormat: '</table>',
      shared: true,
      useHTML: true
    },
    plotOptions: {
      column: {
        pointPadding: 0.2,
        borderWidth: 0
      }
    },
    series: [{
      name: 'Gaz',
      data: gaz
  
    }, {
      name: 'Electricité',
      data: elec
  
    }]
  });


