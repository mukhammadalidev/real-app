from django.urls import path
from .views import UserLoginView,profile_view,logout_view,RegisterView
app_name = 'users'
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path('logout/',logout_view,name="logout"),
]
