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

function postAnswer(id, guess, token) {
	if (guess[guess.length-1] == "+") {
		guess = guess.substring(0, guess.length-1);
	}
	$.ajax({
		url: '/post_food/',
		method: 'POST',
		headers: {
	        "X-CSRFToken": token
	    },
		data: {
			id: id,
			guess: guess
		},
		success: function(data) {

		}, error: function() {
			console.log("ERROR POST /guess");
		}
	})
}

$( document ).ready(function() {
	var img;
	var id;
	var guess;
	var score;

	img = getNext(function(img) {
		score = img.calories;
		id = img.id;
		$(".guess-img").attr('src', img.image);

	});

	$(".btn-checkbox-submit").click(function(e) {
        e.preventDefault();
        guess = $('.rangeslider__handle').text();
        $(".answer").html('Answer: '+score);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log(token);
        postAnswer(id, guess, token);
        getNext(function(img) {
			score = img.calories;
			$(".guess-img").attr('src', img.image);
		});
    });

});