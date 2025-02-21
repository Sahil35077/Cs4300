from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'bookings/home.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # ✅ Redirects to login after successful signup
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(is_booked=False)
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def home(request):
    """Render the home page with links to both API and web views."""
    return render(request, 'bookings/home.html')

def movie_list(request):
    """Render the movie list page."""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

class MovieViewSet(viewsets.ModelViewSet):
    """REST API for movies (CRUD operations)"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    """REST API for seats (availability & booking)"""
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """REST API for bookings"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  