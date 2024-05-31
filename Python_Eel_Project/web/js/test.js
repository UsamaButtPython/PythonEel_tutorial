
// (function(document, tag) {
//     var scriptTag = document.createElement(tag), // create a script tag
//     firstScriptTag = document.getElementsByTagName(tag)[0]; // find the first script tag in the document
//     scriptTag.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'; // set the source of the script to your script
//     firstScriptTag.parentNode.insertBefore(scriptTag, firstScriptTag); // append the script to the DOM
// }(document, 'script'));

// (function(document, tag) {
//     var scriptTag = document.createElement(tag), // create a script tag
//     firstScriptTag = document.getElementsByTagName(tag)[1]; // find the first script tag in the document
//     scriptTag.src = 'scripts.js'; // set the source of the script to your script
//     firstScriptTag.parentNode.insertBefore(scriptTag, firstScriptTag); // append the script to the DOM
// }(document, 'script'));
// $.getScript("scripts.js", function() {
//     alert("Script loaded but not necessarily executed.");
//  });

$(document).ready(function(){
    // $(".Start").click(function(){
    $(document.body).on('click', '.Start' ,function(){
        py_video();
        $(".Start").addClass("Stop");
        $(".Start").html("Stop feed");
        $(".Start").removeClass("Start");

    });
    $(document.body).on('click', '.Stop' ,function(){
        console.log("first")
        $(".Stop").addClass("Start");
        $(".Stop").html("Start feed");
        $(".Stop").removeClass("Stop");
        py_video_stop();
    });
  });
function logout() {
    console.log("Clicked")
    // $.get('/login.html', function(html) {

    //     console.log(html);
    //     document.body.innerHTML=html


    // });
       window.location.replace("login.html")
}
$("#loginForm").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    // var actionUrl = form.attr('action');
    alert("Hacked")
    window.location.replace("index.html")
});    

