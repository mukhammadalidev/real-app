from django.contrib import admin
from .models import CategoryModel,AdvertisementModel,EmployerProfile,Job,Application
# Register your models here.
admin.site.register([CategoryModel,AdvertisementModel,EmployerProfile,Job,Application])