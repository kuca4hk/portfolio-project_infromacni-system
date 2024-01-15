import unidecode
from django.db import models
from ...apps.organizations.models import Organization
import uuid
from ...functions import choices
from ..ciselniky.models import Sex, KSTPR, STPR, OBECB, OKRESB, ODHL, InsuranceCompany, KOD_UKON, STUPEN
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Address(models.Model):

    street = models.CharField(max_length=255)#"""Ulice"""
    descriptiveNumber = models.CharField(max_length=255)#"""Popisné číslo"""
    orientationNumber = models.CharField(max_length=255, blank=True, null=True)#"""Orientační číslo"""
    city = models.ForeignKey(OBECB, on_delete=models.CASCADE, related_name="adressOBECB")#"""Obec"""
    cityDistrict = models.CharField(max_length=255, blank=True, null=True)#"""Praha 8"""
    stateDistrict = models.CharField(max_length=255, blank=True, null=True)#"""Kraj"""
    region = models.ForeignKey(OKRESB, on_delete=models.CASCADE, related_name="adressOKRESB", blank=True, null=True)#"""Okres"""
    state = models.CharField(max_length=255)#"""Stát"""
    zipCode = models.CharField(max_length=255)#"""PSČ"""
    phoneNumber = models.CharField(max_length=255, blank=True, null=True)#"""Telefonní číslo"""
    email = models.CharField(max_length=255, blank=True, null=True)#"""Email"""
    operationId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    validFrom = models.DateField()#"""Platnost od"""
    validSince = models.DateField(blank=True, null=True)#"""Platnost do"""

    def __str__(self):
        for i in choices.PERMANENT_RESIDENCE:
            if i[0] == self.city:
                self.city = i[1]
        return f"{self.street} {self.city}"


class Person(models.Model):

    rowCount = models.IntegerField()
    organizationId = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='person')
    personTypeId = models.IntegerField(choices=choices.PERSON_TYPE_ID)#choices.PERSON_TYPE
    Userid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        try:
            person = PersonDetail.objects.filter(personId=self.pk).last()
            return f"{person.firstName} {person.lastName}"
        except PersonDetail.DoesNotExist:
            return f"{self.pk}"
        except AttributeError:
            return f"{self.pk}"

    def save(self, *args, **kwargs):
        p = PersonDetail.objects.filter(personId=self.pk)
        if not p:
            self.rowCount = 0
        else:
            self.rowCount = len(p)
        super().save(*args, **kwargs)


class PersonDetail(models.Model):

    personId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='personDetailPerson')
    # operationId = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name='personDetailOperation')
    inactiveReasonId = models.IntegerField(validators=[MaxValueValidator(24), MinValueValidator(0)], default=0) #Preruseni a ukonceni studia
    firstName = models.CharField(max_length=255) #jmeno
    lastName = models.CharField(max_length=255)#prijmeni
    birthName = models.CharField(max_length=255, blank=True, null=True)#rodne prijmeni
    birthOn = models.DateField()#datum narozeni
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='personDetailSex')#pohlavi
    identificationCode = models.CharField(max_length=11, help_text="Bez lomítka(/)")#rodne cislo
    familyStatus = models.IntegerField(blank=True, null=True, choices=choices.FAMILY_STATUS)#rodinny stav choices.FAMILY_STATUS
    identityCardNumber = models.CharField(max_length=11, blank=True, null=True)#cislo OP
    citizenship = models.ForeignKey(STPR, on_delete=models.CASCADE, related_name="personDetailSTPR") #Statni obcanstvi
    citizenshipCode = models.ForeignKey(KSTPR, on_delete=models.CASCADE, related_name="personDetailKSTPR") #Kod statniho obcanstvi
    insuranceCompany = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, related_name="personDetailInsuranceCompany", blank=True, null=True)#Cislo pojistovny
    birthAddressId = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='personDetailBirth', blank=True, null=True)
    permanentAddressId = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='personDetailPermanent')
    temporaryAddressId = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='personDetailTemporary', blank=True, null=True)
    contactAddressId = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='personDetailContact')
    validSince = models.DateField()
    validTo = models.DateField(blank=True, null=True)
    dataBox = models.CharField(max_length=255, blank=True, null=True)
    previousSchool = models.ForeignKey(ODHL, on_delete=models.CASCADE, related_name="personDetailODHL", blank=True, null=True) #Predchozi skola
    education = models.ForeignKey(STUPEN, on_delete=models.CASCADE, related_name="personDetailSTUPEN", blank=True, null=True) #Vzdelani
    previousSchoolCode = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def lower_uni(self):
        return unidecode.unidecode(self.lastName.lower())
