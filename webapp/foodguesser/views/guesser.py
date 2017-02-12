from django.shortcuts import render
from foodguesser.models import Food, Score
import random
from django.http import HttpResponse
import json
from django.contrib.staticfiles.templatetags.staticfiles import static

def guess(request):
    return render(request, "foodguesser/guesser/guess.html", {})


def get_food(request):
    feed = Food.objects.all()
    food = random.choice(feed)
    json_dict = {"id":int(food.id), "image":static(str(food.image)), "calories":int(food.calories)}
    return HttpResponse(json.dumps(json_dict))


def post_guess(request):
    if request.method == "POST":
        guessid = int(request.POST.get("id"))
        guesstimate = int(request.POST.get("guess"))

        if(guesstimate and guessid):
            actual = Food.objects.get(id=guessid).calories
            score = math.abs(actual-guesstimate)

            session_add_score(request, score) 
        else:
            return HttpResponse("Didnt do a guesstimatei, probably doing some suspicious stuff. Either that or josh broke it.")


def leaderboard(request):
    scoredata = Score.objects.all().order_by("-score")
    return render(request, "foodguesser/guesser/leaderboard.html", {"scores":scoredata})


#Helper functions
def session_add_score(requesti, add_score):
    score = request.session.get("score")
    
    if(score):
        score += add_score
    else:
        score = add_score

    request.sesion["score"] = score
        
