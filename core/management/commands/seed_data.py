from django.core.management.base import BaseCommand
from core.models import Resort, RoomType, Room

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Resorts
        resorts_data = []

        for r_data in resorts_data:
            resort, created = Resort.objects.get_or_create(
                name=r_data['name'],
                defaults=r_data
            )
            if created:
                self.stdout.write(f'Created resort: {resort.name}')
            else:
                self.stdout.write(f'Resort already exists: {resort.name}')

            # Create Room Types for each Resort
            room_types_data = [
                {'name': 'Standard Suite', 'description': 'Comfortable suite with all amenities.', 'capacity': 2, 'price': 200.00},
                {'name': 'Deluxe Ocean View', 'description': 'Spacious room with a stunning view.', 'capacity': 2, 'price': 350.00},
                {'name': 'Family Villa', 'description': 'Perfect for families, includes dual bedrooms.', 'capacity': 4, 'price': 500.00},
            ]

            for rt_data in room_types_data:
                room_type, created = RoomType.objects.get_or_create(
                    name=rt_data['name'],
                    capacity=rt_data['capacity'],
                    defaults=rt_data
                )

                # Create Rooms
                for i in range(1, 6): # 5 rooms per type per resort
                    room_number = f"{resort.name[:3].upper()}-{room_type.name[:3].upper()}-{i:02d}"
                    Room.objects.get_or_create(
                        resort=resort,
                        room_type=room_type,
                        number=room_number
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
