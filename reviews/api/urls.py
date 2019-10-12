from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from orders.api.views import OrderRudView, OrderApiView
from products.api.views import ProductRudView, ProductApiView
from reviews.api.views import ReviewRudView, ReviewApiView

urlpatterns = [
    url(r'^(?P<id>[0-9a-f-]+)/$', ReviewRudView.as_view()),
    url(r'^$', ReviewApiView.as_view())


]
