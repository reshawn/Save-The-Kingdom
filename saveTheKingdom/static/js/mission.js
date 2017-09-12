function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function(){
    $("#mission").ready(function(){
        let row = Math.floor((Math.random() * 2) + 1);
        let col = Math.floor((Math.random() * 4) + 1);
        var rand_id = "id:"+row+col

        var attempts=1;

        $(".plant").hover(function(){
            $(this).css({'border':'0.1em solid gray', 'border-radius': '1em', 'cursor':'pointer'});
            },function(){
                $(this).css({'border':'none','border-radius':'0','cursor':'default'})
        });

        $(".plant").click(function(){
            if(attempts>0){
                let plant = $(this).attr("id");
                if (plant===rand_id.toString()){
                    //correct potato
                    $(this).css('background-image','url("/static/images/evil_potato.png")');
                    $("#title").text("You did it!");
                    //request session variable status change to hero 
                    $.ajax({
                        type:"POST",
                        url:"setStatusHero/",
                    });
                }
                else {
                    $(this).css({'background-image':'url("/static/images/good_potato.png")'});
                    $(".plant").hover(function(){
                        $(this).css({'border':'none','border-radius':'0','cursor':'not-allowed'});
                        },function(){
                            $(this).css({'border':'none','border-radius':'0','cursor':'default'})
                    });
                    $(".plant").css({'cursor':'not-allowed'});
                    $("#title").text("Wrong potato!");
                }
                attempts --;
            }
            
        });
            
    });
});