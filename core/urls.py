# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
#your routes here
urlpatterns = [
    # REST API
    path('api/', include(router.urls)),
    # Custom function-based endpoint here
    path("api/book-demo/", DemoRequestCreateAPIView.as_view(), name="book-demo"),

    # JWT endpoints
    path('api/auth/token/login/',  MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),
]
