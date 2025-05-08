# core/permissions.py
from django.core.exceptions import PermissionDenied
from .models import CustomUser, CustomRole

AVAILABLE_PERMISSIONS = [ 
    #Your permissions here
]

def has_permission(user: CustomUser, permission: str) -> bool:
    """
    Check if the user has the specified permission based on their custom_role.
    """
    if not user.is_authenticated:
        return False
    if not user.custom_role:
        return False
    return permission in user.custom_role.permissions

def has_role(user: CustomUser, role_name: str) -> bool:
    """
    Check if the user has the specified role.
    """
    if not user.is_authenticated:
        return False
    return user.custom_role and user.custom_role.name == role_name

def require_permission(permission: str):
    """
    Decorator to enforce a permission check before executing a view or function.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not has_permission(self.request.user, permission):
                raise PermissionDenied(f"Permission '{permission}' required.")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def require_any_permission(permissions: list):
    """
    Decorator to enforce that at least one of the listed permissions is present.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not any(has_permission(self.request.user, perm) for perm in permissions):
                raise PermissionDenied(f"One of {permissions} required.")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def get_user_permissions(user: CustomUser) -> list:
    """
    Get all permissions for a user based on their custom_role.
    """
    return user.custom_role.permissions if user.custom_role else []

def get_available_permissions(organization=None) -> list:
    """
    Get all unique permissions available for role creation.
    Could be filtered by organization-specific rules later.
    """
    return AVAILABLE_PERMISSIONS