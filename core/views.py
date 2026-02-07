from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Resort, RoomType, Room, Reservation
from .forms import ReservationForm
from datetime import date

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        # Prefer the 'next' parameter if present
        url = self.get_redirect_url()
        if url:
            return url
            
        # Redirect admins to dashboard
        if self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser):
            return reverse_lazy('admin_dashboard')
            
        # Default behavior (LOGIN_REDIRECT_URL in settings)
        return super().get_success_url()

def home(request):
    location_query = request.GET.get('location')
    if location_query:
        resorts = Resort.objects.filter(location__icontains=location_query)
    else:
        resorts = Resort.objects.all()
    
    # Get unique locations for the dropdown
    locations = Resort.objects.values_list('location', flat=True).distinct()
    
    return render(request, 'core/home.html', {
        'resorts': resorts,
        'locations': locations,
        'search_params': request.GET,
        'today': date.today(),
    })

def resort_detail(request, resort_id):
    resort = get_object_or_404(Resort, id=resort_id)
    # Get room types available at this resort
    room_types = RoomType.objects.filter(rooms__resort=resort).distinct()
    return render(request, 'core/resort_detail.html', {'resort': resort, 'room_types': room_types})

def room_detail(request, resort_id, room_type_id):
    resort = get_object_or_404(Resort, id=resort_id)
    room_type = get_object_or_404(RoomType, id=room_type_id)
    return render(request, 'core/room_detail.html', {'resort': resort, 'room_type': room_type})

@login_required
def book_room(request, resort_id, room_type_id):
    resort = get_object_or_404(Resort, id=resort_id)
    room_type = get_object_or_404(RoomType, id=room_type_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            
            # Find an available room of this type at this resort for the given dates
            # Exclude rooms that have overlapping reservations
            unavailable_rooms = Reservation.objects.filter(
                room__resort=resort,
                room__room_type=room_type,
                check_in__lt=check_out,
                check_out__gt=check_in,
                status__in=['P', 'C'] # Pending or Confirmed
            ).values_list('room_id', flat=True)
            
            available_room = Room.objects.filter(
                resort=resort, 
                room_type=room_type,
                status='A'
            ).exclude(id__in=unavailable_rooms).first()
            
            if available_room:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.room = available_room
                reservation.status = 'C' # Confirm immediately for simplicity, or P
                reservation.save()
                return redirect('my_reservations')
            else:
                form.add_error(None, "No rooms available for these dates.")
    else:
        form = ReservationForm()
    
    return render(request, 'core/booking_form.html', {
        'resort': resort, 
        'room_type': room_type, 
        'form': form
    })

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/my_reservations.html', {'reservations': reservations})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
