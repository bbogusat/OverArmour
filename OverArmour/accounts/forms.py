from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Inheirits from the UserCreationForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2'
        )

    # Override the save method for form
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


# Forms for updating profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio',
            'weight'
        )
