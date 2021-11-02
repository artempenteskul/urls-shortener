from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Url


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password2'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords should match!'})
        user.set_password(password)
        user.save()
        return user


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UrlSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(read_only=True)

    class Meta:
        model = Url
        fields = ('url', 'short_url', 'user')
