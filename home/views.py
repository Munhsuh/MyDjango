from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Post, Food, TourPackage, Nomad
from .forms import GuestbookForm
from .models import GuestbookEntry

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home/home.html', {'posts': posts})

def tour_packages(request):
    packages = TourPackage.objects.all().order_by('-created_at')
    return render(request, 'home/tour_packages.html', {'packages': packages})

def food(request):
    foods = Food.objects.all().order_by('-created_at')
    return render(request, 'home/food.html', {'foods': foods})

def nomads(request):
    nomads = Nomad.objects.all().order_by('-created_at')
    return render(request, 'home/nomads.html', {'nomads': nomads})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,  # Sender's email
                [settings.CONTACT_EMAIL],  # Recipient's email
                fail_silently=False,
            )
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'home/contact_success.html')


def guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            GuestbookEntry.objects.create(name=name, email=email, message=message)
            return redirect('guestbook')  # Redirect to the guestbook page
    else:
        form = GuestbookForm()

    entries = GuestbookEntry.objects.order_by('-created_at')
    return render(request, 'home/guestbook.html', {'form': form, 'entries': entries})