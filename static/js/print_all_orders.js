$(document).ready(function(){
  var message           = document.getElementById("print_table").innerHTML;
  var title             = document.getElementById("title_id").innerHTML;
  var print_columns     = document.getElementById("print_columns").innerHTML;
  var print_rows        = document.getElementById("print_rows").innerHTML;
  var select_columns    = document.getElementById("select_columns").innerHTML;
  var next              = document.getElementById("next").innerHTML;
  var previous          = document.getElementById("previous").innerHTML;
  var search            = document.getElementById("search").innerHTML ;

//  $('.dataTables_length').addClass('bs-select');
    var table = $('#orders_table').DataTable({
      responsive: true,
      dom: 'Bfrtip',
      buttons: [{
        text: print_columns,
        extend: 'print',
        title: title,
        messageTop:message,
        exportOptions: {
          columns: ':visible',
          modifier: {
            selected: null
          }
        }
      },
        'colvis',
      {
        text: print_rows,
        extend: 'print',
        title:title,

        messageTop:message,
        exportOptions: {
          columns: ':visible',
          columns: [ 0, 1, 2, 3, 4, 5],
          modifier: {
//            selected: null
          }
        }	      
      }],
      language: {
        buttons: {
          colvis: select_columns
        }
      },
      "oLanguage": {
        "sSearch": search,
	"sEmptyTable":`{% trans 'No data available in table' %}`,
        "oPaginate": {
          "sPrevious": previous, // This is the link to the previous page
          "sNext": next, // This is the link to the next page
        }
      },
      select: true,
      columnDefs: [{
//        targets: -1,
        visible: false
      }]
    }); new $.fn.dataTable.FixedHeader(table);
  });
