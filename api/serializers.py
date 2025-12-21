from rest_framework import serializers
from advertisement.models import Job, CategoryModel
from users.models import  CustomUser

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'