from django.conf.urls import url
from .views import HomeView
from django.urls import include, path

urlpatterns = [
    path('', HomeView, name="pages_index")
]
