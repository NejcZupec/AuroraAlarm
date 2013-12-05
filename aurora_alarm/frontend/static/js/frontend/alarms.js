$( document ).ready(function() {
    // TODO: Remove to seperate file.
    "Cross site request forgery protection"
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

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
