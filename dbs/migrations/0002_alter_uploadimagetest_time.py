# Generated by Django 3.2.7 on 2022-10-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimagetest',
            name='time',
            field=models.TimeField(default='12:37:51'),
        ),
    ]
