from django.contrib import admin
from django.urls import path,include
from .views import IndexView,search,SearchView,contact_view,about_view,faq_view,JobRemove
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name="home"),
    path('advertisements/',include('advertisement.urls')),
    path('accounts/',include('users.urls')),
    path('search/',SearchView.as_view(),name="search"),
    path("contact/", contact_view, name="contact"),
    path("about/", about_view, name="about"),
    path("faq/", faq_view, name="faq"),
    path('job/delete/<int:pk>/', JobRemove.as_view(), name='job_delete'),
    # API URLs
    path('api/', include('api.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
