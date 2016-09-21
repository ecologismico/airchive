function initialize() {
  var myLatlng = new google.maps.LatLng(47.5573475,7.577261);
  var mapOptions = {
    zoom: 17,
	mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: myLatlng
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  var infowindow = new google.maps.InfoWindow();
  
  var contentString1 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng1 = new google.maps.LatLng(47.5573475,7.577261);
  var marker1 = new google.maps.Marker({
      position: myLatlng1,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker1, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString1);
	   infowindow.open(map, marker1);
  });
  
  var contentString2 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng2 = new google.maps.LatLng(47.5573711111,7.57719866667);
  var marker2 = new google.maps.Marker({
      position: myLatlng2,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker2, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString2);
	   infowindow.open(map, marker2);
  });
  
  var contentString3 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng3 = new google.maps.LatLng(47.5566422778,7.57847380556);
  var marker3 = new google.maps.Marker({
      position: myLatlng3,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker3, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString3);
	   infowindow.open(map, marker3);
  });
  
  var contentString4 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng4 = new google.maps.LatLng(47.5565973889,7.57848172222);
  var marker4 = new google.maps.Marker({
      position: myLatlng4,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker4, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString4);
	   infowindow.open(map, marker4);
  });
  
  var contentString5 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng5 = new google.maps.LatLng(47.5566314444,7.57828672222);
  var marker5 = new google.maps.Marker({
      position: myLatlng5,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker5, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString5);
	   infowindow.open(map, marker5);
  });
  
  var contentString6 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng6 = new google.maps.LatLng(47.5566300556,7.57825422222);
  var marker6 = new google.maps.Marker({
      position: myLatlng6,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker6, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString6);
	   infowindow.open(map, marker6);
  });
  
  var contentString7 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng7 = new google.maps.LatLng(47.5566104444,7.57826563889);
  var marker7 = new google.maps.Marker({
      position: myLatlng7,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker7, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString7);
	   infowindow.open(map, marker7);
  });
  
  var contentString8 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : </p> ' +
      '<p><b>Country</b> :  </p>'+
      '<p><b>Weather Data Source</b> :  </p>'+
      '<p><b>Elevation</b> :  </p>'+
      '<p><b>Type of agricultural system</b> :  </p>'+
      '</div>'+
      '</div>';

  var myLatlng8 = new google.maps.LatLng(47.5565983056,7.57826563889);
  var marker8 = new google.maps.Marker({
      position: myLatlng8,
      map: map,
      title: ''
  });
  google.maps.event.addListener(marker8, 'click', function() {
	   infowindow.close();
	   infowindow.setContent(contentString8);
	   infowindow.open(map, marker8);
  });
  }
  google.maps.event.addDomListener(window, 'load', initialize);