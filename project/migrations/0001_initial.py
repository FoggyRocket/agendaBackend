# Generated by Django 2.0.1 on 2018-02-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='meeting', to='meeting.Meeting')),
            ],
        ),
    ]