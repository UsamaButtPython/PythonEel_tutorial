
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
    // alert("Hacked")
    // var formData = {
    //     email: $("#email").val(),
    //     pass: $("#pass").val(),
    //   };
    // console.log(formData)
    email= $("#email").val()
    pass= $("#pass").val()
    eel.login(email,pass)().then((r) => {
        console.log(r);
        // if(r==true){
        //     window.location.replace("index.html")
        // }
        // else{
        //     alert("Nikal shabash")
        // }
    });
    
    // py_login(formData)
    // window.location.replace("index.html")
});    
