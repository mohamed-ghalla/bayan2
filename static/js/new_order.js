
  var $TABLE = $("#table");
  var $BTN = $('#export-btn');
  var $EXPORT = $('#export');
  var serial = 1 ;
  // Material Select Initialization
  $(document).ready(function() {
    $('.select_item').select2({
      //  placeholder: '',
      allowClear: true
    });
    $('.mdb-select').materialSelect();
  });

  $('#my_form').submit(function(){
    var yy = convertTableToJson();
    document.getElementById("table_data").value = yy;
    alert("Are You Sure ?");
    return true;
  });
  // ############################################################

  $('.table-add').click(function () {
    serial++;
    $TABLE.find('table').append(trString(serial));

    var lastTr = $TABLE.find('table tr').last();
    $('.select_item').select2({
      //  placeholder: '',
      allowClear: true
    });
    lastTr.find('.button_remove').click(removeFunc);
    lastTr.find('.mdb-select').materialSelect();
  });

// ############################################################

  $('.button_remove').click(removeFunc);
  function removeFunc () {
    $(this).parents('tr').detach();
    //serial--;
  };

  // A few jQuery helpers for exporting only
  jQuery.fn.pop = [].pop;
  jQuery.fn.shift = [].shift;
// 

// $BTN.click(function () {
var convertTableToJson = function(){
var $rows = $TABLE.find('tr:not(:hidden)');
var headers = [];
var data = [];
// Get the headers (add special header logic here)

$($rows.shift()).find('th:not(:empty)').each(function () {
//headers.push($(this).text().toLowerCase());
//	alert(headers);
});
headers = ['Serial', 'Item', 'Code', 'Desc', 'Count', 'Quantity', 'Price', 'Total', 'Remove'];

// Turn all existing rows into a loopable array
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

  var trString = function(serial){
    var templateString = `
	<tr>
	<td class="col_td serial" contenteditable="false">${serial}</td>
	<td class="select_td" contenteditable="false">
	<select class="select_item mdb-select form-control" onchange="selectFunction(this)" required>
	<option value="" disabled selected>{% trans 'Please Select Item' %}</option>
	{% for i in items %}
	  <option value="{{i.PACK_ID}}-{{i.UNIT_DESC}}-{{i.NO_OF_ITEMS}}-{{i.PURCH_PRICE}}-${serial}" >{{i.ARABIC_NAME}} ________ {{i.UNIT_DESC}}</option>
	  {% endfor %}
	</select>
	<div class="invalid-feedback">
	  {% trans "Please select a valid Item." %}
	</div>
	</td>
	<td class="col_td" contenteditable="false" id="code_${serial}"></td>
	<td class="col_td" contenteditable="false" id="desc_${serial}"></td>
	<td class="col_td" contenteditable="false" id="no_item_${serial}"></td>
	<td class="col_td" contenteditable="false" id="" >
	  {% render_field form.quantity|attr:"id:quantity_${serial}" onchange="total_function(this)"  class+="form-control quantity_in" %}
	</td>
	<td class="col_td" contenteditable="false" id="price_${serial}"></td>
	<td class="col_td" contenteditable="false" id="total_${serial}" required></td>
	<td class="col_td">
	  <a type="button" class="button_remove btn btn-danger btn-rounded btn-sm my-0">{% trans "Remove" %}</a></span>
	</td>
	</tr>`;
    return templateString ;
  };
/////////////////////////////////////////////////////////////////////////////////////////////
  var selectFunction = function(element){
    alert("changed");
    $(`#code_${serial}`).val($(element).find("option:selected").val());
    var str = $(element).find("option:selected").val();
    var res = str.split("-");
    var x = res[4];
    $(`#code_${x}`).text(res[0]);
    $(`#desc_${x}`).text(res[1]);
    $(`#no_item_${x}`).text(res[2]);
    $(`#price_${x}`).text(res[3]);
    $(`#total_${x}`).text((Number($('#price_'+x).text()) * Number($('#quantity_'+x).val())).toPrecision(4));
  };

  var total_function = function(element){
    //$('#total_'+serial).text(Number($('#price_'+serial).text()) * Number($('#quantity_'+serial).text()));
    var str = $(element).attr('id');
    var x = str.split("_");
    var y = x[1];
    $('#total_'+y).text((Number($('#price_'+y).text()) * Number($('#quantity_'+y).val())).toPrecision(4));
  };

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() == false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

