# Generated by Django 2.1.3 on 2018-11-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternative',
            name='interest_type',
            field=models.CharField(choices=[('period', 'p'), ('effective', 'e'), ('nominal', 'n')], default='nominal', max_length=10),
        ),
        migrations.AlterField(
            model_name='alternative',
            name='interest',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
