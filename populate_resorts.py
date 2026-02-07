import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservation.settings')
django.setup()

from core.models import Resort, RoomType, Room

# Data to populate
resorts_data = [
    {
        "name": "Crimson Resort & Spa",
        "location": "Boracay",
        "description": "Escape to a private paradise where the sea meets the sky. Experience world-class luxury on the pristine white sands of Boracay.",
        "image_url": "https://images.unsplash.com/photo-1540541338287-41700207dee6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
    },
    {
        "name": "The Manor at Camp John Hay",
        "location": "Baguio",
        "description": "Experience the old-world charm and cool mountain breeze of the City of Pines. A perfect retreat for relaxation and romance.",
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" # Reusing a nice hotel image
    },

    {
        "name": "Sagada Heritage Geuast House",
        "location": "Sagada",
        "description": "Wake up to a sea of clouds. Immerse yourself in the rich culture and breathtaking nature of the Cordilleras.",
        "image_url": "https://images.unsplash.com/photo-1518684079-3c830dcef090?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" # Mountain view
    },
    {
        "name": "Kahuna Beach Resort and Spa",
        "location": "La Union",
        "description": "Where surf meets luxury. Enjoy the best waves and the most relaxing spa treatments in the North.",
        "image_url": "https://images.unsplash.com/photo-1437719417032-8595fd9e9dc6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" # Beach sunset
    },
    {
        "name": "Hennan Resort Alona Beach",
        "location": "Bohol",
        "description": "Discover the beauty of Bohol with premium accommodations right on the famous Alona Beach.",
        "image_url": "https://images.unsplash.com/photo-1582719508461-905c673771fd?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
    },
    {
        "name": "Nay Palad Hideaway",
        "location": "Siargao",
        "description": "Barefoot luxury at its finest. Experience the island life in a resort that feels like home.",
        "image_url": "https://images.unsplash.com/photo-1540541338287-41700207dee6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80" 
    },
        {
        "name": "Movenpick Hotel Mactan",
        "location": "Cebu",
        "description": "A Mediterranean-inspired beachfront hotel with contemporary style and fun-filled activities.",
        "image_url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
    },
    {
        "name": "El Nido Resorts",
        "location": "Palawan",
        "description": "Eco-luxury island resorts set in the spectacular limestone islands of El Nido.",
        "image_url": "https://images.unsplash.com/photo-1551632811-561732d1e306?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
    }


]

# Create Resorts and dummy rooms
for data in resorts_data:
    resort, created = Resort.objects.get_or_create(
        name=data['name'],
        defaults={
            'location': data['location'],
            'description': data['description'],
            'image_url': data['image_url']
        }
    )
    if created:
        print(f"Created resort: {resort.name}")
        
        # Create standard room types for the new resort
        deluxe, _ = RoomType.objects.get_or_create(name="Deluxe Room", defaults={"description": "Spacious room with ocean view", "capacity": 2, "price": 5000})
        suite, _ = RoomType.objects.get_or_create(name="Suite", defaults={"description": "Luxury suite with private balcony", "capacity": 4, "price": 10000})
        
        # Create some rooms
        for i in range(1, 4):
            Room.objects.create(resort=resort, room_type=deluxe, number=f"10{i}")
        for i in range(1, 3):
            Room.objects.create(resort=resort, room_type=suite, number=f"20{i}")
            
    else:
        print(f"Resort already exists: {resort.name}")

print("Population complete!")
