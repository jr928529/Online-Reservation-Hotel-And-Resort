from django import forms
from .models import Reservation, Resort, Room

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full', 'id': 'id_check_in'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full', 'id': 'id_check_out'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError("Check-out date must be after check-in date.")
        return cleaned_data

class ResortForm(forms.ModelForm):
    class Meta:
        model = Resort
        fields = ['name', 'category', 'location', 'description', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'category': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'location': forms.TextInput(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'image_url': forms.URLInput(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['resort', 'room_type', 'number', 'status']
        widgets = {
            'resort': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'room_type': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'number': forms.TextInput(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'status': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
        }

class ReservationStatusForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['status', 'payment_status']
        widgets = {
            'status': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
            'payment_status': forms.Select(attrs={'class': 'w-full border-gray-300 rounded-lg shadow-sm focus:border-accent focus:ring focus:ring-accent focus:ring-opacity-50'}),
        }
