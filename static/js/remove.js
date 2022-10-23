document.addEventListener('click',(e) =>
{
        id = e.target.id.split("_");
        if ( id[0] == "remove" && id[1] == "order"){
		url = "/delete_order/"+id[2]+"/";
		$.ajax({
			type: "POST",
			url: url,
			data: { csrfmiddlewaretoken: id[3] },
			success: function (response) {
				alert(response);
			        location.reload();
			},
		});
  	}
	else if(id[0] == "delete" && id[1] == "order"){
	      $.ajax({
        	type: "POST",
	        url: "/delete_order/"+id[2]+"/",
        	data: { csrfmiddlewaretoken: id[3] },
	        success: function (response) {
		        window.location = "https://bayancoopq8.com/list_orders/"+id[4];
	        },
	      });
	}
	else if(id[0] == "delete" && id[1] == "orders"){
		alert(id);
		alert(id[2]);
//		var removeFunc = function (element) {
			var order_date = $('#datepicker').val();
		alert(order_date);
			$.ajax({
			      type: "POST",
			      url: '/delete_old_orders/'+order_date+'/',
			      data: { csrfmiddlewaretoken: id[2] },
			      success: function (response) {
			        alert(response);
			        location.reload();
			      },
		    });
//	 	 };
	}
	
});
$('#datepicker').datepicker({
  uiLibrary: 'bootstrap4'
});
