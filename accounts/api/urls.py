from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.api.views import (

    registration_view,
    )

app_name = "accounts"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', LoginView.as_view(), name='login')
    # url(r'^(?P<username>\d+)/$', AccountRView.as_view()),
]
