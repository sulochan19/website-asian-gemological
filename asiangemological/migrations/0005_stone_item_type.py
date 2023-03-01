# Generated by Django 4.1.7 on 2023-03-01 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asiangemological', '0004_alter_stone_color_alter_stone_dimension_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stone',
            name='item_type',
            field=models.CharField(choices=[('Gemstone', 'Gemstone'), ('Jewelry', 'Jewelry'), ('Rudrakshya', 'Rudrakshya')], default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]