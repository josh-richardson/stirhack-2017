from django.shortcuts import render

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
            
    image = null
    return render(request, "guesser/guess.html", {"img": image})


def leaderboard(request):
    scoredata = Scores.objects.all().order_by("-score")
    return render(request, "guesser/leaderboard.html", {"scores":scoredata})


#Helper functions
def session_add_score(request):
    score = request.session.get("score")
    
    if(score):
        score += 1
    else:
        score = 1

    request.sesion["score"] = score
        
