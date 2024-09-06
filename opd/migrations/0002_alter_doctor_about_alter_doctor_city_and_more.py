# Generated by Django 5.1 on 2024-09-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=0, verbose_name='Year of Experience'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, max_length=200, verbose_name='Speciality'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='street_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Street Address'),
        ),
    ]