from django.urls import path
from .views import AdvertismentView,Job_DetailView,AdsEmployerView,ApplicationView,AdvertisementAPIView,AdvertisementDetailAPIView,CreateWorker,WorkerView,WorkerDeleteView,WorkerDetailView,WorkerEditView

app_name = "job"
urlpatterns = [
    path('categories/<int:pk>/',AdvertismentView.as_view(),name="category"),
    path('job/<int:pk>/',Job_DetailView.as_view(),name="job-detail"),
    path('add/',AdsEmployerView.as_view(),name="add_ads"),
    path('apply/<int:job_pk>/', ApplicationView.as_view(), name='apply_for_job'),
    path('api/jobs/', AdvertisementAPIView.as_view(), name='advertisement-list'),
    path('api/jobs/<int:pk>/', AdvertisementDetailAPIView.as_view(), name='advertisement-detail'),
    path('create-worker/', CreateWorker.as_view(), name='create_worker'),
    path('workers/', WorkerView.as_view(), name='worker_list'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('workers/delete/<int:pk>/', WorkerDeleteView.as_view(), name='worker-delete'),
    path('workers/edit/<int:pk>/', WorkerEditView.as_view(), name='worker-edit'),


]