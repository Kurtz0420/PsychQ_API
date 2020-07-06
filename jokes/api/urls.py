from django.conf.urls import url
from django.urls import path

from jokes.api.views import JokeRudView, JokeApiView
from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'(?P<id>\w+)', JokeRudView.as_view()),
    url(r'^$', JokeApiView.as_view())


]
