function upload(event) {
	event.preventDefault();
	var data = new FormData($('form').get(0));
	console.log(data)
	$.ajax({
		url: 'upload/',
		type: $(this).attr('method'),
		data: data,
		cache: false,
		processData: false,
		contentType: false,
		success: function(data) {
			alert('success');
		}
	});
	return false;
}
$(function() {
	$('#file-form').submit(upload);
});

$('li.nav-item').click(function(e){
	$('.nav-item').removeClass('active');
	$(this).addClass('active');
	if(this.id == 'file_upload'){
		$('.file_share').hide();
		$('#file_upload_div').show();
	}else if(this.id == 'file_history'){
		$('.file_share').hide();
		$('#file_history_div').show();
	}
});

$('.action_delete').click(function(e){
	id = $(this).val();
	var deletedata = this
	$.ajax({
		url: 'upload/',
		data:{
			'file_id':id
		},
		type: 'DELETE',
		success: function(data) {
			alert('Delete success');
			$(deletedata).closest("tr").remove();

		}
	});
});