# Generated by Django 2.1.3 on 2018-11-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0006_alternative_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternative',
            name='n_periods',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
