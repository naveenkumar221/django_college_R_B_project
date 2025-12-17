from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import CustomUserCreationForm


def home(request):
    is_guest = request.session.get('is_guest', False)
    return render(request, 'home.html', {'is_guest': is_guest})


def book_resource(request):
    is_guest = request.session.get('is_guest', False)

    if is_guest:
        if request.method == "POST":
            return redirect('/accounts/login/')
        return render(request, 'book.html', {'guest': True})

    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'home.html', {
            'error': 'Principal can only approve bookings'
        })

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if request.method == "POST":
        Booking.objects.create(
            student_name=request.user.username,
            resource_name=request.POST.get('resource_name'),
            booking_date=request.POST.get('booking_date'),
            booking_time=request.POST.get('booking_time'),
            status='Pending'
        )
        return redirect('my_bookings')

    return render(request, 'book.html')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        student_name=request.user.username
    )
    return render(request, 'my_bookings.html', {'bookings': bookings})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session.pop('is_guest', None)  # clear guest
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def guest_login(request):
    logout(request)
    request.session['is_guest'] = True
    return redirect('home')


def user_logout(request):
    request.session.pop('is_guest', None)
    logout(request)
    return redirect('home')
