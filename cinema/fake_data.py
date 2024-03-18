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

producers = []
for _ in range(5):
    producer_data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=40),
        'image': fake.image_url()
    }

    if fake.random_int(min=0, max=7):
        producer_data['date_of_death'] = fake.date_of_birth(minimum_age=1, maximum_age=40)

    producers.append(producer_data)

    Producer.objects.create(**producer_data)


for _ in range(5):
    film_data = {
        'title': fake.sentence(nb_words=3, variable_nb_words=True),
        'description': fake.paragraph(),
        'age': fake.random_int(min=0, max=18),
        'image': fake.image_url(),
        'producer': fake.random_element(elements=producers),
        'actors': fake.random_elements(elements=actors_data),
        'genre': fake.random_elements(elements=genres)
    }


    film = Film.objects.create(**film_data)
