from django.shortcuts import render
from django.views.generic import TemplateView
from workouts.models import Workout


# Homepage view passed the workout model objects
def HomeView(request):
    workouts = Workout.objects.all()
    return render(request, 'pages/index.html', {'workouts': workouts})
