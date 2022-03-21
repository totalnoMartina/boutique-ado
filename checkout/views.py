from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KfqwcDxDT4PvG1CzmCxm4i5trbLgxxaRKLC61bKeAAzApNTikfd8Q7srL8FpzICp7FNcyyLasxSogE78At8pyLn00AHU4RBlS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)