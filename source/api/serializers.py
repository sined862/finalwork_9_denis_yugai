from rest_framework import serializers
from gallery.models import Photo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['img', 'photos']


