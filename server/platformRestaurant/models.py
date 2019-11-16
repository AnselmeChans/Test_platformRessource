from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

from multiselectfield import MultiSelectField





class User(AbstractUser):
    user_firstname = models.CharField("prénom", max_length=200, )
    user_lastname = models.CharField("nom", max_length=200, )
    user_email = models.EmailField("email", max_length=70, unique=True,)
    user_password = models.CharField("password", max_length=50,)
    user_birthdate = models.DateField("date d'anniversaire")
    user_created_on = models.DateField("date de création compte", default=date.today,)
    user_last_login = models.DateField('login', default=date.today)
    user_is_active = models.BooleanField("is active", default=False)  
    is_particular = models.BooleanField()
    is_enterprise = models.BooleanField()
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
    room_description = models.TextField("description", max_length=512, blank=True, null=True)
    room_informations_pratiques = models.TextField("informations pratiques", max_length=1024, blank=True, null=True)
    room_is_active = models.BooleanField("atelier actif")
    room_is_validated = models.BooleanField("atelier valide")
    
    def __str__(self):
        return self.room_title






