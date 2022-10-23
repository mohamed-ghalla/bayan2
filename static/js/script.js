document.addEventListener('change',(e) =>
{
  id = e.target.id;
  s = e.target.id.split("_");
	select_item(s);
});
function select_item(s){
  if ( s[0] == "select" && s[1] == "item"){
    var str = $("#"+id+" option:selected").val();
    var res = str.split("-");
    var x = s[2];
    $(`#code_${x}`).text(res[0]);
    $(`#desc_${x}`).text(res[1]);
    $(`#no_item_${x}`).text(res[2]);
    $(`#price_${x}`).text(res[3]);
    $(`#total_${x}`).text((Number($('#price_'+x).text()) * Number($('#quantity_'+x).val())).toPrecision(4));
  }
  else if(s[0] == "quantity"){
	$(`#quan_${s[1]}`).val($(`#quantity_${s[1]}`).val());
	var str = $(`#quantity_${s[1]}`).attr('id');
	  alert(str);
	var x = str.split("_");
	var y = x[1];
	$('#total_'+y).text((Number($('#price_'+y).text()) * Number($('#quantity_'+y).val())).toPrecision(4));
  }
}

//  ################ ################  ################  ################  ################  
$('.button_remove').click(removeFunc);
function removeFunc () {
  $(this).parents('tr').detach();
  //serial--;
};
//  ################ ################  ################  ################  ################  
//
//var x = document.getElementById("select_item").addEventListener("change", selectFunction.bind(this),  false);

//function selectFunction(element){
//  var y = document.getElementById("select_item");
//  alert("1");
//  //    $(`#code_${serial}`).val($("#select_item option:selected").val());
//  var str = $("#select_item option:selected").val();
//  var res = str.split("-");
//  var x = res[4];
//  alert("2");
//  $(`#code_${x}`).text(res[0]);
//  $(`#desc_${x}`).text(res[1]);
//  $(`#no_item_${x}`).text(res[2]);
//  $(`#price_${x}`).text(res[3]);
//  $(`#total_${x}`).text((Number($('#price_'+x).text()) * Number($('#quantity_'+x).val())).toPrecision(4));
//}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//document.getElementById("quantity_1").addEventListener("change", totalFunction.bind(this), false);

//function totalFunction(element){
////$('#total_'+serial).text(Number($('#price_'+serial).text()) * Number($('#quantity_'+serial).text()));
//$("#quan_1").val($("#quantity_1").val());
//var str = $("#quantity_1").attr('id');
//var x = str.split("_");
//var y = x[1];
//$('#total_'+y).text((Number($('#price_'+y).text()) * Number($('#quantity_'+y).val())).toPrecision(4));
//}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
var $TABLE = $("#table");
var $BTN = $('#export-btn');
var $EXPORT = $('#export');
var serial = 1 ;
// Material Select Initialization
$(document).ready(function() {
//$('.select_item').select2({
////    placeholder: '',
//    allowClear: true,
//  });
//  $('.mdb-select').materialSelect();
//	alert("ready");
});
///////////////////////////////////////////////////////////////////////////////
$('#my_form').submit(function(){
  var yy = convertTableToJson();
  document.getElementById("table_data").value = yy;
  alert("Are You Sure ?");
  return true;
});
//// ############################################################
//  ################ ################  ################  ################  ################  
//var trString = function(){
//  var templateString = document.getElementById("template_Row").innerHTML;
//  serial++;
//  alert("serial= ", serial);
  
//  return templateString ;
//};
//  ################ ################  ################  ################  ################  

$('.table-add').click(function () {
  serial++;
  var a ="<tr><td class='col_td serial' contenteditable='false'>"+serial+"</td>" ;
  var b ="<td class='select_td' contenteditable='false' id='select_td_"+serial+"'>" ;
  let c =document.getElementById("select_td_1").innerHTML;
  let result = 'id="select_item_'.concat(serial+'"');
  let text = 'id="select_item_1"';
  let c1 = c ;
  let cc = c1.replace(text, result);
  var d ="</td><td class='col_td' contenteditable='false' id='code_"+serial+"'></td>";
  var e ="<td class='col_td' contenteditable='false' id='desc_"+serial+"'></td><td class='col_td' contenteditable='false' id='no_item_"+serial+"'></td>";
  var f ="<td class='col_td' contenteditable='false' id='quan_"+serial+"' value=3 id='quan_td'>";
  var g =document.getElementById("quan_1").innerHTML;
  let g1='id="quantity_1"';
  let g2='id="quantity_'.concat(serial+'"');
  let gg=g.replace(g1,g2);
  var h ="<td class='col_td' contenteditable='false' id='price_"+serial+"'></td><td class='col_td' contenteditable='false' id='total_"+serial+"' required></td><td class='col_td' id='remove_td'>";
  var i =document.getElementById("remove_td").innerHTML+"</td></tr>";
  var my_row = a+b+cc+d+e+f+gg+h+i;
  $TABLE.find('table').append(my_row); //(trString());

  var lastTr = $TABLE.find('table tr').last();
  lastTr.addEventListener("change", (e) =>//, false);
{
  id = e.target.id;
  s = e.target.id.split("_");
	alert(s);
	select_item(s);
});
	alert(lastTr.find('.button_remove'));
  $('.select_item').select2({
    //  placeholder: '',
    allowClear: true
  });
  lastTr.find('.button_remove').click(removeFunc);
//  lastTr.find('.mdb-select').materialSelect();
});  
//  ################ ################  ################  ################  ################  

// A few jQuery helpers for exporting only
  jQuery.fn.pop = [].pop;
  jQuery.fn.shift = [].shift;
//// 

//$BTN.click(function () {
    
  var convertTableToJson = function(){
    var $rows = $TABLE.find('tr:not(:hidden)');
    var headers = [];
    var data = [];
    // Get the headers (add special header logic here)

    $($rows.shift()).find('th:not(:empty)').each(function () {
    //    headers.push($(this).text().toLowerCase());
    });
    headers = ['Serial', 'Item', 'Code', 'Desc', 'Count', 'Quantity', 'Price', 'Total', 'Remove'];

    // Turn all existing rows into a loopable array
//    $rows.slice(1).each(function () {
	  //
    $rows.each(function () {    
      var $td = $(this).find('td');
      var h = {};
      // Use the headers from earlier to name our hash keys
      headers.forEach(function (header, i) {
        if (i == 1){
          h[header] = $td.eq(i).find('option:selected').text().split("________")[0];
        }
        else if (i == 5){
          h[header] = $td.eq(i).find("input").val();
        }
        else {
          h[header] = $td.eq(i).text();
        }
      });
      data.push(h);
    });
    // Output the result
    $EXPORT.text(JSON.stringify(data));
    return JSON.stringify(data);
  };
//});

