/*
$(function(){$("a#calculate").bind("click",function(){$.getJSON("/unibas/CaseStudies/Study 1",{quantity:$(".chosen-select").val(),fromtime:$("#datetimepicker1").val(),totime:$("#datetimepicker2").val(),filter:"flot"},function(a){var c=a.data;$.plot($("#placeholder"),[{data:c,color:"#428bca",shadowSize:0,label:a.label}],{yaxis:{},xaxis:{mode:"time",timeformat:"%H:%M",timezone:"+0300"},grid:{hoverable:!0},points:{show:!0},lines:{show:!0}});$("#placeholder").bind("plothover",function(a,c,b){b?($("#tooltip").remove(),
a=moment(b.datapoint[0]/1E3-10800,"X").format("HH:mm"),showTooltip(b.pageX,b.pageY,a+" : "+b.datapoint[1])):$("#tooltip").remove()})});return!1})});function showTooltip(a,c,d){$('<div id="tooltip">'+d+"</div>").css({position:"absolute",display:"none",top:c-30,left:a+5,border:"1px solid #ddd",padding:"2px 5px","background-color":"#eee",opacity:1}).appendTo("body").fadeIn(300)};
*/

$(function() {
	
	$("a#calculate").click(function () {
	       var select = $('select#quantity');
			var selectedItem= select.find(':selected');
			window.optgroupLabel = selectedItem.parent().prop('label');
	   });       
    $("a#calculate").bind("click", function() {
		
        $.getJSON("/hydro/getdata/", {
            quantity: $(".chosen-select").val(),
            fromtime: $("#datetimepicker1").val(),
            totime: $("#datetimepicker2").val(),
            format: "flot",
			station: optgroupLabel
        }, function(a) {
            var c = a.data;
            $.plot($("#placeholder"), [{
                data: c,
                color: "#428bca",
                shadowSize: 0,
                label: a.label
            }], {
                yaxis: {},
                xaxis: {
                    mode: "time",
                    timeformat: "%H:%M",
                    timezone: "+0300"
                },
                grid: {
                    hoverable: !0
                },
                points: {
                    show: !0
                },
                lines: {
                    show: !0
                }
            });
            $("#placeholder").bind("plothover", function(a, c, b) {
                b ? ($("#tooltip").remove(),
                    a = moment(b.datapoint[0] / 1E3 - 10800, "X").format("HH:mm"), showTooltip(b.pageX, b.pageY, a + " : " + b.datapoint[1])) : $("#tooltip").remove()
            })
        });
        return !1
    })
});

function showTooltip(a, c, d) {
    $('<div id="tooltip">' + d + "</div>").css({
        position: "absolute",
        display: "none",
        top: c - 30,
        left: a + 5,
        border: "1px solid #ddd",
        padding: "2px 5px",
        "background-color": "#eee",
        opacity: 1
    }).appendTo("body").fadeIn(300)
}