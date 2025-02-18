from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51QKM4iDIwIPOm657wuUTu6HgU757tg2ZvVByqYEOrMVuftR0DtzAwtOa2VzHm3HFNLNzMRmLow3YfDFYkbw4EaWr00ddoYUDk9',
        'client_secret' : 'test client secret'
    }

    return render(request, template, context)