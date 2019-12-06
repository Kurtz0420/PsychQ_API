from django.conf.urls import url
from django.urls import path

from articlesCC.api.views import ArticleRudView, ArticleApiView
from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'(?P<id>\w+)', ArticleRudView.as_view()),
    url(r'^$', ArticleApiView.as_view())


]
