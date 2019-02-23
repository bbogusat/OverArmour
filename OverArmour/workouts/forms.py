from django import forms
from .models import Workout, Exercise


# Extends Model form
class WorkoutCreationForm(forms.ModelForm):
    name = forms.CharField(label="Workout name", required=True)
    # Queryset of all of the exercises available
    exercises = forms.ModelMultipleChoiceField(
        label="Exercises", queryset=Exercise.objects.all(), widget=forms.SelectMultiple(), required=True)
    img = forms.ImageField(label="Image")

    # Excludes the user field of the Workout Model
    class Meta:
        model = Workout
        exclude = ['users']
