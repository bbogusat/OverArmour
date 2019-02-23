from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Method to register a new user
def register(request):
    # If posting then take the POST request check validity and save
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages_index')
        # Display the form to register.html
    form = RegistrationForm()

    args = {'form': form}
    return render(request, 'registration/register.html', args)


# Method to display user profile, will send user as arg
def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)


# Form to update user profile
@login_required
def update_profile(request):
    if request.method == 'POST':
        # Get both forms you want to display / post to
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, (
                'Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
