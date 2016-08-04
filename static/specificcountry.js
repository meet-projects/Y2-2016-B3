$(document).ready(function() { 
//	var map = new google.maps.Map(document.getElementById("map"), {center: {lat: 0, lng: 0}, zoom:2});
	//console.log(map);


	// In the following example, markers appear when the user clicks on the map.
// Each marker is labeled with a single alphabetical character.
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var labelIndex = 0;

  function initialize(lati, lon) {

    //var Italy = { lat: 41.8719, lng: 12.5674 };
    //var Israel = { lat: 31.0461, lng: 34.8516 };
    //var Mexico = { lat: 23.6345, lng: 102.5528 };
    //var Palestine = { lat: 31.9522, lng:  35.2332 };
    //var countrylat = {"Israel":Israel, "Mexico":Mexico,"Palestine":Palestine,:"Italy":Italy}
    console.log("Lat, Long: " + lati + ", " + lon);
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: { lat: lati, lng: lon  }
    });

    // This event listener calls addMarker() when the map is clicked.


    // Add a marker at the center of the map.

    addMarker({ lat: lati, lng: lon  }, map);
  }

  // Adds a marker to the map.
  function addMarker(location, map) {
    // Add the marker at the clicked location, and add the next-available label
    // from the array of alphabetical characters.
    var marker = new google.maps.Marker({
      position: location,
      label: labels[labelIndex++ % labels.length],
      map: map
    });
  };

});


function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var marker = new google.maps.Marker({
    position: location,
    label: labels[labelIndex++ % labels.length],
    map: map
  });
};

function initialize(lati, lon) {

    var Italy = { lat: 41.8719, lng: 12.5674 };
    //var Israel = { lat: 31.0461, lng: 34.8516 };
    //var Mexico = { lat: 23.6345, lng: 102.5528 };
    //var Palestine = { lat: 31.9522, lng:  35.2332 };
    //var countrylat = {"Israel":Israel, "Mexico":Mexico,"Palestine":Palestine,:"Italy":Italy}
    console.log("Lat, Long: " + lati + ", " + lon);
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: Italy
    });

    console.log(map);

    // This event listener calls addMarker() when the map is clicked.


    // Add a marker at the center of the map.

    addMarker({ lat: lati, lng: lon  }, map);
  }