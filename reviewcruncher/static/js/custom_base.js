$(document).ready(function(){
    //load_data();

    function load_data(query){
     var text = query;
     $.ajax({
       type: "GET",
       url: '/search_home_product_list',
       dataType: "json",
     // data:text,
         data: {query: text},
       success: function(response){
         setResponse(response)
                   //console.log(response);
       }
     })
    }

    $('#search_text').keyup(function(){
     var search = $(this).val();

     if(search != '')
     {
     //console.log(search)
      load_data(search);
     }
     else
     {
     load_data();
     }
    });
   });
   function setResponse(val) {
     var n=val.length
     var x=1;
     console.log(val)
     if (n==1){
       document.getElementById("count"+(x)).innerHTML=val[0]
     }
     else{
       for (i = 1; i <n; i+=2) {
         // var openDropdown =val[i];
         // console.log(i+1)
         document.getElementById("count"+(x)).innerHTML=val[i]
         document.getElementById("count"+(x)).style.display = "block";
         document.getElementById("count"+(x)).href = "http://127.0.0.1:8080/product_dashboard/"+val[i-1];

         x=x+1;
         // document.getElementById("myDropdown").classList.toggle("show");
       }
     }
     document.getElementById("myDropdown").classList.toggle("show");
     for (i = x; i <=5; i++) {
       document.getElementById("count"+(i+1)).style.display = "none";
     }

   }