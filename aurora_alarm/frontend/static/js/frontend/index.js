$( document ).ready(function() {

    // prepare today's date in Python's format
    var d = new Date();
    var date = d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();

    // get aurora daily value via API, if exists in database
    $.ajax({
        type: "GET",
        url: API_URL + "aurora_daily_forecast/?date=" + date,
        success: function(data) {

            // if aurora value for today exists, show current value and the progress bar
            if (data.count != 0) {
                var current_value = data.results[0].current_value;

                $("#aurora-value-progress-bar").show();
                $("#current-aurora-value").html(current_value);

                /* Calculate a value for progressbar (convert between two intervals)
                        Input interval: 0...5
                        Output interval: 0...100 */
                var interval_value = 100.0/5 * current_value;

                $("#aurora-value-progress-bar .progress-bar").css("width", interval_value + "%");
            }
        }
    });

});
