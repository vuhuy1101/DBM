
var q4 = "";
$(document).ready(function(){
  var q = "";
  var q1 = "";
  var q2 = "";
  var q3 = "";
  
	// $("#tester").click(function(){
	// 	$("#time_text").hide();
	// });

	$(".dropdown-menu li a").click(function(){
		$(this).parents(".btn-group").find('.selection').text($(this).text());
		$(this).parents(".btn-group").find('.selection').val($(this).text());
		$(this).parents(".btn-group").find('.dimensionText').val($(this).text());
		$(this).parents(".btn-group").find('.dropdownValue').val($(this).attr('value'));

    q += $(this).parents(".btn-group").find('.dropdownValue').attr('name') + "=";
    //alert($(this).parents(".btn-group").find('.dropdownValue').attr('name'));
    
    q += $(this).parents(".btn-group").find('.dropdownValue').val();
    //alert($(this).parents(".btn-group").find('.dropdownValue').val());
    global_list.push($(this).parents(".btn-group").find('.dropdownValue').val());
       
    q += "&";
	});


  $("input").click(function(){
    if($(this).attr('name') == "action"){
      q1 = ("action=" + $(this).attr('value') + "&");
    }
    if($(this).attr('name') == "dimension"){
      if($(this).attr('value') == "Product"){
        q2 = "conceptProduct=";
      }
      else if($(this).attr('value') == "Store"){
        q2 = "conceptStore=";
      }
      else if($(this).attr('value') == "Time"){
        q2 = "conceptTime=";
      }
    }
    
    if($(this).attr('name') == "timeAttr"){
      q4 = "&val0=" + $(this).val();
     }
    else if($(this).attr('name') == "productAttr"){
       q4 = "&val0=" + $(this).val();
    }
    else if($(this).attr('name') == "storeAttr"){
       q4 = "&val0=" + $(this).val();
    }
    
    
    $("select").click(function(){
       q3 = $(this).find('option:selected').attr('value');
    });
    
    q = q1 + q2 + q3 + q4;
  });
  
 

	 // $(function(){
        // Get json response
        //var stringJsonObject;

        //GENERIC JAVASCRIPT CODE FOR ANY TABLE
        $('#customSubmit').click(function(){
          $("#loadops").load("/loadOperations");
          $.getScript('/../static/js/script.js');
          $.getJSON('/getResults', q, function (ret) {
            //alert('JSON got: ' + JSON.stringify(ret));
             var stringJsonObject = JSON.stringify(ret);


             //this section generates table header

             //all json objects in an array
             var jsonObjectArray = JSON.parse(stringJsonObject);
			 // alert('JSON' + obj[0].total_sales);

			 //one json object to generate the header
			 var oneObjectForHeader = jsonObjectArray[1];
			 var tableHeader = "<tr>";
			 $.each(oneObjectForHeader, function(key, value){
			 	tableHeader+= "<th>"+key+"</th>";			 	
			 });
			 tableHeader+="</tr>";
			 $('#olapResultTableHeader>tr').remove();
			 $('#olapResultTableHeader').append(tableHeader);

			 //this section generates table data values
			 var tableBody;
			 $("#olapResultTableBody>tr").remove()
			 $.each(jsonObjectArray, function(idx, obj){
			 	tableBody="<tr>"
			 	$.each(obj, function(key, value){
			 		console.log(key + ":" + value);
			 		tableBody+="<td>"+value+"</td>";
			 	});
			 	tableBody+="</tr>";
			 	$("#olapResultTableBody").append(tableBody);
			 });
			 });
        });
 


   $('#submit').click(function(){
    alert(q);
    $.getJSON('/getResults', q, function (ret) {
        
        //alert('JSON got: ' + JSON.stringify(ret));
         var stringJsonObject = JSON.stringify(ret);


         //this section generates table header

         //all json objects in an array
         var jsonObjectArray = JSON.parse(stringJsonObject);
    			 // alert('JSON' + obj[0].total_sales);

    			 //one json object to generate the header
    			 var oneObjectForHeader = jsonObjectArray[1];
    			 var tableHeader = "<tr>";
    			 $.each(oneObjectForHeader, function(key, value){
    			 	tableHeader+= "<th>"+key+"</th>";			 	
    			 });  
          tableHeader+="</tr>";
    			 $('#olapResultTableHeader>tr').remove();
    			 $('#olapResultTableHeader').append(tableHeader);

    			 //this section generates table data values
    			 var tableBody;
    			 $("#olapResultTableBody>tr").remove()
    			 $.each(jsonObjectArray, function(idx, obj){
    			 	tableBody="<tr>"
    			 	$.each(obj, function(key, value){
    			 		console.log(key + ":" + value);
    			 		tableBody+="<td>"+value+"</td>";
    			 	});
    			 	tableBody+="</tr>";
    			 	$("#olapResultTableBody").append(tableBody);
    			 });
    });
  });
      

});