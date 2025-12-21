from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from advertisement.models import Job
from .serializers import JobSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class JobsAPIView(APIView):
    def get(self, request):
        jobs = Job.objects.all().order_by('-created_at')
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=200)
    
class JobDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        
        serializer = JobSerializer(job)
        return Response(serializer.data, status=200)
    

class CreateJob(CreateAPIView):
    permission_classes = [
        IsAdminUser
    ]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class DestroyJob(APIView):
    permission_classes = [
        IsAdminUser
    ]

    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        
        job.delete()
        return Response({"message": "Job deleted successfully"}, status=200)
    

class UpdateJob(APIView):
    permission_classes = [
        IsAdminUser
    ]

    def put(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)