# Generated by Django 5.0.3 on 2024-03-16 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_film_actors_film_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
