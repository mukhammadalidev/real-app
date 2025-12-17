from rest_framework import serializers
from .models import Job,CategoryModel,EmployerProfile,Application



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'  

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    employer = EmployerProfileSerializer()

    class Meta:
        model = Job
        fields = '__all__'