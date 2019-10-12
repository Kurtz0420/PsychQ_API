from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView


urlpatterns = [
    url(r'(?P<id>\w+)', CategoryRudView.as_view()),
    url(r'^$', CategoryApiView.as_view())


]
