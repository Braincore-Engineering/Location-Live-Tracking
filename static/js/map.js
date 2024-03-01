var map;

// Check if there are locations available
if (locations.length > 0) {
  var firstLocation = locations[0];

  // Initialize the map and set view to the first location
  map = L.map("map").setView([firstLocation.lat, firstLocation.lon], 13);
} else {
  // Initialize the map with default view
  map = L.map("map").setView([51.505, -0.09], 13);
}

// Add a base layer to the map
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

// Extract latitude and longitude from locations array
var latlngs = locations.map(function (location) {
  return [location.lat, location.lon];
});

// Add marker for the first location
if (locations.length > 0) {
  var firstLocation = locations[0];
  L.marker([firstLocation.lat, firstLocation.lon])
    .addTo(map)
    .bindPopup("Latitude: " + firstLocation.lat + "<br>Longitude: " + firstLocation.lon)
    .openPopup();
}

// Add marker for the last location
if (locations.length > 1) {
  var lastLocation = locations[locations.length - 1];
  L.marker([lastLocation.lat, lastLocation.lon])
    .addTo(map)
    .bindPopup("Latitude: " + lastLocation.lat + "<br>Longitude: " + lastLocation.lon)
    .openPopup();
}

// Create a polyline with dashed lines, starting from the second location
if (locations.length > 1) {
  var polyline = L.polyline(latlngs.slice(1), { dashArray: "10, 10" }).addTo(map);
}
