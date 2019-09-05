from django.conf.urls import url

from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostRudView.as_view()),
    url(r'^$', PostApiView.as_view())


]
