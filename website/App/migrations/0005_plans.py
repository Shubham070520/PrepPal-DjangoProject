# Generated by Django 5.1 on 2024-09-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_exam_exam_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
