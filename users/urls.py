from django.urls import path

from users.views import RegisterView, profile_info, UserUpdatePasswordView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='distribution:distributions'), name='logout'),
    path('profile/<int:pk>', profile_info, name='profile'),
    path('password/<int:pk>', UserUpdatePasswordView.as_view(), name='change_pass'),
]