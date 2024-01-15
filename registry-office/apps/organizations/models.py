from django.db import models
import uuid
from ...functions import choices
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..ciselniky.models import OKRESB

# Create your models here.


class Organization(models.Model):

    dataOperationId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)#
    cin = models.CharField(max_length=9, unique=True)#unique red IZO
    icoAuthority = models.IntegerField()#authority
    """Vygenerovano s Marketou"""
    osszName = models.CharField(max_length=255)#nazev ossz
    osszDistrictId = models.ForeignKey(OKRESB, on_delete=models.CASCADE, related_name="+", blank=True, null=True)#okres choice. okresy jsou v tabulce district
    osszVariableSymbol = models.CharField(max_length=255)#variabilni symbol
    name = models.CharField(max_length=255)#nazev
    uniqueCode = models.CharField(max_length=255)#unique code IZO
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if self.dataOperationId is None and self.uniqueCodeCategoryId is None:
        #     self.dataOperationId = uuid.uuid4()
        #     self.uniqueCodeCategoryId = uuid.uuid4()
        super().save(*args, **kwargs)


class VirtualOperation(models.Model):

    uniqueCode = models.CharField(max_length=255)#unique code IZO skoly predtim
    codeTypeId = models.IntegerField(choices=choices.CODE_TYPE_ID)#typ kodu choice. (vyresim jeste s ladou)

    def __str__(self):
        return self.uniqueCode
