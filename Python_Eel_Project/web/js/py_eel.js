function py_video() {
        eel.video_feed()()
    }
function py_video_stop() {
    // $( "#bg" ).replaceWith( '<img id="bg" src="" alt="">' );
    eel.video_stop()()
}
function GetFilterValue(cond) {
    eel.filter(cond)()
}

eel.expose(updateImageSrc);
function updateImageSrc(val) {
    let elem = document.getElementById('bg');
    elem.src = "data:image/jpeg;base64," + val
}
function py_login(data) {
    eel.login(data)()
}


    