from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from workouts.models import Exercise, Workout
from .forms import WorkoutCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required
# Create your views here.


def create_workout(request):
    if request.method == "POST":
        form = WorkoutCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.name = form.cleaned_data['name']
            form.img = form.cleaned_data['img']
            form.exercises = form.cleaned_data['exercises']
            workout = form.save()
            workout.users.add(request.user)
            workout.save()
            return redirect('pages_index')
    else:
        form = WorkoutCreationForm()
        args = {'form': form}
        return render(request, 'workouts/create.html', args)


class WorkoutDetail(generic.DetailView):
    model = Workout
    template_name = 'workouts/workout_detail.html'


@login_required
def attach_workout(request):
    if request.method == "POST":
        w_id = request.POST['workout']
        workout = Workout.objects.get(id=w_id)
        workout.users.add(request.user)
        workout.save()
        return redirect('profile')
    return redirect('workout_detail')
