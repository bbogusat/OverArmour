from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('create_workout/', views.create_workout, name='create_workout'),
    path('<int:pk>/', views.WorkoutDetail.as_view(), name='workout_detail'),
    path('attach_workout/', views.attach_workout, name='attach_workout'),
]
