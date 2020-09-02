$(document).ready(function(){

    var srch_errs = true
   
    $('#srchpart').keyup(function(){
        search_test();
    });

// creting function for search test
    function search_test(){
        var srch_value =  $('#srchpart').val(); 
        if(srch_value.length ==""){
            $('#srchpart').css('border','2px solid red');
            srch_errs= false;
            return false;

        }else{
            $('#srchpart').css('border','1px solid #ced4da');
            return true;

        }

    };
    //validating button
        
   $('#srchbtn').click(()=>{
       srch_errs = true;
       search_test();
       if(srch_errs == true){
           return true;
       }else{
           return false;
       }


   })

})