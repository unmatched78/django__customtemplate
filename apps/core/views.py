from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .mixins import CacheMixin, LoggingMixin

class BaseAPIView(LoggingMixin, generics.GenericAPIView):
    """
    Base API view with common functionality
    """
    def handle_exception(self, exc):
        """
        Handle exceptions and return appropriate responses
        """
        self.log_error(f"Exception in {self.__class__.__name__}: {exc}")
        return super().handle_exception(exc)

class BaseListCreateView(CacheMixin, BaseAPIView, generics.ListCreateAPIView):
    """
    Base view for list and create operations
    """
    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class BaseRetrieveUpdateDestroyView(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    Base view for retrieve, update, and destroy operations
    """
    pass
