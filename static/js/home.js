$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
  });
document.addEventListener('click',(e) =>
{
        id=e.target.id;//.split("_");
	items = id.split('_');
	if(items[0] == "transaction"){
	    $.ajax({
		type: 'GET',
		url: "/read_transaction/"+items[1],
    		data: {},
		success: function (response) {
		},
	    });
	}
});

