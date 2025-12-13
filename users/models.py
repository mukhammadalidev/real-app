from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLES = (
        ('Worker','Worker'),
        ('Employer','Employer'),
    )
    user_roles = models.CharField(max_length=255,choices=USER_ROLES,default='Employer')