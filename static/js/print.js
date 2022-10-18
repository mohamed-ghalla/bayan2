document.addEventListener('click',(e) =>
{
	id=e.target.id;//.split("_");
	name = $(document.getElementById(id)).attr('url');
	var path = window.location.origin+name ;
	if(id.split("_")[0] == "print"){
		alert("print");
		if (name.endsWith('.pdf')) {
			pdf = window.open(path);
			pdf.print();
			printJS(path);
		}

		else if (name.endsWith('docx')) {
			var wnd = window.open(path);
			wnd.print();
		}
		else if (name.endsWith('png') || name.endsWith('jpg') ||  name.endsWith('jfif')){
			image = window.open(path);
			image.print();
			printJS(name, 'image');
		}
		else{
			window.print();
		}
	}
	else if (id.split("_")[0] == "show"){
		if (name.endsWith('.pdf')) {
			alert(path);
			window.open(path);
//	    		$("#img_div").html(`<embed src=`+path+` frameborder="0" width="100%" height="600px">`);
		}
		else if (name.endsWith('png') || name.endsWith('jpg') ||  name.endsWith('jfif')){
			$("#img_div").html("<img class='files file-pic' src="+path+" width='100%' >");
		}
	
	}
});


//function show_img(source) {
//  type = source.split('.')[1];
//  if (source.endsWith('.docx') || source.endsWith('.doc')){
//    $("#img_div").html(`<iframe src="https://docs.google.com/gview?url=https://bayancoopq8.com`+source+`&embedded=true" frameborder="0" width="100%" height="600px"></iframe>`);
//  }
//  else if(source.endsWith('.pdf')){
//    $("#img_div").html(`<embed src=https://bayancoopq8.com`+source+` frameborder="0" width="100%" height="600px">`);
//  }
//  else if(source.endsWith('.png') || source.endsWith('.jpg') || source.endsWith('.jfif')){
//    $("#img_div").html("<img class='files file-pic' src="+source+" width='100%' >");
//  }
//  else if(source.endsWith('.xlsx')){
//    $("#img_div").html(`<iframe src='https://view.officeapps.live.com/op/embed.aspx?src=https://bayancoopq8.com`+source+`' width='100%' height='565px' frameborder='0'> </iframe>`);
//  }
//};
