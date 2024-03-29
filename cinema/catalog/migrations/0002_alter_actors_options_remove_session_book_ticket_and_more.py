# Generated by Django 5.0.3 on 2024-03-16 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actors',
            options={'verbose_name_plural': 'Actors'},
        ),
        migrations.RemoveField(
            model_name='session',
            name='book_ticket',
        ),
        migrations.RemoveField(
            model_name='session',
            name='price',
        ),
        migrations.AddField(
            model_name='actors',
            name='image',
            field=models.ImageField(default=None, upload_to='media/actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='age',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(default=None, upload_to='media/film'),
        ),
        migrations.AddField(
            model_name='producer',
            name='image',
            field=models.ImageField(default=None, upload_to='media/producer'),
        ),
        migrations.AddField(
            model_name='session',
            name='hall',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='timetable',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Available', 'Available'), ('On Loan', 'On Loan')], default='Available', max_length=50)),
                ('seat', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=13)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.session')),
            ],
        ),
    ]
