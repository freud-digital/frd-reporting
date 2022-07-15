Highcharts.getJSON(
    'data/all_manifestations_hc.json',
    function (data) {  
        Highcharts.chart('container_manifestations_all', {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: 0,
                plotShadow: false
            },
            title: {
                'text': data[0][1]+data[1][1]
            },
            tooltip: {
                pointFormat: 'Manifestationen: <b>{point.y}</b>'
            },
            accessibility: {
                point: {
                    valueSuffix: '%'
                }
            },
            plotOptions: {
                pie: {
                    dataLabels: {
                        enabled: true,
                        distance: -50,
                        style: {
                            fontWeight: 'bold',
                            color: 'white'
                        }
                    },
                    startAngle: -90,
                    endAngle: 90,
                    center: ['50%', '75%'],
                    size: '110%'
                }
            },
            series: [{
                type: 'pie',
                innerSize: '50%',
                data: data
            }]
        });
    }
);
