var newImage;
var xArray = [];
var yArray = [];
var long = [];
var lat = [];
var iterator = 0;

// Retrieve photo



document.getElementById("editbtn").onclick = function spawnClickable() {
    newImage = document.createElement('img');
    newImage.src = imageSource;    //make this the upload's 'e.target.result',  'e' being the parameter of the file when uploaded
    document.body.appendChild(newImage);   //after this it still needs to exit the *image upload modal* (also try to restric to a single upload at a time)

    newImage.addEventListener("mousedown", function (e) {
    	var currenti = iterator;

    	xArray[currenti] = e.offsetX;
    	yArray[currenti] = e.offsetY;

    	var label, latitude, longitude, latbtn, longbtn;  //this looks really messy but its functional
		label = document.createElement('modal');
		label.appendChild(document.createTextNode('Point ' + currenti +  ' x: ' + xArray[currenti] + ' y: ' + yArray[currenti]));

		latitude = document.createElement('input');
		latitude.type = 'text';

		latbtn = document.createElement('button');
		latbtn.onclick = function updateLat() {
			latbtn.innerHTML = 'Latitude: ' + latitude.value;
			lat[currenti] = latitude.value;
		};
		latbtn.innerHTML = 'Update latitude';




		longitude = document.createElement('input');
		longitude.type = 'text';
		longbtn = document.createElement('button');
		longbtn.onclick = function updateLat() {
			longbtn.innerHTML = 'Longitude: ' + longitude.value;
			long[currenti] = longitude.value;
			console.log(longitude.value);
		};
		longbtn.innerHTML = 'Update longitude';

		label.appendChild(latitude);
		label.appendChild(latbtn);
		label.appendChild(longitude);
		label.appendChild(longbtn);
		document.body.appendChild(label);

    	iterator++;
	});


	var finishbtn = document.createElement('button');
		finishbtn.onclick = function finish() {
			var string = "";

			for (var i = 0; i < iterator; i++){
				string += 'Point ' + i + '<br>';
				string += 'x: ' + xArray[i] + '<br>';
				string += 'y: ' + yArray[i] + '<br>';
				string += 'latitude: ' + lat[i] + '<br>';
				string += 'longitude: ' + long[i] + '<br><br>';
			}
			document.write(string); //instead of this, upload the data to server
		};
		finishbtn.innerHTML = 'Finish Editing';

		document.body.appendChild(finishbtn);
};
