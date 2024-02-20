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
        let my_cricle = new L.Draggable(this.mapCircle)
        my_cricle.enable()
    }

    get apiKey(){
        return this.key
    }

    get getRadius(){
        return this.radius
    }

    set setRadius(newRadius){
        this.radius = newRadius
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
        // CREATE AJAX TO SEND DATA WITH POST METHOD
    })

    btn_increaseZoom.addEventListener("click", () => {
        if (locationMap.mapCircle.getRadius() <= 1020){

            cursorEnable(btn_increaseZoom)
            locationMap.mapCircle.setRadius(locationMap.mapCircle.getRadius() + 20)
        }else{
            cursorDisable(btn_increaseZoom)
        }
    })

    btn_decreaseZoom.addEventListener("click", () => {
        if (locationMap.mapCircle.getRadius() >= 360){

            cursorEnable(btn_decreaseZoom)
            locationMap.mapCircle.setRadius(locationMap.mapCircle.getRadius() - 20)
        }else{
            cursorDisable(btn_decreaseZoom)
        }
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
        changeMapCircle(coords)
    }

    function changeMapCircle(coords){
        locationMap.mapCircle.setLatLng(coords)
        
    }

    function cursorEnable(btnElement){
        if(btnElement.previousElementSibling != null && btnElement.previousElementSibling.hasAttribute("attribute", "disabled")){
            btnElement.previousElementSibling.removeAttribute("attribute", "disabled")
            btnElement.previousElementSibling.style.cursor = "pointer"

        }else if(btnElement.previousElementSibling === null && btnElement.nextElementSibling.hasAttribute("attribute", "disabled")){
            btnElement.nextElementSibling.removeAttribute("attribute", "disabled")
            btnElement.nextElementSibling.style.cursor = "pointer"
        }
    }

    function cursorDisable(btnElement){
        btnElement.setAttribute("attribute", "disabled")
        btnElement.style.cursor = "not-allowed"
    }
})