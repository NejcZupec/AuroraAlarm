$( document ).ready(function() {
	var means = [30, 29, 20, 12, 3, 1];
    "Get user specific values through API and prepare form values."
    $.ajax({
        type: "GET",
        url: API_URL + "user_profiles/?user=" + user_id,
        success: function(data) {
            $('#select-threshold').val(data.results[0].threshold);
            if (data.results[0].receive_daily_alarms == true) {
                $('#myonoffswitch-daily').prop("checked", "true");
            } else {
                $('#myonoffswitch-daily').removeProp("checked");
            }

            if (data.results[0].receive_real_time_alarms == true) {
                $('#myonoffswitch-real').prop("checked", "true");
            } else {
                $('#myonoffswitch-real').removeProp("checked");
            }

            $('#select-radius').val(data.results[0].radius);
            $('#lng').val(data.results[0].longitude);
            $('#lat').val(data.results[0].latitude);

            var lat_and_long = data.results[0].latitude + ", " + data.results[0].longitude;
            $("#city").geocomplete("find", lat_and_long);
            updateSummary();
        }
    });

    "Setup autocomplete for city search and turn on geocomplete."
    $("#city").geocomplete({
        map: "#map-canvas-location",
        details: "form",
        markerOptions: {
            draggable: true
        }
    });

    "Bind marker and longitude/latitude fields."
    $("#city").bind("geocode:dragged", function(event, latLng) {
        $("input[name=lat]").val(latLng.lat()).change();
        $("input[name=lng]").val(latLng.lng()).change();
    });

    "When values are changed (daily alarms), save them with AJAX request."
    $('#daily-alarms-settings-form').change(function() {

        if ($('#myonoffswitch-daily').is(":checked")) {
            var notifications_daily = true;
        } else {
            var notifications_daily = false;
        }

        if ($('#myonoffswitch-real').is(":checked")) {
            var notifications_real = true;
        } else {
            var notifications_real = false;
        }

        $.ajax({
            type: "PUT",
            url: API_URL + "user_profiles/" + user_id + "/",
            data: {
                'user': parseInt(user_id),
                'threshold': $('#select-threshold option:selected').text(),
                'receive_real_time_alarms': notifications_real,
                'receive_daily_alarms': notifications_daily
            },
            success: function(data) {
                $('#success-text').show(100);
                $('#success-text').delay(1500).fadeOut(1000);
                updateSummary();
            }
        });
    });

    "When values are changed (real-time alarms), save them with AJAX request."
    $('#real-time-alarms-settings-form').change(function() {

        if ($('#myonoffswitch-daily').is(":checked")) {
            var notifications_daily = true;
        } else {
            var notifications_daily = false;
        }

        if ($('#myonoffswitch-real').is(":checked")) {
            var notifications_real = true;
        } else {
            var notifications_real = false;
        }

        setTimeout(function() {
            $.ajax({
                type: "PUT",
                url: API_URL + "user_profiles/" + user_id + "/",
                data: {
                    'user': parseInt(user_id),
                    'longitude': $('#lng').val(),
                    'latitude': $('#lat').val(),
                    'radius': $('#select-radius').val(),
                    'receive_real_time_alarms': notifications_real,
                    'receive_daily_alarms': notifications_daily
                },
                success: function(data) {
                    $('#success-text-real-time').show(100);
                    $('#success-text-real-time').delay(1500).fadeOut(1000);
                	updateSummary();
                }
            });
        }, 500);

    });
    function updateSummary() {
		console.log("updating");
		if ($('#myonoffswitch-daily').is(":checked")) {
		    var value = $('#select-threshold option:selected').text();
			var text = "You will receive a notification, when auroral activity will be equal or above " + value +". Based on notifications history, you will receive approximately " + means[value] + " emails per month.";                
		    $('#summary-daily').prop('textContent', text);
		} else {
		console.log('false');
		    $('#summary-daily').prop('textContent', 'Switch daily alarms on to get notifications.');
		}
		if ($('#myonoffswitch-real').is(":checked")) {
			var text = "You will receive an email, when someone will notify others inside " + $('#select-radius').val() + "km around your position."              
		    $('#summary-real').prop('textContent', text);
		} else {
		console.log('false');
		    $('#summary-real').prop('textContent', 'Switch real-time alarms on to get notifications.');
		}
}
});
