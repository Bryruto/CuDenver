let id;
let clock;
let is_on;
function set_time()
{
    clock = document.getElementById("timer").innerHTML;
    let hours,min,sec;
    [hours, min, sec]=clock.split(":")
    sec++;
    if (sec == 60)
    {
        sec = 0;
        min++;
        if (min == 60)
        {
            min = 0;
            hours++;
        }
    }
    clock = [hours, min, sec].join(":");
    document.getElementById("timer").innerHTML = clock;
}
function reset()
{
    clock = document.getElementById("timer").innerHTML;
    let hours,min,sec;
    [hours, min, sec]=clock.split(":")
    hours = "00";
    min = "00";
    sec = "00";
    clock = [hours, min, sec].join(":");
    document.getElementById("timer").innerHTML = clock;
}
function on()
{
    if (is_on != true)
    {
    id =setInterval(set_time,1000);
    is_on = true;
    }
}
function off()
{
    is_on = false;
    clearInterval(id);
}

function done(button)
{
    let node = button.parentNode.parentNode;
    node.style.backgroundColor = "green";
    let row = button.closest("tr");
    let text = row.querySelectorAll("input");
    for (let line of text)
    {
        line.style.backgroundColor = "green";
    }
}


