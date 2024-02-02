class Map{
    constructor(){
        this.key = "pk.9bac73b8821d501d511a29413e757052"
        this.HTMLMap = document.getElementById("map")
        this.defaultCoordsValue = {lat: -30.088, lon: -51.023}
        this.radius = 500
        this.mapObject = null
        this.mapCircle = null
        this.showMap()
        this.displayCircle()
    }

    showMap(){
        let map = L.map(this.HTMLMap).setView(this.defaultCoordsValue, 15)

        L.tileLayer(`https://{s}-tiles.locationiq.com/v3/streets/r/{z}/{x}/{y}.raster?key=${this.apiKey}`, {
            maxZoom: 19,
            attribution: '&copy; <a href="https://locationiq.com/attribution" title="Affordable, Scalable & Reliable location services">LocationIQ</a>'
        }).addTo(map)

        this.mapObject = map
    }

    displayCircle(){
        let circle = L.circle([-30.09, -51.04], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: this.radius,
        }).addTo(this.mapObject)

        this.mapCircle = circle
    }

    get apiKey(){
        return this.key
    }

    set lat(newLat){
        this.lat = newLat
    }

    set lon(newLon){
        this.lat = newLon
    }
}

document.addEventListener("DOMContentLoaded", ()=> {
    const options = {method: 'GET', headers: {accept: 'application/json'}}
    const btn_increaseZoom = document.getElementById("increase-zoom")
    const btn_decreaseZoom = document.getElementById("decrease-zoom")
    const inputLocation = document.getElementById("location")
    const coords = {lat: 0.0, lon: 0.0}
    const locationMap = new Map()
    
    inputLocation.addEventListener("focusout", () =>{

        if(inputLocation.value != ''){
            fetch(`https://us1.locationiq.com/v1/search?q=${inputLocation.value}&format=json&matchquality=0&key=${locationMap.apiKey}`, options)
            .then(response => response.json())
            .then(response => getCoords(response, coords))
            .then(response => changeMapView(coords))
            .catch(err => console.error(err))
        }
    })

    btn_increaseZoom.addEventListener("click", () => {
        locationMap.mapCircle.setRadius(locationMap.mapCircle.getRadius() + 20)
    })

    btn_decreaseZoom.addEventListener("click", () => {
        locationMap.mapCircle.setRadius(locationMap.mapCircle.getRadius() - 20)
    })

    function getCoords(response, coords){
        try{
            const latitude = parseFloat(response[0].lat)
            const longetude = parseFloat(response[0].lon)
            coords.lat = latitude
            coords.lon = longetude
        }catch (error){
            alert("Deu erro papai: " + error)
        }
    }

    function changeMapView(coords){
        locationMap.mapObject.panTo(coords, 15)
    }
})