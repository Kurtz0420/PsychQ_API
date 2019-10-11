import uuid

from rest_framework import serializers
from accounts.models import Account


# Converts to JSON + Validation for data passed
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # password2 have to be added manually

    class Meta:
        model = Account
        fields = [
            'uuid',
            'username',
            'email',
            'password',
            'password2'
        ]
        # THis will secure the user passwords and hide
        extra_kwagrs = {
            'password': {'write_only': True}
        }

        # data validation

    def save(self):
        account = Account(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'Confirm Password': 'Passwords must match'})
        account.set_password(password)
        # account.set_uuid(uuid.uuid4)
        account.save()
        return account


#
# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = [
#             'pk',
#             'uuid',
#             'username',
#             'email',
#             'date_joined',
#             'last_login',
#             'profile_pic'
#         ]
#         read_only_fields = ['pk', 'uuid', 'date_joined']
#
#         # For Field Validation
#
#         #  This part is not working properly, come back to it later
#         def __init__(self):
#             self.instance = None
