import csv
import random

from django.db import models


class CargoModel(models.Model):
    pick_up = models.CharField(max_length=155)
    delivery = models.CharField(max_length=155)
    weight = models.PositiveSmallIntegerField()
    description = models.TextField()


class CargoModelTest(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.pick_up:
            self.pick_up = self.random_location()

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
        if not self.pick_up:
            location_data = self.random_location()
            self.pick_up = f"{location_data['zip_code']}, {location_data['city']}, {location_data['state']}, {location_data['lat']}, {location_data['lng']}"
        super().save(*args, **kwargs)

    weight = models.PositiveSmallIntegerField()
    description = models.TextField()
    pick_up = models.CharField(max_length=255, blank=True, null=True)


class CargoModeTEstTEst(models.Model):
    weight = models.PositiveSmallIntegerField()
    description = models.TextField()
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    pick_up = models.BooleanField(default=False)

    def fill_location_data(self):
        with open('C:/Users/islam/car_search-/uszips.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['zip'] == self.zip_code:
                    self.city = row['city']
                    self.state = row['state_name']
                    self.lat = row['lat']
                    self.lng = row['lng']
                    break

    def save(self, *args, **kwargs):
        if not self.pick_up:
            self.fill_location_data()
            self.pick_up = True
        super().save(*args, **kwargs)