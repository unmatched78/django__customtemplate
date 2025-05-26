# core/views.py
import logging
from rest_framework import viewsets, status, generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes, api_view, permission_classes
from django.contrib.auth import get_user_model
from .models import *
from rest_framework import filters
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from decimal import Decimal
from django.db import transaction 
User = get_user_model()
# Module‐level logger
logger = logging.getLogger(__name__)  # best practice for namespaced logging

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Call the base class to get the original tokens
        data = super().validate(attrs)
        # Attach your user info
        data['user'] = {
            'id':       self.user.id,
            'username': self.user.username,
            'email':    self.user.email,
            # add more fields as needed
        }
        return data
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # --- Inject these claims into BOTH access & refresh tokens ---
        token['user_id']     = user.id
        token['role']        = user.custom_role.name if user.custom_role else None
        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


    def perform_create(self, serializer):
        logger.info(f"{self.request.user} creating organization {serializer.validated_data.get('name')}")
        serializer.save(created_by=self.request.user)

class CustomRoleViewSet(viewsets.ModelViewSet):
    """CRUD for Custom Roles."""
    queryset = CustomRole.objects.all()
    serializer_class = CustomRoleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, RolePermission]
    required_permission = 'create_roles'

class UserViewSet(viewsets.ModelViewSet, OrgQuerysetMixin):
    """CRUD for Users within the same organization."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, RolePermission]
    required_permission = 'view_users'
class DemoRequestCreateAPIView(generics.CreateAPIView):
    queryset         = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer
    permission_classes = [permissions.AllowAny]
