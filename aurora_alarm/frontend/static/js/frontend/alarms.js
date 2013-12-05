$( document ).ready(function() {

    "Get current threshold value for specific user and prepare form values."
    $.ajax({
        type: "GET",
        url: API_URL + "user_profiles/?user=" + user_id,
        success: function(data) {
            $('#select-threshold').val(data.results[0].threshold);

            if (data.results[0].receive_daily_alarms == true) {
                $('#myonoffswitch').prop("checked", "true");
            } else {
                $('#myonoffswitch').removeProp("checked");
            }
        }
    });

    "When values are changed, save them with AJAX request."
    $('#daily-alarms-settings-form select, #myonoffswitch').change(function() {

        if ($('#myonoffswitch').prop("checked")) {
            var notifications = true;
        } else {
            var notifications = false;
        }

        $.ajax({
            type: "PUT",
            url: API_URL + "user_profiles/" + user_id + "/",
            data: {
                'user': parseInt(user_id),
                'threshold': $('#select-threshold option:selected').text(),
                'receive_daily_alarms': notifications
            },
            success: function(data) {
                $('#success-text').show(100);
                $('#success-text').delay(1500).fadeOut(1000);
            }
        });
    });

});
