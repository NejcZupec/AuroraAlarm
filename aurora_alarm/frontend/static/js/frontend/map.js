    var locations = [
        new google.maps.LatLng(65.585, 22.151),
        new google.maps.LatLng(65.589, 22.148),
        new google.maps.LatLng(65.583, 22.155),
        new google.maps.LatLng(65.580, 22.145)
    ];
    var images = [
        '<img border="0" src="./aa.JPG">',
        '<img border="0" src="./aa2.JPG">',
        '<img border="0" src="./aa3.JPG">',
        '<img border="0" src="./aa4.JPG">'
    ];
    var markers = [];
    var iterator = 0;
    var map;
$( document ).ready(function() {
    console.log("Hello world");
    google.maps.event.addDomListener(window, 'load', initialize);
});

function initialize() {
    console.log("Initialization...");
    var myLatlng = new google.maps.LatLng(65.585, 22.151);
    var mapOptions = {
        center: myLatlng,
        zoom: 14
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
