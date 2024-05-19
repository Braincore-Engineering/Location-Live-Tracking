var map;

if (locations.length > 0) {
  var firstLocation = locations[0];
  map = L.map("map").setView([firstLocation.lat, firstLocation.lon], 13);
} else {
  map = L.map("map").setView([51.505, -0.09], 13);
}

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

var latlngs = locations.map(function (location) {
  return [location.lat, location.lon];
});

// Debugging: Log latlngs to console to check
console.log(latlngs);

if (locations.length > 0) {
  var firstLocationMarker = L.marker([firstLocation.lat, firstLocation.lon])
    .addTo(map)
    .bindPopup("Latitude: " + firstLocation.lat + "<br>Longitude: " + firstLocation.lon)
    .openPopup();
}

if (locations.length > 1) {
  var lastLocation = locations[locations.length - 1];
  L.marker([lastLocation.lat, lastLocation.lon])
    .addTo(map)
    .bindPopup("Latitude: " + lastLocation.lat + "<br>Longitude: " + lastLocation.lon)
    .openPopup();
}

// Calculate total distance
var totalDistance = 0;
for (var i = 0; i < latlngs.length - 1; i++) {
  totalDistance += map.distance(latlngs[i], latlngs[i + 1]);
}

// Define color gradient
var colorGradient = chroma.scale(['red', 'yellow']).mode('lab').colors(100);

// Interpolate points along each segment
function interpolatePoints(latlngs, numPoints) {
  var interpolatedLatlngs = [];
  for (var i = 0; i < latlngs.length - 1; i++) {
    var start = latlngs[i];
    var end = latlngs[i + 1];
    var segmentLength = map.distance(start, end);
    var segmentPoints = Math.ceil((segmentLength / totalDistance) * numPoints);

    for (var j = 0; j < segmentPoints; j++) {
      var t = j / segmentPoints;
      var lat = start[0] + t * (end[0] - start[0]);
      var lng = start[1] + t * (end[1] - start[1]);
      interpolatedLatlngs.push([lat, lng]);
    }
  }
  interpolatedLatlngs.push(latlngs[latlngs.length - 1]);
  return interpolatedLatlngs;
}

// Interpolate points to get a smoother gradient
var numPoints = 1000; // Adjust this number as needed for smoothness
var interpolatedLatlngs = interpolatePoints(latlngs, numPoints);

// Apply gradient to the polyline
var coloredPolyline = [];
for (var i = 0; i < interpolatedLatlngs.length - 1; i++) {
  var colorIndex = Math.floor((i / (interpolatedLatlngs.length - 1)) * (colorGradient.length - 1));
  var segment = L.polyline([interpolatedLatlngs[i], interpolatedLatlngs[i + 1]], {
    color: colorGradient[colorIndex],
    weight: 5,
    opacity: 0.8
  });
  coloredPolyline.push(segment);
  segment.addTo(map);
}

// Fit map bounds to the polyline
map.fitBounds(L.polyline(latlngs).getBounds());
