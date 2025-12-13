from django.urls import path
from .views import AdvertismentView,Job_DetailView,AdsEmployerView,ApplicationView

app_name = "job"
urlpatterns = [
    path('categories/<int:pk>/',AdvertismentView.as_view(),name="category"),
    path('job/<int:pk>/',Job_DetailView.as_view(),name="job-detail"),
    path('add/',AdsEmployerView.as_view(),name="add_ads"),
    path('apply/<int:job_pk>/', ApplicationView.as_view(), name='apply_for_job'),


]