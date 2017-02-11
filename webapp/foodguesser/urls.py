from django.conf.urls import url
from foodguesser import views
from foodguesser.views import *

urlpatterns = [
    url(r'^$', views.base.index, name="index"),
    url(r'^about/$', views.base.index, name="about"),
    url(r'^guess/$', views.guesser.guess, name="guess"),
    url(r'^leaderboard/$', views.guesser.leaderboard, name="leaderboard"),
]
