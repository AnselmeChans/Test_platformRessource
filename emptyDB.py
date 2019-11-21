# -*- coding: utf-8 -*-
from psycopg2.extensions import AsIs
import django
from django.db import connection
import sys
import os
import datetime
import random
from lorem.text import TextLorem
from faker import Faker
fake = Faker('fr_Fr')
from platformRestaurant.models import User, Room, Info




def create_user():
    cursor = connection.cursor()
    cursor.execute("create user %s with password %s", (AsIs('hansouu'), 'guadeloupe=>1992==>hansUndFranz==>Twin!!',))
    

def django_setup():
    sys.path.append(os.path.join(os.curdir, 'server'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    django.setup()


django_setup()


def emptyDB():
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE platformRestaurant_user CASCADE;")
    cursor.execute("ALTER SEQUENCE platformRestaurant_user_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE platformRestaurant_user_room_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE platformRestaurant_user_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE platformRestaurant_info_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE platformRestaurant_room_info_id_seq RESTART WITH 1")
    print("Terminé ! La BDD est vide")

django_setup()


def getDateFromAnotherDate(date, days_after_today=0):
    return date + datetime.timedelta(days=days_after_today)


def removeSpaces(string_with_space):
    parts_of_string = string_with_space.split(' ')
    return ''.join(parts_of_string)


def createFakerUserData():
    
    fake_name = fake.name()
    email = random.choice(["@gmail.com", "@protonmail.com"])
    username = fullname.split(' ')[0]
    user_lastname = fake_name.split(' ')[1]

    def passwordGeneration(length):
        if not isinstance(length, int) or length < 8:
            raise ValueError("temp password must have positive length")

        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        return ''.join(random.choice(chars) for _ in range(length))

    # Création du user dans la BDD
    user = User.objects.create(
        username=username,
        user_lastname=user_lastname,
        email=(random.choice(username) + str(random.randint(0, 9)) + user_lastname+email).lower(),
        password=passwordGeneration(10),
        user_birthdate=fake.profile()["birthdate"],
        user_created_on=fake.date_time_between(
                                                start_date="-30y", 
                                                end_date="now", 
                                                tzinfo=None).date(),
        user_last_login=datetime.datetime.now().date(),
        user_is_active=random.choice([True, False]),
        is_particular=random.choice([True, False]),
        is_enterprise=random.choice([True, False])
    )
    return user


def createFakerRoom(user_id):
    
    lorem = TextLorem(wsep=' ', srange=(2, 6))
    nb_days = random.randint(1, 3)
    nb_hours = nb_days * 7
    room = Room.objects.create(
        user=user_id,
        room_address=fake.address(),
        room_zipcode=removeSpaces(fake.postcode()),
        room_city=fake.city(),
        room_title=lorem.sentence(),
        room_is_active=random.choice([True, False]),
        room_is_validated=random.choice([True, False])
    )
    return room




def createFakerInfo(room_id):
    lorem = TextLorem(wsep=' ', srange=(2, 10))
    
    google_map_list = [
        'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1123.3850145412064!2d37.600589158335865!3d55.72774864513666!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54b0be3ac9d11%3A0x735806d25b3bdc55!2z0JzRg9C30LXQuSDRgdC-0LLRgNC10LzQtdC90L3QvtCz0L4g0LjRgdC60YPRgdGB0YLQstCwIMKr0JPQsNGA0LDQtsK7!5e0!3m2!1sru!2sru!4v1547763408711', 
        'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1530.8494832689219!2d37.59693065124095!3d55.74157162835216!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54baea59877dd%3A0xb4d0c3eb557a1c98!2zwqvQnNCe0KHQmtCe0JLQodCa0JjQmSDQlNCe0Jwg0KTQntCi0J7Qk9Cg0JDQpNCY0JjCuw!5e0!3m2!1sru!2sru!4v1547845790316',
         'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d17967.866965087615!2d37.60335432286895!3d55.74141791432578!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb9384e1a3b2da434!2z0JPQvtGB0YPQtNCw0YDRgdGC0LLQtdC90L3Ri9C5INC80YPQt9C10Lkg0JAu0KEuINCf0YPRiNC60LjQvdCw!5e0!3m2!1sru!2sru!4v1547878731704',
         'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2245.9848620916428!2d37.618675215617316!3d55.741392000339864!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54afe32078357%3A0xa50d6e8b9a7b028f!2z0JPQvtGB0YPQtNCw0YDRgdGC0LLQtdC90L3QsNGPINCi0YDQtdGC0YzRj9C60L7QstGB0LrQsNGPINCz0LDQu9C10YDQtdGP!5e0!3m2!1sru!2sru!4v1547878659681',
        'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2245.9763498372804!2d37.59654121561725!3d55.741539900328505!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54baea59877dd%3A0xb4d0c3eb557a1c98!2zwqvQnNCe0KHQmtCe0JLQodCa0JjQmSDQlNCe0Jwg0KTQntCi0J7Qk9Cg0JDQpNCY0JjCuw!5e0!3m2!1sru!2sru!4v1547878587877', 
        'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2244.397087990157!2d37.62463341561838!3d55.76897499821247!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54a68e2e342b7%3A0x934bc1e9948c826b!2z0KbQtdC90YLRgCDQnNCw0YDRgQ!5e0!3m2!1sru!2sru!4v1547878491776'
    ]

    info = Info.objects.create(
        room=room.id
        map_google= random.choice(google_map_list)
        information=lorem.sentence(),
    )
    return info



def createFakeData():
    list_users = []
    list_info = []
    list_room = []

    # Crée 10 users
    for i in range(10):
        user = createFakerUserData()
        list_users.append(user)
        
        info = createFakerInfo()

        # 5 users ont réservés une salle de restaurant
        if i < 5:
            room = createFakerRoom(user.id)
            list_room.append(room)

            

    # Création de 0 à 2 commentaires par user
    for user in list_users:
        for _ in range(random.randint(0, 3)):
            createFakerComment(user.id, random.choice(list_ateliers).id)

    # Création de 0 à 4 réservations par user
    for user in list_users:
        for _ in range(random.randint(0, 4)):
            createFakerReservation(user.id, random.choice(list_sessions))

    # Création des catégories et des sous-catégories liées
    list_sub_categories = createCategoriesAndSubcategories()

    # Liaison des ateliers à des sous-catégories
    createSubcategoriesAteliers(list_ateliers, list_sub_categories)

    print("Terminé ! La BDD a été remplie")

