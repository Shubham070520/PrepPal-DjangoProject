# Generated by Django 5.1 on 2024-09-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='test_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='test_score',
            field=models.FloatField(default=0),
        ),
    ]
