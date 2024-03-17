import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'cinema.settings')
django.setup()


from catalog.models import Genre, Actors, Producer, Film
from faker import Faker


fake = Faker()


for _ in range(5):
    genre_name = fake.word()
    Genre.objects.create(name=genre_name)

genres = Genre.objects.all()

