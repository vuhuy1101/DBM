var productD = ['description', 'brand', 'subcategory', 'category', 'department'];
var storeD = ['store_number','street_address','city','county','state','zip','district','region'];
var timeD = ['date', 'day_of_week', 'day_number_in_month', 'month', 'quarter', 'fiscal_period', 'year'];
	
function add_dim(name){
	//alert(global_list);
	var list = document.getElementsByName(name)[0].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i]){
				pos = j;
			}
		}
		if(pos > -1){  
			list[pos].disabled = true;
		}
	}
}
	
function remove_dim(name){
	var list = document.getElementsByName(name)[1].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;
	

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i]){
				pos = j;
			}
		}
		if(pos > -1){  
			for(i = 0; i < list.length; i++){
				if(pos != i)
					list[i].disabled = true;
			}
			
		}
	}
}
	
	
function roll_up(name){
	var list = document.getElementsByName(name)[2].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;
	

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i])
				pos = j;
		}
		if(pos > -1){  
			while(pos > -1){
				list[pos].disabled = true;
				pos--;
			}
		}
	}
}
	
function drill_down(name){
	var list = document.getElementsByName(name)[3].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;
	

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i]){
				pos = j;
			}
		}
		if(pos > -1){  
			while(pos < list.length){
				list[pos].disabled = true;
				pos++;
			}
		}
	}
}
	
function slice(name){
	var list = document.getElementsByName(name)[4].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;
	

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i]){
				pos = j;
			}
		}
		if(pos > -1){  
			for(i = 0; i < list.length; i++){
				if(pos != i)
					list[i].disabled = true;
			}
			
		}
	}
}

function dice(name){
	var list = document.getElementsByName(name)[5].getElementsByTagName("option");
	var i,j;
	var thArray = [];
	var pos = -1;
	

	//get the value from the table headers
	$('#olapResultTable > thead > tr > th').each(function(){
		thArray.push($(this).text())
	})
	
	//disable that option
	for(i = 0; i < thArray.length;i++){
		for(j = 0; j < list.length; j++){
			if(list[j].value == thArray[i]){
				pos = j;
			}
		}
		if(pos > -1){  
			for(i = 0; i < list.length; i++){
				if(pos != i)
					list[i].disabled = true;
			}
			
		}
	}
}
	
	
function update(c1, c2, c3, index){
	document.getElementsByName(c1)[index].style.display = "block";
	var class2 = document.getElementsByName(c2);
	var class3 = document.getElementsByName(c3);
	
	for(var i = 0; i < class2.length;i++)
		class2[i].style.display = "none";
		
	for(var i = 0; i < class3.length;i++)
		class3[i].style.display = "none";
		
	if(index == 4){
		document.getElementsByName(c1+"0")[0].style.display = "block";
		document.getElementsByName(c2+"0")[0].style.display = "none";
		document.getElementsByName(c3+"0")[0].style.display = "none";
	}

	
}
	
function displayOption(){
	if(document.getElementById('addDim').checked == true)
		document.getElementById('addDimOption').style.display = "block";
	else
		document.getElementById('addDimOption').style.display = "none";

	if(document.getElementById('removeDim').checked == true)
		document.getElementById('removeDimOption').style.display = "block";
	else 
		document.getElementById('removeDimOption').style.display = "none";

	if(document.getElementById('rollup').checked == true){
		document.getElementById('rollupOption').style.display = "block";
	}else 
		document.getElementById('rollupOption').style.display = "none";

	if(document.getElementById('drilldown').checked == true)
		document.getElementById('drilldownOption').style.display = "block";
	else 
		document.getElementById('drilldownOption').style.display = "none";

	if(document.getElementById('slice').checked == true)
		document.getElementById('sliceOption').style.display = "block";
	else 
		document.getElementById('sliceOption').style.display = "none";

	if(document.getElementById('dice').checked == true)
		document.getElementById('diceOption').style.display = "block";
	else 
		document.getElementById('diceOption').style.display = "none";
	
}