var date = new Date();
console.log(date);

var day = date.getDay();
var hours = date.getHours();
var min = date.getMinutes();
var sec = date.getSeconds();
/*
function ApplyTheme(currentDay, currentHour, currentSecond){
    var bodyClass = $('body').attr("class");
    $('body').removeAttr("class")
    if ((currentHour >=7)&&(currentHour < 18)){
        bodyClass = "light";
    }
    else {
        bodyClass = "dark";
    }
    $('body').addClass(bodyClass);
console.log(currentHour, currentSecond)
}
ApplyTheme(day, hours, sec);
