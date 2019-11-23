from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

from multiselectfield import MultiSelectField


class User(AbstractUser):
    username = models.CharField("username", max_length=10,  unique=True)
    user_lastname = models.CharField("nom", max_length=10, )
    email = models.EmailField("email", max_length=50, unique=True,)
    password = models.CharField("password", max_length=255,)
    user_birthdate = models.DateField("date d'anniversaire", default=date.today,)
    user_created_on = models.DateField("date de création compte", default=date.today,)
    user_last_login = models.DateField('login', default=date.today)
    user_is_active = models.BooleanField("is active", default=False)  
    is_particular = models.BooleanField(default=False)
    is_enterprise = models.BooleanField(default=False)
    # user_profile_picture = models.ImageField("image de profil du user", upload_to=get_image_path, blank=True, null=True,)

    def __str__(self):
        return self.user_firstname + ' ' + self.user_lastname



class Particular(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Enterprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_address = models.CharField("adresse", max_length=500,)
    room_zipcode = models.CharField("code Postal", max_length=12,)
    room_city = models.CharField("ville", max_length=128,)
    room_title = models.CharField("titre", max_length=500,)
    room_is_active = models.BooleanField("atelier actif")
    room_is_validated = models.BooleanField("atelier valide")
    longitude = models.CharField("longitude", max_length=100)
    latitude = models.CharField("latitude", max_length=100)
    informations = models.TextField("description", max_length=512, blank=True, null=True)
    
    def __str__(self):
        return self.room_title

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    
    
    
    






