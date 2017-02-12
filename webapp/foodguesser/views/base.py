from django.shortcuts import render

def index(request):
	request.session["score"] = 0
	return render(request, "foodguesser/guesser/guess.html", {})

def about(request):
    return render(request, "base/about.html", {})
