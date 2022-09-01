from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings

from products.models import Product
from .models import Contact
from .forms import ContactForm

def index(request):
    """ A view to return the index page """
    featured_list = Product.objects.filter(featured=True)
    context = {
        'featured_list': featured_list,
    }
    return render(request, 'home/index.html', context)


def privacy(request):
    """
    view to display Privacy Policy
    """
    return render(request, 'home/privacy.html')


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        sender = "Contact request from" + " " + str(email)
        msg_mail = str(message) + ", " + str(sender)
        if form.is_valid():
            send_mail(
                subject,
                msg_mail,
                email,
                [settings.DEFAULT_FROM_EMAIL, ]
            )
            form.save()
            messages.success(request, 'Your Email has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'There Was an Error Trying to Send Email Message,\
                    Please check your form.'
            )
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'home/contact.html', context)