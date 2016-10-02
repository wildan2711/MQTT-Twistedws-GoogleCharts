$(document).ready(function() {
    // create websocket
    if (! ("WebSocket" in window)) WebSocket = MozWebSocket; // firefox
    var socket = new WebSocket("ws://localhost:9000");
    var plant =[];
    // open the socket
    var graphs = {
        temp: {
            data: [],
            options: {}
        }
    };
    google.charts.load('current', {'packages':['corechart']});
    function drawChart(){
        var headers = ["Seconds"];
        var contents = [[]];
        for (var i=1; i <= plant.length; i++){
            headers[i] = plant[i-1].name;
        }
        
        for (var i=0; i < 10; i++){
            contents[i] = [];
            contents[i][0] = i;
            for (var j=1; j <= plant.length; j++){
                contents[i][j] = plant[j-1].temp[i];
            }
        }

        console.log(JSON.stringify(contents));
		
        graphs.temp.data = new google.visualization.DataTable();
        graphs.temp.data.addColumn('number','Seconds');
		
        for (var i=0; i < plant.length; i++){
            graphs.temp.data.addColumn('number', plant[i].name);
        }
		
        graphs.temp.data.addRows(contents);
        graphs.temp.options = {
            title: 'Temperature (Celsius)',
            legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(graphs.temp.data, graphs.temp.options);
    }

    socket.onopen = function(event) {
        socket.send('connected\n');

    // show server response
        socket.onmessage = function(e) {
            $("#output").text(e.data);
            plant = JSON.parse(e.data);
            google.charts.setOnLoadCallback(drawChart);


        };

    }
});