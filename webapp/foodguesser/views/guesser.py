from django.shortcuts import render
from foodguesser.models import Food, Score
import random
from django.http import HttpResponse
import json


def guess(request):
    if request.method == "POST":
        guessid = request.POST.get("id")
        guesstimate = request.POST.get("guess")

        if(guesstimate and guessid):
            if(Food.objects.get(id=guessid).calories == guesstimate):
                session_add_score(request)
            
            return HttpRedirect(reverse("guess"))
        else:
            return HttpResponse("Didnt do a guesstimate")
            
    images = Food.objects.all()
    image = random.choice(images)
    return render(request, "foodguesser/guesser/guess.html", {"image": str(image)})


def get_food(request):
    feed = Food.objects.all()
    food = random.choice(feed)
    json_dict = {"id":int(food.id), "image":str(food.image), "calories":int(food.calories)}
    return HttpResponse(json.dumps(json_dict))

def leaderboard(request):
    scoredata = Score.objects.all().order_by("-score")
    return render(request, "foodguesser/guesser/leaderboard.html", {"scores":scoredata})


#Helper functions
def session_add_score(request):
    score = request.session.get("score")
    
    if(score):
        score += 1
    else:
        score = 1

    request.sesion["score"] = score
        
