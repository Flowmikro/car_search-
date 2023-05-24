import random
import string
from django.db import models


class TruckModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.sku:
            self.sku = self.random_sku()
            self.location = self.random_location()

    def random_sku(self):
        num = random.randint(1000, 9999)
        letter = random.choice(string.ascii_uppercase)
        return f"{num}{letter}"

    def random_location(self):
        with open('C:/Users/islam/car_search-/uszips.csv') as f:
            lines = f.readlines()
        line = random.choice(lines)
        zip_code, lat, lng, city, state, *_ = line.split(',')
        return {
            'zip_code': zip_code,
            'city': city,
            'state': state,
            'lat': lat,
            'lng': lng,
        }

    def save(self, *args, **kwargs):
        if not self.location:
            location_data = self.random_location()
            self.location = f"{location_data['zip_code']}, {location_data['city']}, {location_data['state']}, {location_data['lat']}, {location_data['lng']}"
        super().save(*args, **kwargs)

    location = models.CharField(max_length=255, blank=True, null=True)
    load_capacity = models.PositiveSmallIntegerField()
    sku = models.CharField(max_length=5, unique=True, blank=True)


