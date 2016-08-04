

var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var labelIndex = 0;

function initialize(lati, lon) {
    
    var test = { lat: lon, lng: lati };

    var mapProps = {
            zoom: 5,
            center: { lat: lon, lng:lati  }
        };
    var map = new google.maps.Map(document.getElementById('map'), mapProps);
    addMarker(test, map);
}


function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var marker = new google.maps.Marker({
    position: location,
    label: labels[labelIndex++ % labels.length],
    map: map
  });
};

