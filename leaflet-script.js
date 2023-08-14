function initMap() {
    let map = L.map('map').setView([40.0, 32.0], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    conquestData.forEach(conquest => {
        L.marker([conquest.lat, conquest.lon])
            .addTo(map)
            .bindPopup(`<strong>${conquest.Name}</strong><br>${conquest.Year}</strong><br>${conquest.Era}`);
    });

    //Create a marker layer (in the example done via a GeoJSON FeatureCollection)
    var sliderControl = L.control.sliderControl({position: "bottomright", layer: geojsonData});

    //Make sure to add the slider to the map ;-)
    map.addControl(sliderControl);

    //And initialize the slider
    sliderControl.startSlider();
}

let conquestData = []; // This variable will store our parsed data

Papa.parse('data_year.csv', {
    download: true,
    header: true,
    dynamicTyping: true,
    complete: function(results) {
        conquestData = results.data;
        var geojsonData = {
            type: "FeatureCollection",
            features: []
        };

        results.data.forEach(function(row) {
            if(row.Year !== null && row.Year !== "") {
                var feature = {
                    type: "Feature",
                    properties: {
                        time: row.Year + "-01-01" // Assuming you want to set the time as the start of the year
                    },
                    geometry: {
                        type: "Point",
                        coordinates: [row.lon, row.lat]
                    }
                };
                geojsonData.features.push(feature);
                }
        });

        console.log(conquestData);
        console.log(geojsonData);
        initMap(); // Call a function to display the map once the data is loaded
    }
});


