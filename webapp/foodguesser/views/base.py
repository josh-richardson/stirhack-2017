from django.shortcuts import render

def index(request):
    return render(request, "foodguesser/guesser/guess.html", {})

def about(request):
    return render(request, "base/about.html", {})
