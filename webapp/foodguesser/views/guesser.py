from django.shortcuts import render
from foodguesser.models import Food, Score
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import math
import random
import json

def guess(request):
    return render(request, "foodguesser/guesser/guess.html", {})


def username(request):

    if request.method == "POST":
        if(request.POST["username"]):
            request.session["username"] = request.POST["username"]

    return render(request, "foodguesser/guesser/username.html",{})


def get_food(request):
    feed = Food.objects.all()
    food = random.choice(feed)
    json_dict = {"id":int(food.id), "image":static(str(food.image)), "calories":int(food.calories)}
    return HttpResponse(json.dumps(json_dict))


def post_food(request):
    if request.method == "POST":
        guessid = int(request.POST.get("id"))
        guesstimate = int(request.POST.get("guess"))

        if(guesstimate and guessid):
            actual = Food.objects.get(id=guessid).calories
            score = math.fabs(actual-guesstimate)

            session_add_score(request, score)
            return HttpResponse("Guess submitted")
        else:
            return HttpResponse("Didnt do a guesstimate, probably doing some suspicious stuff. Either that or josh broke it.")


def leaderboard(request):
    scoredata = Score.objects.all().order_by("-score")
    return render(request, "foodguesser/guesser/leaderboard.html", {"scores":scoredata})


#Helper functions
def session_add_score(request, add_score):
    score = request.session.get("score")
    
    if(score):
        score += add_score
    else:
        score = add_score

    request.session["score"] = score
        
