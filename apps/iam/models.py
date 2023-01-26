from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utilities.models import BaseModel
from config.validators import _PHONE_REGEX, _NAME_REGEX
from enum import Enum

# Create your models here.
class User(AbstractUser):
    id = models.CharField(max_length=255, primary_key=True)
    ordering = ('username',)
    username = models.CharField(
        # ('Mobile Number'),
        # validators=[_PHONE_REGEX],
        max_length=255, unique=True
    )
    email = models.EmailField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    last_name = models.CharField(max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10, blank=True, null=True,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
        )
    )
    is_blocked = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)

class SessionLog(BaseModel):
    session_id = models.CharField(max_length=100)
    client_id = models.CharField(max_length=50)

    def __str__(self):
        return '{} Logged in at {}'.format(self.session_id, self.created_at)

class GroupEnum(Enum):
    ADMIN_GROUP = 'Admin'
    CUSTOMER_GROUP = 'CustomerGroup'