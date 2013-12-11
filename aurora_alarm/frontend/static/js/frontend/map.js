var locations = [];
var images = [];
var markers = [];
var iterator = 0;
var map;
$( document ).ready(function() {
    google.maps.event.addDomListener(window, 'load', loadPhotos);
});

function loadPhotos() {
    getPhotos(API_URL + "photo_with_location");
}

function getPhotos(url) {
    $.ajax({
        type: "GET",
        url: url,
        success: function(data) {
            for (var i = 0; i < data.results.length; i++) {
                var result = data.results[i];
                var location = new google.maps.LatLng(result.latitude, result.longitude);
                locations.push(location);
                var path = result.image;
                images.push('<img border="0" src="/static/photologue/' + path + '">');
            }
            url = data.next;
            if (url) {
                getPhotos(url);
            } else {
                initialize();
            }
        }
    });
}

function initialize() {
    var myLatlng = new google.maps.LatLng(65.585, 22.151);
    var mapOptions = {
        center: myLatlng,
        zoom: 11
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    drop();
}
function drop() {
    for (var i = 0; i < locations.length; i++) {
        setTimeout(function() {
            addMarker();
        }, i * 200);
    }
}
function addMarker() {
    var marker = new google.maps.Marker({
        position: locations[iterator],
        map: map,
        draggable: false,
        animation: google.maps.Animation.DROP
    });
    markers.push(marker);
    var infowindow = new google.maps.InfoWindow({
        content: images[iterator]
    });
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
    });
    iterator++;
}
