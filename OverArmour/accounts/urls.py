from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile')
]
