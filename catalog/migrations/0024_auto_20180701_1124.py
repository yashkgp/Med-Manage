# Generated by Django 2.0.2 on 2018-07-01 11:24

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20180701_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visited',
            name='doctor_visited',
        ),
        migrations.RemoveField(
            model_name='visited',
            name='prescri',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='doctor',
            new_name='doctor_visited',
        ),
        migrations.AddField(
            model_name='prescription',
            name='date_visited',
            field=models.DateField(default=datetime.date(2018, 7, 1)),
        ),
        migrations.AddField(
            model_name='prescription',
            name='what_for',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='visits',
            field=models.ManyToManyField(to='catalog.Prescription'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='visited',
        ),
    ]
