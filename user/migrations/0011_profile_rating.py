# Generated by Django 2.1.2 on 2018-10-20 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20181010_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
