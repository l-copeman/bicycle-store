from django.shortcuts import render
from .models import About


def about_view(request):
    """" A view to return about page informtation"""
    about = About.objects.first()

    context = {
        'about': about,
    }
    template = 'about/about.html'

    return render(request, template, context)
