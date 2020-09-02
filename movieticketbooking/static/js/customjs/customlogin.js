//--------------validation for login form--------------------

$(document).ready(function(){
    //hiding  message section span by default in the form
    $('#err_msgemail').hide();
    $('#err_msgpassword').hide();

    var email_err = true;
    var password_err = true;

    //calling function for email section
    $('#lgn_input_1').keyup(function(){
     email_check();
    });

    //calling function for password section
    $('#lgn_input_2').keyup(function(){
        password_check() 
    });


    
//creating function for email text box section
    function email_check(){
        var eml = $('#lgn_input_1').val();
        if(eml.length == ""){
        $('#err_msgemail').show();
        $('#err_msgemail').html("**Please fill the text field**");
        $('#err_msgemail').focus();
        $('#err_msgemail').css('color','red');
         email_err = false;
         return false;
       }if( (eml.length <= 3) || (eml.length >= 30) ){
           $('#err_msgemail').show();
           $('#err_msgemail').html("**please enter the character from 4-14")
           $('#err_msgemail').focus();
           $('#err_msgemail').css('color','red');
           email_err = false;
           return false;
       }else{
          $('#err_msgemail').hide();
          return true 
       }

    };

//creating function for password section..
function password_check(){
    var pswd = $('#lgn_input_2').val();
    if(pswd.length == ""){
        $('#err_msgpassword').show();
        $('#err_msgpassword').html("**Please input your password**");
        $('#err_msgpassword').focus();
        $('#err_msgpassword').css('color','red');
        password_err = false;
        return false;
    }if( (pswd.length <= 2) || (pswd.length >= 20) ){
        $('#err_msgpassword').show();
        $('#err_msgpassword').html("**please input the character from 2-20**");
        $('#err_msgpassword').focus();
        $('#err_msgpassword').css('color','red');
        password_err = false;
        return false;
    }else{
        $('#err_msgpassword').hide();
        return true
    }

};

//creating function for login button..;
$('#lgn_btn').click(function(){ 
    email_err = true;
    password_err = true;
    email_check();
    password_check();
if( (email_err == true ) && (password_err == true) ){
    alert("logged in successfully")
   return true;
}
else{
    alert("please re-enter data  correctly")
    return false;
}
})
});





