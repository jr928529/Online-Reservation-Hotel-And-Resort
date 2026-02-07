import os
import sys

# Path to your project directory
sys.path.insert(0, os.getcwd())

# Path to your settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'hotel_reservation.settings'

from hotel_reservation.wsgi import application
