from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Url


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UrlSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(read_only=True)

    class Meta:
        model = Url
        fields = ('url', 'short_url', 'user')
