from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from .views import UserProfileView

app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/<slug:name>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', views.logout, name='logout'),
]
