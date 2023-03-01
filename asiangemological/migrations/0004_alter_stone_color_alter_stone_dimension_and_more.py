# Generated by Django 4.1.7 on 2023-02-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asiangemological', '0003_alter_stone_item_described_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='stone',
            name='dimension',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='stone',
            name='identified_as',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='stone',
            name='item_described',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='stone',
            name='shape',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='stone',
            name='weight',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]