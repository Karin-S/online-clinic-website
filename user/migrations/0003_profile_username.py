# Generated by Django 2.1.2 on 2018-10-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181004_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='user1', max_length=10),
        ),
    ]
