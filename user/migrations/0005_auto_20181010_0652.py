# Generated by Django 2.1.2 on 2018-10-10 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181010_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
