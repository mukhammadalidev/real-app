from django.urls import path

from .views import JobsAPIView,JobDetailAPIView,CreateJob,UpdateJob,DestroyJob

urlpatterns = [
    path('jobs/', JobsAPIView.as_view(), name='jobs_api'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job_detail_api'),
    path('jobs/create/', CreateJob.as_view(), name='create_job_api'),
    path('jobs/update/<int:pk>/', UpdateJob.as_view(), name='update_job_api'),
    path('jobs/delete/<int:pk>/', DestroyJob.as_view(), name='delete_job_api'),
]