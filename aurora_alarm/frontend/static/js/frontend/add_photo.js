$( document ).ready(function() {

    "Setup autocomplete for city search and turn on geocomplete."
    $("#city").geocomplete({
        map: "#map-canvas-location",
        details: "form",
        markerOptions: {
            draggable: true
        },
        detailsAttribute: "class",
        location: "Lulea"
    }).bind("geocode:result", function(event, result){
            $("#id_latitude").val(result.geometry.location.nb).change();
            $("#id_longitude").val(result.geometry.location.ob).change();
    });;

    "Bind marker and longitude/latitude fields."
    $("#city").bind("geocode:dragged", function(event, latLng) {
        $("#id_latitude").val(latLng.lat()).change();
        $("#id_longitude").val(latLng.lng()).change();
    });

});
