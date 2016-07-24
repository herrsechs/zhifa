$.ajax({
	type: "POST",
	url: "localhost:8000:account/register",
	data: {username: 'gamino', password: '123456', gender: 'male', role: 'Customer'},
	ContentType: "application/json",
	success: function(){

	},
	error: function(){

	}
});
