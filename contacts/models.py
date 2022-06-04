from datetime import datetime
from django.db import models

class Contact (models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()

    def __str__(self) -> str:
        return self.name