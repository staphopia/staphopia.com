function generate_sequencing_center_chart() {
    Highcharts.chart('sequencing-centers', {
        data: { table: 'sequencing-centers-table'},
        chart: { type: 'column' },
        legend: { enabled: false },
        title: { text: 'Top 10 S. aureus Sequencing Contributors'},
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                useHTML: true,
                style: {
                    fontSize: '12px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            type: 'logarithmic',
            allowDecimals: false,
            title: { text: 'Total Samples In ENA Database' }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name;
            }
        }
    });
}

function generate_mlst_chart() {
    Highcharts.chart('mlst', {
        data: { table: 'mlst-table'},
        chart: { type: 'column'},
        legend: { enabled: false },
        title: { text: 'Top 10 S. aureus Sequenced MLSTs'},
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                useHTML: true,
                style: {
                    fontSize: '12px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            type: 'logarithmic',
            allowDecimals: false,
            title: { text: 'Total Samples' }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name;
            }
        }
    });
}

function generate_sequence_quality_chart() {
    Highcharts.chart('sequence-quality-chart', {
        data: { table: 'seqeunce-quality-table'},
        chart: { type: 'column'},
        title: { text: 'Per Base Sequencing Quality'},
        xAxis: {
            type: 'category',
            title: { text: 'Position' },
            labels: {
                useHTML: true,
                style: {
                    fontSize: '12px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            max: 42,
            tickInterval: 2,
            allowDecimals: false,
            title: { text: 'Mean Quality' }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name;
            }
        }
    });
}
