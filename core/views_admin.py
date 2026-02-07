from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Resort, Room, Reservation
from .forms import ResortForm, RoomForm, ReservationStatusForm
from django.contrib.auth.models import User

# Check if user is admin
def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    total_reservations = Reservation.objects.count()
    available_rooms = Room.objects.filter(status='A').count()
    total_users = User.objects.count()
    
    # Calculate approximate revenue (sum of room prices for 'Paid' reservations)
    # Note: detailed revenue logic might need Duration calculation, keeping it simple for now or adding a method in Model
    # For now, let's just count Completed/Paid reservations * room price per night (assuming 1 night for simplicity unless we calc days)
    # A better approach for the future is to store 'total_price' in Reservation model.
    # We will display 0 for now or a placeholder if complex calculation is needed in models.py
    
    # Simple placeholder revenue (Count of Paid * Avg Price 5000) just for demo or 0
    total_revenue = 0 
    
    recent_reservations = Reservation.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_reservations': total_reservations,
        'available_rooms': available_rooms,
        'total_users': total_users,
        'total_revenue': total_revenue, # Placeholder
        'recent_reservations': recent_reservations,
    }
    return render(request, 'core/admin/dashboard.html', context)

@user_passes_test(is_admin, login_url='login')
def admin_resort_list(request):
    resorts = Resort.objects.all()
    return render(request, 'core/admin/resort_list.html', {'resorts': resorts})

@user_passes_test(is_admin, login_url='login')
def admin_resort_create(request):
    if request.method == 'POST':
        form = ResortForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resort created successfully!')
            return redirect('admin_resort_list')
    else:
        form = ResortForm()
    return render(request, 'core/admin/resort_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def admin_resort_update(request, pk):
    resort = get_object_or_404(Resort, pk=pk)
    if request.method == 'POST':
        form = ResortForm(request.POST, instance=resort)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resort updated successfully!')
            return redirect('admin_resort_list')
    else:
        form = ResortForm(instance=resort)
    return render(request, 'core/admin/resort_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def admin_resort_delete(request, pk):
    resort = get_object_or_404(Resort, pk=pk)
    if request.method == 'POST':
        resort.delete()
        messages.success(request, 'Resort deleted successfully!')
        return redirect('admin_resort_list')
    return render(request, 'core/admin/resort_confirm_delete.html', {'object': resort})

@user_passes_test(is_admin, login_url='login')
def admin_room_list(request):
    rooms = Room.objects.all()
    return render(request, 'core/admin/room_list.html', {'rooms': rooms})

@user_passes_test(is_admin, login_url='login')
def admin_room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room created successfully!')
            return redirect('admin_room_list')
    else:
        form = RoomForm()
    return render(request, 'core/admin/room_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def admin_room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully!')
            return redirect('admin_room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'core/admin/room_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def admin_room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully!')
        return redirect('admin_room_list')
    return render(request, 'core/admin/room_confirm_delete.html', {'object': room})

@user_passes_test(is_admin, login_url='login')
def admin_reservation_list(request):
    reservations = Reservation.objects.all().order_by('-created_at')
    return render(request, 'core/admin/reservation_list.html', {'reservations': reservations})

@user_passes_test(is_admin, login_url='login')
def admin_reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationStatusForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('admin_reservation_list')
    else:
        form = ReservationStatusForm(instance=reservation)
    return render(request, 'core/admin/reservation_form.html', {'form': form, 'object': reservation})

@user_passes_test(is_admin, login_url='login')
def admin_user_list(request):
    users = User.objects.all()
    return render(request, 'core/admin/user_list.html', {'users': users})
