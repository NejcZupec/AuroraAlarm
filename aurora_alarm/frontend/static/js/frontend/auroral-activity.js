$( document ).ready(function() {

    // Hihgcharts chart for AuroraActivity
    $(function() {
        $.getJSON(API_URL + 'aurora_activity_chart_data_json/', function(data) {
            // Create the chart
            $('#auroral-activity-chart-container').highcharts('StockChart', {
                rangeSelector : {
                    selected : 1
                },

                yAxis : {
                    title : {
                        text : 'Auroral activity level'
                    },
                    plotLines : [{
                        value : 3,
                        color : 'red',
                        dashStyle : 'shortdash',
                        width : 2,
                        label : {
                            text : 'Alarm threshold'
                        }
                    }]
                },

                scrollbar : {
                    enabled: false
                },

                series : [{
                    name : 'Auroral activity level',
                    data : data,
                    type : 'column',
                    marker : {
                        enabled : true,
                        radius : 3
                    },
                    tooltip: {
                        valueDecimals: 0
                    }
                }]
            });
        });
    });
});
