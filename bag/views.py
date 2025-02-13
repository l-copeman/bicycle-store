from django.shortcuts import render, redirect, reverse


def bag_view(request):
    """" A view to return shopping bag"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """" A view to add an item to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """" A view to update an item in the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag_view'))