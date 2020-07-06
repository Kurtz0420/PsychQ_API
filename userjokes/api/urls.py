from django.conf.urls import url
from django.urls import path

from jokes.api.views import JokeRudView, JokeApiView
from posts.api.views import PostRudView, PostApiView
from userjokes.api.views import UserJokeRudView, UserJokeApiView

urlpatterns = [
    url(r'^(?P<id>[0-9a-f-]+)/$', UserJokeRudView.as_view()),
    url(r'^$', UserJokeApiView.as_view())


]
