# Generated by Django 5.0.3 on 2024-03-17 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_ticket_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='age',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
