function getNext(callback) {
	$.ajax({
		url: '/get_food',
		success: function(data) {
			console.log(data);
			callback(JSON.parse(data));
		}, error: function() {
			console.log("ERROR GET /image");
		}
	})
}

function postAnswer(id, guess) {
	$.ajax({
		url: '/post_food',
		method: 'POST',
		data: {
			id: id,
			guess: guess
		},
		success: function(data) {
			console.log("Guess posted");

		}, error: function() {
			console.log("ERROR POST /guess");
		}
	})
}

$( document ).ready(function() {
	console.log("ready");
	var img;
	var id;
	var guess;
	var score;

	img = getNext(function(img) {
		console.log(img.image);
		score = img.calories;
		id = img.id;
		$(".guess-img").attr('src', '/static/'+img.image);

	});

	$(".btn-checkbox-submit").click(function(e) {
        e.preventDefault();
        guess = $('.rangeslider__handle').text();
        console.log(img);
        $(".answer").html('Answer: '+score);
        postAnswer(id, guess);
        getNext(function(img) {
			score = img.calories;
			$(".guess-img").attr('src', '/static/'+img.image);
		});
    });

});