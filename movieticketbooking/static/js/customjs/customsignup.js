// validating   signup form
$(document).ready(function(){
    
    $('#eml_err_msg').hide();
    $('#pass_err_msg').hide();
    $('#repass_err_msg').hide();


    var err_email= true;
    var err_password = true;
    var err_confirmpassword= true;
    
// calling password for email
    $('#signupemail').keyup(function(){
        email_check();
    });
// calling function for password
    $('#signuppassword').keyup(function(){
        password_check();
    });
    //calling function for confirm password
    $('#signupconfirmpassword').keyup(function(){
        repassword_check();
    });
//creating function for email
    function email_check(){
        var eml_value=$('#signupemail').val();
        if(eml_value.length == ""){
           $('#eml_err_msg').show();
           $('#eml_err_msg').html("** please fill up the text field**");
           $('#eml_err_msg').focus();
           $('#eml_err_msg').css('color','red');
            err_email= false;
            return false;

        
        }if((eml_value.length <= 4 ) || (eml_value.length >= 30) ){
        $('#eml_err_msg').show();
        $('#eml_err_msg').html("**please enter the character from 5-29 in the field**");
        $('#eml_err_msg').focus();
        $('#eml_err_msg').css('color','red');
        err_email= false;
        return false;

    }else{
        $('#eml_err_msg').hide();
        return true;
    }
};

// creating function for password

function password_check(){
    var pass_value = $('#signuppassword').val();
    if(pass_value.length == ""){
        $('#pass_err_msg').show();
        $('#pass_err_msg').html("** please fill up the text field**");
        $('#pass_err_msg').focus();
        $('#pass_err_msg').css('color','red');
        err_password= false;
        return false;

    
    }if((pass_value.length <= 4) || (pass_value.length > 12) ){
    $('#pass_err_msg').show();
    $('#pass_err_msg').html("**please enter the character from 5-12 in the field**");
    $('#pass_err_msg').focus();
    $('#pass_err_msg').css('color','red');
    err_password= false;
    return false;

}else{
    $('#pass_err_msg').hide();
    return true;
}
};

//creating function for repassword check
function repassword_check(){
    var pass_value = $('#signuppassword').val();
    var repass_value = $('#signupconfirmpassword').val();
    if(repass_value.length == ""){
        $('#repass_err_msg').show();
        $('#repass_err_msg').html("** please fill up the text field**");
        $('#repass_err_msg').focus();
        $('#repass_err_msg').css('color','red');
        err_confirmpassword = false;
        return false;

    
    }if(repass_value.length !== pass_value.length){
    $('#repass_err_msg').show();
    $('#repass_err_msg').html("**please re-enter your password correctly**");
    $('#repass_err_msg').focus();
    $('#repass_err_msg').css('color','red');
    err_confirmpassword= false;
    return false;

}else{
    $('#repass_err_msg').hide();
    return true;
}
};

/// for signup button
$('#signupbutton').click(function(){
    err_email = true;
    err_password = true;
    err_confirmpassword = true;
    email_check();
    password_check();
    repassword_check();
    if ((err_email == true) && (err_password == true) && (err_confirmpassword == true)){
        alert("signed up successfully");
        return true;
    }else{
        alert("please insert data coorectly");
        return false;
    }
});



})