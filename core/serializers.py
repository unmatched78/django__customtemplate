from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()
#serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone']
class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = DemoRequest
        fields = [
            "id", "full_name", "email", "company",
            "phone", "datetime", "message", "created_at"
        ]
        read_only_fields = ["id", "created_at"]

#more serializers here
