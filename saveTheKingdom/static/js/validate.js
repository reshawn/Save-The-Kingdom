var form = document.querySelector('#f');

var comment = form.querySelector('#cmt');
var nickname = form.querySelector('#nickname');




form.onsubmit = function submitForm(event){
    event.preventDefault();
    var nam = nickname.value;
    var comm = comment.value;

    if (nam.length===0) {
        document.getElementById("err").innerHTML="Nickname must be entered";
        return false;
    }
    if (comm.length===0) {
        document.getElementById("err1").innerHTML="Please enter a quote/story";
        return false;
    }

    form.submit();
    
    // var data = new FormData(form);
    // fetch('/mission/saveWanderer/',{
    //     credentials:'include',
    //     method:'POST',
    //     body: data
    // })
    // .then(response => {
    //     window.location = '/myWanderers/';

    // })
    window.location = '/myWanderers/';
    return false;
}
