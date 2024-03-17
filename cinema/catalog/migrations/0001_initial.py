# Generated by Django 5.0.3 on 2024-03-07 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('date_of_death', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('date_of_death', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField()),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.actors')),
                ('genre', models.ManyToManyField(to='catalog.genre')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.producer')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=20)),
                ('timetable', models.DateTimeField(blank=True, null=True)),
                ('book_ticket', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=50)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.film')),
            ],
        ),
    ]