from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validations

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        # add in extra fields here...
        fields = ('id', 'username', 'email', 'password', 'password_confirmation', 'name', 'image', 'meals', 'bio',)
