# Generated by Django 5.0.3 on 2024-03-16 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_ticket_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user_id',
        ),
    ]
