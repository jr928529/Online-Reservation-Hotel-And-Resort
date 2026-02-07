import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservation.settings')
django.setup()

from core.models import Resort

print("Remaining unique locations:")
locations = Resort.objects.values_list('location', flat=True).distinct()
for loc in locations:
    print(f"- {loc}")
