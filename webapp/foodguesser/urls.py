from django.conf.urls import url
from foodguesser import views

urlpatterns = [
    url(r'^$', views.base.index, name="index"),
    url(r'^about/$', views.base.index, name="about"),
    url(r'^guess/$', views.guesser.guess, name="guess"),
    url(r'^leaderboard/$', views.guesser.leaderboard, name="leaderboard"),
    url(r'^randomimage/$', views.better_guess.random_image, name="random_image")
    url(r'get_food/$', views.guesser.get_food, name="get_food"),
]
