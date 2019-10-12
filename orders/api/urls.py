from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from orders.api.views import OrderRudView, OrderApiView
from products.api.views import ProductRudView, ProductApiView

urlpatterns = [
    url(r'^(?P<order_id>[0-9a-f-]+)/$', OrderRudView.as_view()),
    url(r'^$', OrderApiView.as_view())

    # first url will take uuid as a parameter

]
