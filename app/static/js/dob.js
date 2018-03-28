$(document).ready(function(){
    var select = $("#DOB");
    for(var i = 2016; i >=1940; i--){
        select.append(`<option value="${i}">${i}</option>`);
    }
});