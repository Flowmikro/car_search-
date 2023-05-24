import csv
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

def get_random_location():
    with open('C:/Users/islam/car_search-/uszips.csv') as f:
        reader = csv.DictReader(f)
        row = random.choice(list(reader))
        return {
            'zip': row['zip'],
            'city': row['city'],
            'state_name': row['state_name'],
            'lat': row['lat'],
            'lng': row['lng'],
        }

class TruckModelTest(models.Model):
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.random_sku()
        if not self.zip:
            location_data = get_random_location()
            self.zip = location_data['zip']
            self.city = location_data['city']
            self.state_name = location_data['state_name']
            self.lat = location_data['lat']
            self.lng = location_data['lng']

        super().save(*args, **kwargs)

    def random_sku(self):
        num = random.randint(1000, 9999)
        letter = random.choice(string.ascii_uppercase)
        return f"{num}{letter}"

    load_capacity = models.PositiveSmallIntegerField()
    sku = models.CharField(max_length=5, unique=True, blank=True)

    zip = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state_name = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)




