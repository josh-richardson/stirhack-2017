from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^/$', views.base.index, name="index"),
    url(r'^about/$', views.base.index, name="about"),
    url(r'^guess/$', views.guesser.guess, name="guess"),
    url(r'^leaderboard/$', views.guesser.leaderboard, name="leaderboard"),
]
