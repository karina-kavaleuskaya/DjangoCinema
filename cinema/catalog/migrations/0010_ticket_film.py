# Generated by Django 5.0.3 on 2024-03-16 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_film_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.film'),
            preserve_default=False,
        ),
    ]
