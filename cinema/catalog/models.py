from django.db import models
from user.models import CustomUser
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actors(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='media/actor', default=None)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    class Meta:
        verbose_name_plural = 'Actors'

    def get_absolute_url(self):
        return reverse('actor-detail', args=[self.pk])


class Producer(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='media/producer', default=None)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    def get_absolute_url(self):
        return reverse('producer-detail', args=[self.pk])


class Film(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField()
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actors)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to='media/film', default=None)

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[self.pk])


class Session(models.Model):
    hall = models.CharField(max_length=5)
    timetable = models.CharField(max_length=20)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('session-detail', args=[self.pk])


class Ticket(models.Model):
    STATUSES = (
        ('Available', 'Available'),
        ('On Loan', 'On Loan'),
    )
    status = models.CharField(choices=STATUSES, max_length=50, default='Available')
    seat = price = models.CharField(max_length=10)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    isbn = models.CharField(max_length=13)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    borrower = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('ticket-detail', args=[self.pk])



