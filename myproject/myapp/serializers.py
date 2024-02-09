# serializers.py

from rest_framework import serializers
from .models import Paragraph, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'dob', 'createdAt', 'modifiedAt')

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'text', 'user', 'created_at')
