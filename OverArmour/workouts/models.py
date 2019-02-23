from django.db import models
from django.contrib.auth.models import User


def workout_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/workout_<id>/<filename>
    return 'workout_{0}/{1}'.format(instance.id, filename)


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    reps = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to=workout_dir_path, default=None)
    exercises = models.ManyToManyField(Exercise)
    users = models.ManyToManyField(User, related_name='workouts')

    def __str__(self):
        return self.name
