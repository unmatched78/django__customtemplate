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


