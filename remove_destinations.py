import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservation.settings')
django.setup()

from core.models import Resort

locations_to_remove = ["Dubai", "UAE", "Samal", "Swiss Alps", "Maldives"]

for loc in locations_to_remove:
    # Use icontains to be safe against formatting differences
    resorts = Resort.objects.filter(location__icontains=loc)
    count = resorts.count()
    if count > 0:
        print(f"Deleting {count} resorts with location matching '{loc}'")
        resorts.delete()
    else:
        print(f"No resorts found matching '{loc}'")

print("Cleanup complete.")
