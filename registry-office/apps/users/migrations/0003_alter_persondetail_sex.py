# Generated by Django 3.2.19 on 2023-08-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230824_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')]),
        ),
    ]
