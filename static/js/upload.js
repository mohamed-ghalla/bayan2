//var x = document.getElementById("upload_sheet").addEventListener("click", uploadSheet.bind(this), false);
//function uploadSheet(element) {
//  };
document.addEventListener('click',(e) =>
{
	id = e.target.id.split("_");
	if ( id[0] == "upload" && id[1] == "sheet"){
		$.ajax({
			type:'GET',
			url:`/update_vendor_products/`,
			data:{'VEND_CODE':id[2]},
			success:function (response){
				$('#exampleModal').modal({
					backdrop: 'static',
					keyboard: false
				});
				$("#data_form").html(response);
			},
		});
	}
	else if (id[0] == "upload" && id[1] == "all"){
    		$.ajax({
			type: 'GET',
			url: `/update_all_products/`,
			data: {},
			success: function (response) {
		        	$('#allProductModal').modal({
		        		backdrop: 'static',
				        keyboard: false
		        	});
        			$("#products_data_form").html(response);
			},
		});
	}
	else if(id[0] == "upload" && id[1] == "chique"){
    		$.ajax({
			type: 'GET',
			url: `/upload_chique/`,
			data: { 'vendor_id': id[2] },
			success: function (response) {
				$('#chiqueModal').modal({
					backdrop: 'static',
					keyboard: false
			        });
			        $("#chique_data_form").html(response);
	      		},
    		});

	}
	else if(id[0] =="upload" && id[1] == "bill"){
    		$.ajax({
			type: 'GET',
			url: `/upload_bill/`,
			data: {'VEND_CODE': id[2]},
			success: function (response) {
				$('#BillModal').modal({
					backdrop: 'static',
					keyboard: false
			        });
				$("#bill_data_form").html(response);
			},
		});
	}
	else if(id[0] =="upload" && id[1] == "order"){
	      $.ajax({
        		type: 'GET',
		        url: `/upload_conf_order/`,
		        data: { 'order_no': id[2] },
		        success: function (response) {
			        $("#data_form").html(response);
			        $('#exampleModal').modal({ backdrop: 'static', keyboard: false });
			//          $('#exampleModal').modal();
		        },
		 });
	 }
});	
  $("#bill_form").on('submit', function (e) {
    $("#chique_spinner").show();
    $("#chique_submit_btn").hide();
    $("#chique_cancel_btn").hide();
  });

$("#upload_form").on('submit', function (e){
  $("#products_spinner").show();
  $("#products_cancel").hide();
  $("#products_submit").hide();
});

$("#all_products_form").on('submit', function (e){
  $("#allProducts_spinner").show();
  $("#submit_button").hide();
  $("#cancel_button").hide();
});

$("#chique_form").on('submit', function (e){
  $("#chique_spinner").show();
  $("#chique_submit_btn").hide();
  $("#chique_cancel_btn").hide();
});
$("#my_form").on('submit', function (e){
  $("#sales_order_spinner").show();
  $("#sales_order_save").hide();
});
