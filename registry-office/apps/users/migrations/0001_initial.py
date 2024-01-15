# Generated by Django 3.2.19 on 2023-08-10 09:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('descriptiveNumber', models.CharField(max_length=255)),
                ('orientationNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('cityDistrict', models.CharField(blank=True, max_length=255, null=True)),
                ('stateDistrict', models.CharField(max_length=255)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('operationId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('validFrom', models.DateField()),
                ('validSince', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rowCount', models.IntegerField()),
                ('personTypeId', models.IntegerField(choices=[('1', 'Student'), ('2', 'Teacher'), ('3', 'Employee')])),
                ('Userid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('organizationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='organizations.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PersonDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inactiveReasonId', models.IntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('birthName', models.CharField(blank=True, max_length=255, null=True)),
                ('birthOn', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('identificationCode', models.CharField(help_text='Bez lomítka(/)', max_length=10)),
                ('familyStatus', models.IntegerField(blank=True, choices=[('1', 'Single')], null=True)),
                ('identityCardNumber', models.CharField(blank=True, max_length=9, null=True)),
                ('citizenship', models.CharField(max_length=255)),
                ('citizenshipCode', models.CharField(max_length=255)),
                ('insuranceCompany', models.IntegerField(blank=True, null=True)),
                ('validSince', models.DateField()),
                ('validTo', models.DateField(blank=True, null=True)),
                ('birthAddressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personDetailBirth', to='users.address')),
                ('contactAddressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personDetailContact', to='users.address')),
                ('permanentAddressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personDetailPermanent', to='users.address')),
                ('personId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personDetailPerson', to='users.person')),
                ('temporaryAddressId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personDetailTemporary', to='users.address')),
            ],
        ),
    ]
