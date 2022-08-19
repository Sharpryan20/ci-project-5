from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LCmV5Bl7UhIncU1aFomJjWAHxgTJXajKWTHs187tOj95ukXCT7Du8keJdvDOIrOdxPB0P5k5ZyOJCJGkdROyboJ00BKT2euHU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
