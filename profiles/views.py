from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')


    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form' : form,
        'orders' : orders,
    }

    return render(request, template, context)