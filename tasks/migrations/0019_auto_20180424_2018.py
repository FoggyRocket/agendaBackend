# Generated by Django 2.0.1 on 2018-04-24 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_auto_20180323_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='expiry',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='starts',
            new_name='start',
        ),
    ]
