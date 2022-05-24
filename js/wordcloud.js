Highcharts.getJSON(
    'data/wordcloud_data.json',
    function (data) {  
        Highcharts.chart('container_wordcloud', {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: 0,
                plotShadow: false
            },
            title: false,
            series: [{
                type: 'wordcloud',
                data,
                name: 'Occurrences'
            }]
        });
    }
);
