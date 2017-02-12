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
		success: function(score) {
			$(".score").html('Score: '+parseInt(score));

		}, error: function() {
			console.log("ERROR POST /guess");
		}
	})
}

$(document).ready(function() {
	var img;
	var id;
	var guess;
	var score;
	var calories;

	img = getNext(function(img) {
		calories = img.calories;
		id = img.id;
		$(".guess-img").attr('src', img.image);
	});

	$(".btn-checkbox-submit").click(function(e) {
        e.preventDefault();
        guess = $('.rangeslider__handle').text();
        $('.answer-div').css('visibility', 'visible');
        $(".answer").html('Answer: '+calories);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        postAnswer(id, guess, token);

        $(".btn-checkbox-submit").prop('disabled', true);
    });

    $(".btn-next").click(function(e) {
    	e.preventDefault();
    	$('.answer-div').css('visibility', 'hidden');
    	getNext(function(img) {
        	console.log("Timeout finished");
			calories = img.calories;
			$(".guess-img").attr('src', img.image);
		})
		$(".btn-checkbox-submit").prop('disabled', false);
    });

    $("a[href='#leaderboard']").click(function(e) {
    	$.ajax({
			url: '/get_score',
			success: function(data) {
				data = JSON.parse(data);
				for (key in data) {
					console.log(data[key]);
					$(".highscores").append("<tr><td>"+data[key].fields.username+"</td><td>"+data[key].fields.score+"</td></tr>");
				}
			}, error: function() {
				console.log("ERROR GET /get_score");
			}
		})

    });

});



$("#username-submit").click(function () {
    $('.nav-tabs a[href="#caloroid"]').tab('show');
});