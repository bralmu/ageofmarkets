const URL = "http://127.0.0.1:5000/";


var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");


$.get(URL, function(data, status){
    if (status == "success") {
        draw_canvas(data);
    }});


function draw_canvas(retrieved_data) {
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

