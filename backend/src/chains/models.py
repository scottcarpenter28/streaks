from django.db import models
from django.contrib.auth.models import User


FREQUENCIES = {
    "D": "Daily",
    "ND": "Number of times per day",
    "W": "Weekly",
    "NW": "N days per week",
    "M": "Monthly",
    "NM": "N days per month"
}


class Chain(models.Model):
    name = models.CharField(max_length=64)
    frequency = models.CharField(max_length=64, choices=FREQUENCIES)
    frequency_count = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class EntryDate(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    entry_date = models.DateField(auto_now_add=True)
