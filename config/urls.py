from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('distribution/', include('distribution.urls', namespace='distribution')),
    path('users/', include('users.urls', namespace='users')),
]
