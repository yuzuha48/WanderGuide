async function saveDays(event, trip_id) {
    event.preventDefault();
    resetFlashMessage();
    let form_json = {};
    let forms = document.getElementsByClassName("day_form");

    Array.from(forms).forEach((form, index) => {
        let dayData = new FormData(form);
        form_json[index] = {};
        for (let [key, value] of dayData.entries()) {
            form_json[index][key] = value;
        }
    });

    const response = await fetch(`/add_days/${trip_id}`, {
            method: 'POST', 
            body: JSON.stringify(form_json), 
            headers: {
                'Content-Type': 'application/json'
            }
        }); 

    const data = await response.json();
    if ("errors" in data) {
        resetFlashMessage();
        let errorsHTML = ""; 
        for(let error of Object.values(data.errors)) {
            errorsHTML += `<p>${error}</p>`;
        }
        showFlashMessage(errorsHTML);
        window.location.href = "#top";
    }
    else if ("success" in data && data.success) {
        window.location.href = 'http://127.0.0.1:5001/profile';
    }
    else {
        showFlashMessage("Something went wrong. Please try again.");
        window.location.href = "#top";
    }
}

function resetFlashMessage() {
    let flashMessagesContainer = document.getElementById('errorMessages');
    flashMessagesContainer.classList.add("hidden");
    let messages = flashMessagesContainer.querySelectorAll('p');
    messages.forEach(message => {
        message.remove();
    } )
}

function showFlashMessage(message) {
    let flashMessagesContainer = document.getElementById('errorMessages');
    flashMessagesContainer.classList.remove("hidden");
    let flashMessageElement = document.createElement('p');
    flashMessageElement.innerHTML = message;
    flashMessagesContainer.appendChild(flashMessageElement);
}

var dayCount = 1; 
function addDay() {
    dayCount++;
    let allDays = document.getElementById("all_days");
    let oneDay = document.createElement("div");
    oneDay.classList.add("one_day");
    oneDay.innerHTML = `
    <form method="post" class="day_form">
        <h2>Day ${dayCount}</h2>
        <div class="mb-3">
            <label for="day_theme" class="form-label">Brief Description of Day ${dayCount}</label>
            <input type="text" class="form-control" id="day_theme" name="day_theme" placeholder="Spend the day like a local!">
        </div>
        <div class="mb-3">
            <label for="location" class="form-label">Location</label>
            <input type="text" class="form-control" id="location" name="location" placeholder="Shimokitazawa">
        </div>
        <div class="mb-3">
            <label for="activity" class="form-label">Activity</label>
            <textarea class="form-control" id="activity" name="activity" rows="5" placeholder="Roam the streets and go to as many thrift stores as you can!"></textarea>
        </div>
    </form>
    `;
    allDays.appendChild(oneDay);
}

function saveTrip(image, trip_id) {
    fetch(`/save/${trip_id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (image.src.endsWith("empty_heart.png")) {
            image.src = "/static/images/red_heart.png";
        } else {
            image.src = "/static/images/empty_heart.png";
        }
    })
    .catch(error => {
        console.error(error);
    });
    location.reload();
}

function unsaveTrip(image, trip_id) {
    fetch(`/unsave/${trip_id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (image.src.endsWith("empty_heart.png")) {
            image.src = "/static/images/red_heart.png";
        } else {
            image.src = "/static/images/empty_heart.png";
        }
    })
    .catch(error => {
        console.error(error);
    });
    location.reload();
}

async function updateDays(event) {
    event.preventDefault();
    resetFlashMessage();
    let form_json = {};
    let forms = document.getElementsByClassName("day_form");

    Array.from(forms).forEach((form) => {
        let day_id = form.querySelector(".day_id").innerText
        let dayData = new FormData(form);
        form_json[day_id] = {};
        for (let [key, value] of dayData.entries()) {
            form_json[day_id][key] = value;
        }
    });

    const response = await fetch(`/edit_days`, {
            method: 'POST', 
            body: JSON.stringify(form_json), 
            headers: {
                'Content-Type': 'application/json'
            }
        }); 

    const data = await response.json();
    if ("errors" in data) {
        resetFlashMessage();
        let errorsHTML = ""; 
        for(let error of Object.values(data.errors)) {
            errorsHTML += `<p>${error}</p>`;
        }
        showFlashMessage(errorsHTML);
        window.location.href = "#top";
    }
    else if ("success" in data && data.success) {
        window.location.href = 'http://127.0.0.1:5001/profile';
    }
    else {
        showFlashMessage("Something went wrong. Please try again.");
        window.location.href = "#top";
    }
}

function search() {
    let searchInput = document.getElementById('searchInput');
    let allTrips = document.getElementById('all_trips');
    let trips = Array.from(allTrips.getElementsByClassName('card'));
    let searchTerm = searchInput.value.toLowerCase();
    trips.forEach(function(trip) {
        let text = trip.querySelector('h5').textContent.toLowerCase();
        if(text.includes(searchTerm)) {
            trip.style.display = 'block';
        }
        else {
            trip.style.display = 'none';
        }
    });
}

function initMap() {
    let tripIdElement = document.getElementById("trip_id"); 
    let tripId = tripIdElement.innerText;

    let city = document.getElementById("city").textContent
    let geocoder = new google.maps.Geocoder();

    geocoder.geocode({address: city}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            if (results.length > 0) {
                results = results[0].geometry.location; 
                city_coordinates = {lat: results.lat(), lng: results.lng()}

                let map = new google.maps.Map(document.getElementById('map'), {
                    center: city_coordinates, 
                    zoom: 9.5
                });
            
                map.addListener('click', event => {
                    placeMarker(event.latLng, map);
                    let latitude = event.latLng.lat();
                    let longitude = event.latLng.lng();
                    
                    let mapData = new FormData(); 
                    mapData.append('latitude', latitude);
                    mapData.append('longitude', longitude);
            
                    fetch(`/save_coordinates/${tripId}`, { 
                        method: 'POST', 
                        body: mapData
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                    })
                    .catch(error => {
                        console.error(error);
                    });
                });
            }
        }
    });
}

function placeMarker(location, map) {
    new google.maps.Marker({
        position: location,
        map: map
    });
}

function initMapView() {
    let city = document.getElementById("city").textContent;
    let geocoder = new google.maps.Geocoder();

    geocoder.geocode({address: city}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            if (results.length > 0) {
                results = results[0].geometry.location; 
                city_coordinates = {lat: results.lat(), lng: results.lng()}

                let map = new google.maps.Map(document.getElementById('map'), {
                    center: city_coordinates, 
                    zoom: 9.5
                });

                let coordinates = document.querySelectorAll(".latlong");
                Array.from(coordinates).forEach(coordinate => {
                    let latitude = parseFloat(coordinate.querySelector(".latitude").textContent);
                    let longitude = parseFloat(coordinate.querySelector(".longitude").textContent);
                    let location = {lat: latitude, lng: longitude};

                    let marker = new google.maps.Marker({
                        position: location, 
                        map: map
                    });
                });
            }
        }
    });
}

function initMapEdit() {
    let tripIdElement = document.getElementById("trip_id"); 
    let tripId = tripIdElement.innerText;

    let city = document.getElementById("city").textContent;
    let geocoder = new google.maps.Geocoder();

    geocoder.geocode({address: city}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            if (results.length > 0) {
                results = results[0].geometry.location; 
                city_coordinates = {lat: results.lat(), lng: results.lng()}
                
                let map = new google.maps.Map(document.getElementById('map'), {
                    center: city_coordinates, 
                    zoom: 9.5
                });

                let coordinates = document.querySelectorAll(".latlong");
                Array.from(coordinates).forEach(coordinate => {
                    let latitude = parseFloat(coordinate.querySelector(".latitude").textContent);
                    let longitude = parseFloat(coordinate.querySelector(".longitude").textContent);
                    let location = {lat: latitude, lng: longitude};

                    let marker = new google.maps.Marker({
                        position: location, 
                        map: map
                    });
                });

                map.addListener('click', event => {
                    placeMarker(event.latLng, map);
                    let latitude = event.latLng.lat();
                    let longitude = event.latLng.lng();
                    
                    let mapData = new FormData(); 
                    mapData.append('latitude', latitude);
                    mapData.append('longitude', longitude);
            
                    fetch(`/save_coordinates/${tripId}`, { 
                        method: 'POST', 
                        body: mapData
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                    })
                    .catch(error => {
                        console.error(error);
                    });
                });
            }
        }
    });
}