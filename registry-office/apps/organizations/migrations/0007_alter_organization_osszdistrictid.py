# Generated by Django 3.2.19 on 2023-09-03 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciselniky', '0001_initial'),
        ('organizations', '0006_alter_organization_osszdistrictid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='osszDistrictId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.okresb'),
        ),
    ]