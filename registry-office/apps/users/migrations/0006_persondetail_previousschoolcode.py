# Generated by Django 3.2.19 on 2023-09-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20230903_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondetail',
            name='previousSchoolCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
