# Generated by Django 3.2.19 on 2023-09-07 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholl_class', '0009_alter_studentdetail_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='interruption',
            field=models.IntegerField(verbose_name=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)])),
        ),
    ]
