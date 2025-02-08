from django.shortcuts import render

def bag_view(request):
    """" A view to return shopping bag"""

    return render(request, 'bag/bag.html')