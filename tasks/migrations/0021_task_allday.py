# Generated by Django 2.0.1 on 2018-05-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_auto_20180424_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='allDay',
            field=models.BooleanField(default=True),
        ),
    ]