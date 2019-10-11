from django.contrib.auth import backends
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.views import LoginView
from django.db.models import Q
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from accounts.api.serializers import RegistrationSerializer
from accounts.models import Account


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully Registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)

    def get_queryset(self):
        return Account.objects.filter(username=self.kwargs['username'])



# class AccountRView(generics.RetrieveAPIView):
#     lookup_field = 'pk'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field
#     #  #data will be fetched by entring pk
#     serializer_class = AccountSerializer
#     queryset = Account.objects.all()
#
#     def get_queryset(self):
#         return Account.objects.all()
