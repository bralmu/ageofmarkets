const URL_WORLD_MAP = "http://127.0.0.1:5000/worldmap/";
const URL_WORLD_PLAYERS = "http://127.0.0.1:5000/worldplayers/";

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");


$.get(URL_WORLD_MAP, function(data, status){
    if (status == "success") {
        drawWorldMap(data);
    }});


$.get(URL_WORLD_PLAYERS, function(data, status){
    if (status == "success") {
        drawWorldPlayers(data);
    }});


function drawWorldPlayers(retrieved_data) {
    var color, center_x, center_y, radius, start_angle, end_angle;
    color = "white";
    radius = 10;
    start_angle = 0;
    end_angle = 2 * Math.PI    
    for (i in retrieved_data) {
        ctx.beginPath();
        center_x = retrieved_data[i][1] * 50 + 25;
        center_y = retrieved_data[i][2] * 50 + 25;
        ctx.arc(center_x, center_y, radius, start_angle, end_angle)
        ctx.fillStyle = color;    
        ctx.fill();
    }
}


function drawWorldMap(retrieved_data) {
    var color, x, y;
    for (i in retrieved_data) {
        ctx.beginPath();
        switch (retrieved_data[i][0]) {
            case 0:
                color = "brown";
                break;
            case 1:
                color = "blue";
                break;
            default:
                color = "black";
                break;
        }
        x = retrieved_data[i][1] * 50;
        y = retrieved_data[i][2] * 50;
        ctx.fillStyle = color;    
        ctx.fillRect(x, y, 50, 50);        
        ctx.stroke();
    }
}

