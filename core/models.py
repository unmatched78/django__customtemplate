from decimal import Decimal
from django.db import transaction
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta
from django.db import models, transaction
from django.core.exceptions import ValidationError

# --- Core and Role Models ---
FREQUENCY_DELTAS = {
    'daily':    datetime.timedelta(days=1),
    'weekly':   datetime.timedelta(weeks=1),
    'biweekly': datetime.timedelta(weeks=2),
    'monthly':  lambda dt: (dt + relativedelta(months=1)).replace(day=dt.day),
}

class Timer(models.Model):
    updated_at=models.DateTimeField(auto_now=True)
    created_at= models.DateTimeField(auto_now_add=True)
    
    class meta:
        abstract=True
class CustomRole(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="roles_created"
    )

    class Meta:
        unique_together = ('name', 'organization')

    def __str__(self):
        return f"{self.name} - {self.organization.name}"

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    custom_role = models.ForeignKey(
        CustomRole,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )

    def get_roles(self):
        return [self.custom_role.name] if self.custom_role else []

    def has_permission(self, perm):
        return self.custom_role and perm in self.custom_role.permissions

# demo_model always necessary
class DemoRequest(models.Model):
    full_name   = models.CharField(max_length=150)
    email       = models.EmailField()
    company     = models.CharField(max_length=150, blank=True)
    phone       = models.CharField(max_length=20, blank=True)
    datetime    = models.DateTimeField(null=True, blank=True)
    message     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} <{self.email}> @ {self.created_at:%Y-%m-%d %H:%M}"


