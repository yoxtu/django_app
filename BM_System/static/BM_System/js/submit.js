window.onload = function(){
    var form = document.getElementById("form");
    if(form != null){
        form.addEventListener('submit', (evt) => {
            var submit = document.getElementById('submit');
            submit.disabled = true;
        }, false);
    }
}