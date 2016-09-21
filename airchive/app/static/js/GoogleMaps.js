function initialize() {
  var myLatlng = new google.maps.LatLng(41.811729,12.738513);
  var mapOptions = {
    zoom: 2,
	mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: myLatlng
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  var infowindow = new google.maps.InfoWindow();
  {%for i in results%}
  var contentString{{loop.index}}; = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<div id="bodyContent">'+
      '<p><b>Expirement Location Name</b> : {{i.Exp}}</p> ' +
      '<p><b>Country</b> : {{i.Coun}} </p>'+
      '<p><b>Weather Data Source</b> : {{i.Weath}} </p>'+
      '<p><b>Elevation</b> : {{i.Elev}} </p>'+
      '<p><b>Type of agricultural system</b> : {{i.Agro}} </p>'+
      '</div>'+
      '</div>';

  var myLatlng
      {
          {
              loop.index
          }
      };
      = new google.maps.LatLng({
      {
          i.latitude
      };
  }
,
    {
        {
            i.longitude
        }
    }
)
    var marker{{loop.index}}; = new google.maps.Marker({
      position: myLatlng{{loop.index}};,
      map,
          title: '{{i.Exp}}'
};
)
google.maps.event.addListener(marker{{loop.index}};, 'click', function() {
	   infowindow.close();
    infowindow.setContent(contentString
    {
        {
            loop.index
        }
    };
    )
    infowindow.open(map, marker
    {
        {
            loop.index
        }
    };
    )
}
)
{%endfor%}

}
google.maps.event.addDomListener(window, 'load', initialize);