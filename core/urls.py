"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
