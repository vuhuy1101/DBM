
var q4 = "";
var q5 = "";
var q6 = "";
var q7 = "";
var q = "";
var q3 = "";
$(document).ready(function(){
  var q1 = "";
  var q2 = "";
  var temp1 = "";
  var temp2 = "";
  
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
    
    $("select").click(function(){
       q3 = $(this).find('option:selected').attr('value');
    });
    
   /* $('#time_box').click(function(){
      $('#time_box').toggle(this.checked);
      q3 = $('#time_box').val();
    });
    $('#product_box').click(function(){
      $('#product_box').toggle(this.checked);
      q3 = $('#product_box').val();
    });
    */
    
    

    q = q1 + q2 + q3;
  });  
  
  $('#store_box').click(function(){
    $('#store_box').toggle(this.checked);
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
    
    if($("#store_box").is(':checked')){
      //alert($('#_store').val());
      q += ("&conceptStore=" + $('#_store').val());
     }
    
    if($("#product_box").is(':checked')){
      if($('select').attr('name') == 'productAttr'){
        //alert($('#_product').val());
        q += ("&conceptProduct=" + $('#_product').val());
      }
     }
    

    if($("#time_box").is(':checked')){
      if($('select').attr('name') == 'timeAttr'){
        //alert($('#_time').val());
        q += ("&conceptTime=" + $('#_time').val());
      }
     }
    
    
   
    
    
    if($("#timeAttr0").val() != "")
      q4 = "&val0=" + $("#timeAttr0").val();
    if($("#productAttr0").val() != "")
      q4 = "&val0=" + $("#productAttr0").val();
    if($("#storeAttr0").val() != "")
      q4 = "&val0=" + $("#storeAttr0").val();   
    
    //time = 1,2 ; product = 3,4 ; store = 5,6
    if($("#timeAttr1").val() != "" && $("#timeAttr2").val() != "")
      q5 = "&val1=" + $("#timeAttr1").val() + "&val2=" + $("#timeAttr2").val();
    if($("#productAttr1").val() != "" && $("#productAttr2").val() != "")
      q6 = "&val3=" + $("#productAttr1").val() + "&val4=" + $("#productAttr2").val();
    if($("#storeAttr1").val() != "" && $("#storeAttr2").val() != "")
      q7 = "&val5=" + $("#storeAttr1").val() + "&val6=" + $("#storeAttr2").val();
      
    
    q += (q4 + q5 + q6 + q7);
    
        
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