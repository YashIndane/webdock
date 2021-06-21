// This function receives the command and writes the output to the division
function exe(){

var command = document.getElementById("ibox").value;

var xhr = new XMLHttpRequest();

var queryString = "http://IP/cgi-bin/main.py?cmd=" + command;

// go to the API
xhr.open("GET", queryString, true);

xhr.send();

xhr.onload = function() {
  // get the response from API
  var output = xhr.responseText;
    
  // writing the output to a division
  document.getElementById("outdiv").innerHTML = output;
  }
}

// This function shows the available images
function img(){

var xhr = new XMLHttpRequest();

var queryString = "http://IP/cgi-bin/img.py";

// go to the API
xhr.open("GET", queryString, true);

xhr.send();

xhr.onload = function() {
  // get the response from API
  var output = xhr.responseText;

  // writing the output to a division
  document.getElementById("outdiv").innerHTML = output;
  }
}

// This function shows the running conainers
function lvcon(){

var xhr = new XMLHttpRequest();

var queryString = "http:/IP/cgi-bin/con.py";

// go to the API
xhr.open("GET", queryString, true);

xhr.send();

xhr.onload = function() {
  // get the response from API
  var output = xhr.responseText;

  // writing the output to a division
  document.getElementById("outdiv").innerHTML = output;
  }
}
