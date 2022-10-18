$(document).ready(function(){
  var message		= document.getElementById("print_header").innerHTML;
  var title		= document.getElementById("title_id").innerHTML;
  var print_columns	= document.getElementById("print_columns").innerHTML;
  var print_rows		= document.getElementById("print_rows").innerHTML;
  var select_columns	= document.getElementById("select_columns").innerHTML;
  var next		= document.getElementById("next").innerHTML;
  var previous		= document.getElementById("previous").innerHTML;
  var search		= document.getElementById("search").innerHTML ;

  var table = $('#vendors_table').DataTable({
    responsive: true,
    dom: 'Bfrtip',
    buttons: [{
      text: print_columns,
      extend: 'print',
      title:title,
      messageTop: message,
      customize: function (win) {
      },
      exportOptions: {
        columns: ':visible',
        columns: [ 0, 1, 2, 3, 4],
        modifier: {
          selected: null
        }
      }
    },
    'colvis',
    {
      extend: 'print',
      text: print_rows,
      title:title,
      messageTop:message,
      exportOptions: {
        columns: ':visible',
        columns: [ 0, 1, 2, 3, 4],
        modifier: {
        //            selected: null
        }
      }
    }],
    language: {
      buttons: {
        colvis: select_columns,
      }
    },
    "oLanguage": {
      "sSearch": search ,
      "sEmptyTable": "",
      "oPaginate": {
        "sPrevious": previous, // This is the link to the previous page
        "sNext": next, // This is the link to the next page
      }
    },
    select: true,
    columnDefs: [{
      extend: 'print',
      visible: false,
      //        targets: -1
    }]
  }); new $.fn.dataTable.FixedHeader(table);
});
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////