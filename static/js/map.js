// Function to initialize and draw the map
function initializeMap(locations) {
  // If map already exists, remove it
  if (map) {
    map.remove(); // Clear the previous map instance
  }

  // Create a new map instance
  if (locations.length > 0) {
    var firstLocation = locations[0];
    map = L.map("map").setView([firstLocation.lat, firstLocation.lon], 13);
  } else {
    map = L.map("map").setView([51.505, -0.09], 13); // Default location
  }

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
  }).addTo(map);

  // Clear existing markers and polylines
  map.eachLayer(function (layer) {
    if (layer instanceof L.Marker || layer instanceof L.Polyline) {
      map.removeLayer(layer);
    }
  });

  // Add markers for first and last locations
  if (locations.length > 0) {
    // Marker for the first location
    var firstMarker = L.marker([firstLocation.lat, firstLocation.lon])
      .addTo(map)
      .bindPopup("First Location: " + firstLocation.name); // Add popup if name exists

    // Marker for the last location
    var lastLocation = locations[locations.length - 1];
    var lastMarker = L.marker([lastLocation.lat, lastLocation.lon])
      .addTo(map)
      .bindPopup("Last Location: " + lastLocation.name); // Add popup if name exists
  }

  // Create a polyline for all locations
  if (locations.length > 1) {
    var latlngs = locations.map(function (location) {
      return [location.lat, location.lon];
    });
    var polyline = L.polyline(latlngs, {
      color: "blue",
      dashArray: "10, 10",
    }).addTo(map);
    map.fitBounds(polyline.getBounds());
  }
}
