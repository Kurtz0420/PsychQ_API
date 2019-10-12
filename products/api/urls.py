from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from products.api.views import ProductRudView, ProductApiView

urlpatterns = [
    url(r'(?P<id>\w+)', ProductRudView.as_view()),
    url(r'^$', ProductApiView.as_view())


]
