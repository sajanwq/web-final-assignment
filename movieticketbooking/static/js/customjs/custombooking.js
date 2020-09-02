$(document).ready(function(){
    //hiding error message by default
    $('#err_msg_email').hide();
    $('#err_msg_movie').hide();
    $('err_msg_tickets').hide();
    $('err_msg_name').hide();

// declaring boolean value true by default
     var tickets_errs = true;
     var email_errs = true;
     var movie_errs = true;
     var name_errs = true;
    
 // calling function of email
    $('#nooftickets').keyup(function(){
        checkfor_tickets();
    });
// calling functio of movie
    $('#emailpart').keyup(function(){
        checkfor_email();
    });
// calling function of tickets
    $('#moviepart').keyup(function(){
        checkfor_movie();
    });
 // calling function of name
$('#namepart').keyup(function(){
    checkfor_name();
});

function checkfor_tickets(){
 var tickets_val =$('#nooftickets').val();
 if(tickets_val.length == ""){
    $('#err_msg_tickets').show();
    $('#err_msg_tickets').html("**Field cannot be empty**");
    $('#err_msg_tickets').focus();
    $('#err_msg_tickets').css('color','red');
    tickets_errs = false;
    return false;

 }if(tickets_val <=5 ){
    $('#err_msg_tickets').show();
    $('#err_msg_tickets').html("**please enter value greate than 4**");
    $('#err_msg_tickets').focus();
    $('#err_msg_tickets').css('color','red');
    tickets_errs =false;
    return false;
 }else{
    $('#err_msg_tickets').hide();
     return true;
 };

};

// creating function for email
function checkfor_email(){
    var emailvalues =$('#emailpart').val();
    if(emailvalues.length == ""){
       $('#err_msg_email').show();
       $('#err_msg_email').html("**Field cannot be empty**");
       $('#err_msg_email').focus();
       $('#err_msg_email').css('color','red');
       email_errs = false;
       return false;
   
    }else{
       $('#err_msg_email').hide();
        return true;
    };
   
   };

   // creating function for moviepart
function checkfor_movie(){
    var movievalues =$('#moviepart').val();
    if(movievalues.length == ""){
       $('#err_msg_movie').show();
       $('#err_msg_movie').html("**Field cannot be empty**");
       $('#err_msg_movie').focus();
       $('#err_msg_movie').css('color','red');
       movie_errs = false;
       return false;
   
    }else{
       $('#err_msg_movie').hide();
        return true;
    };
};

   // creating function for namepart
   function checkfor_name(){
    var namevalues =$('#namepart').val();
    if(namevalues.length == ""){
       $('#err_msg_name').show();
       $('#err_msg_name').html("**Field cannot be empty**");
       $('#err_msg_name').focus();
       $('#err_msg_name').css('color','red');
       name_errs = false;
       return false;

    }else{
       $('#err_msg_name').hide();
        return true;
    };
};

// validating button
$('#bookingbtn').click(()=>{
    tickets_errs = true;
    email_errs = true;
    movie_errs = true;
    name_errs =true;
    checkfor_tickets();
    checkfor_email();
    checkfor_movie();
    checkfor_name();
    if ((tickets_errs == true) && (email_errs == true) && (movie_errs == true) && (name_errs == true)){
        alert("Booked successfully");
        return true;

    }else{
        alert("Cannot be booked Please check your entry");
        return false;
    }
});

   
  
})