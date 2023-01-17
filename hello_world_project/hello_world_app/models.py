from django.db import models
import uuid 
from datetime import datetime

def generate_slug_hash():
    return str(uuid.uuid1())[:8]

def today():
    return datetime.today().date()


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    joined_date = models.DateField(default=today)
    #slug_hash = models.UUIDField(default=uuid.uuid1, null=False)
    slug_hash = models.CharField(max_length=8, default=generate_slug_hash, null=False)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}"
        #return f"{self.firstname}, {self.lastname} - {self.phone} - {self.joined_date}"