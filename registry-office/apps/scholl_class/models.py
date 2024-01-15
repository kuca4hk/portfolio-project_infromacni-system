import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ..users.models import Person, PersonDetail
from ..organizations.models import VirtualOperation, Organization
import uuid
from ...functions import choices
from ..ciselniky.models import (KOD_ZAH, KOD_UKON, PRIZN_ST, ZPUSOB, PRERUS, ST_SKOLY, DRST, DELST, FST,
                                FieldLanguage, ForeignLanguage, ExamType, Success, KOD_VETY, ROCNIK, KOD_ZMEN)
from django.core.exceptions import ValidationError


class Class(models.Model):

    name = models.CharField(max_length=255, default="")#nazev tridy
    rowCount = models.IntegerField()#concureny check
    operationId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.rowCount:
            self.rowCount = 0
        super().save(*args, **kwargs)


class StudyField(models.Model):

    name = models.ForeignKey(ST_SKOLY, on_delete=models.CASCADE, related_name="+")#nazev(Gymnazium, ElektroTechnika, ...) #TODO nastavit default hodnotu y tabulkz ST_SKOLY
    code = models.ForeignKey(ST_SKOLY, on_delete=models.CASCADE, related_name="studyFieldST_SKOLY")#kod gymnazia, elektrotechniky, ...
    backkOfficeName = models.CharField(max_length=255, null=True, blank=True)#poznamka
    language_o = models.ForeignKey(FieldLanguage, on_delete=models.CASCADE, related_name="studyFieldFieldLanguage_o")#jazyk o

    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):

    rowCount = models.IntegerField()#TODO dodělat
    personId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='studentPerson')
    organizationId = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="studentOrganization", default=None)#foreign key na operation

    def __str__(self):
        return str(self.personId) #vrazit jmeno a prijmeni

    def save(self, *args, **kwargs):
        student = StudentDetail.objects.filter(StudentId=self.pk)
        if not student:
            self.rowCount = 0
        else:
            self.rowCount = len(student)
        super().save(*args, **kwargs)


class StudentDetail(models.Model):

    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='studentDetailStudent')
    classId = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='studentDetailClass', null=True, blank=True)
    startDate = models.DateField()#datum zacatku studia
    startReason = models.ForeignKey(KOD_ZAH, on_delete=models.CASCADE, related_name="studentDetailKOD_ZAH")#duvod zacatku studia
    obligatorySchoolAttendenceYears = models.CharField(max_length=1, choices=choices.START_CODE)#povinna dochazka
    endDate = models.DateField(null=True, blank=True)#datum ukonceni studia
    endReason = models.ForeignKey(KOD_UKON, on_delete=models.CASCADE, related_name="studentDetailKOD_UKON", null=True, blank=True)#duvod ukonceni studia
    studyFieldId = models.ForeignKey(StudyField, on_delete=models.CASCADE, related_name='studentDetailStudyField')
    focus = models.CharField(max_length=255, blank=True, null=True)#zamereni
    yearsOfStudy = models.CharField(max_length=255, default="9")#doba studia
    grade = models.ForeignKey(ROCNIK, on_delete=models.CASCADE, related_name="+")#rocnik
    formAttendence = models.ForeignKey(PRIZN_ST, on_delete=models.CASCADE, related_name="studentDetailPRIZN_ST")#Dalkove nebo prezencne
    interruption = models.IntegerField(validators=[MaxValueValidator(24), MinValueValidator(0)], default=0)#preruseni
    codeChange = models.ForeignKey(KOD_ZMEN, on_delete=models.CASCADE, related_name="studentDetailKOD_ZMEN", null=True, blank=True)#zmena kodu
    lenghtOfEducationProgram = models.ForeignKey(DELST, on_delete=models.CASCADE, related_name="studentDetailDELST", blank=True, null=True)#doba studia
    kindOfEducation = models.ForeignKey(DRST, on_delete=models.CASCADE, related_name="studentDetailDRST")#typ studia ≈TODO zmenit
    formOfEducation = models.ForeignKey(FST, on_delete=models.CASCADE, default="")
    methodOfSchoolAttendance = models.ForeignKey(ZPUSOB, on_delete=models.CASCADE, related_name="studentDetailZPUSOB")#zpusob studia
    financing = models.IntegerField(editable=False, default=1) #MSMT
    individualPlanId = models.IntegerField(blank=True, null=True)#individualni studijni plan
    codeOfTest = models.CharField(default="", max_length=1, editable=False)#kod testu
    codeRepeat = models.ForeignKey(ExamType, on_delete=models.CASCADE, related_name="studentDetailExamType", blank=True, null=True)#opakovani
    codeLanguageOfGraduation = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, related_name='studentDetailForeignLanguage', null=True, blank=True)
    resultOfGraduation = models.ForeignKey(Success, on_delete=models.CASCADE, related_name="studentDetailSucces", null=True, blank=True)#vysledek
    dateOfGraduation = models.DateField(null=True, blank=True)#datum ukonceni
    seriesOfCertificate = models.CharField(max_length=255, null=True, blank=True)#serie vysvedceni
    numberofCertificate = models.CharField(max_length=255, null=True, blank=True)#cislo vysvedceni
    seriesOfTeachingSheet = models.CharField(max_length=255, null=True, blank=True)#serie vyucovaciho listu
    numberofTeachingSheet = models.CharField(max_length=255, null=True, blank=True)#cislo vyucovaciho listu
    virtualOperationId = models.ForeignKey(VirtualOperation, on_delete=models.CASCADE, related_name='studentDetailVirtualOperation')
    organizationID = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='studentDetailOperation')
    validSince = models.DateField()#platnost od
    validTo = models.DateField(blank=True, null=True)#platnost do
    language_1 = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, related_name='+')#jazyk
    language_2 = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default="0")#jazyk
    language_3 = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default="0")#jazyk
    language_4 = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default="0")#jazyk
    codeSentence = models.ForeignKey(KOD_VETY, on_delete=models.CASCADE, related_name="studentDetailKOD_VETY", null=True, blank=True)#zmena
    zmen_dat = models.DateField(blank=True, null=True)#datum zmeny

    def __str__(self):
        person = self.StudentId.personId
        person_detail = PersonDetail.objects.filter(personId=person.pk).last()
        return f"{person_detail.firstName} {person_detail.lastName}"

    def clean(self):

        if self.endDate and not self.endReason or self.endReason and not self.endDate:
            raise ValidationError('Musíte vyplnit důvod ukončení studia')
        elif self.interruption and not self.validSince:
            raise ValidationError('Musíte vyplnit od kdy je to platné (Interruptin nebo ValidSince)')
        elif self.language_1 == 30 or self.language_2 == 30 or self.language_3 == 30 or self.language_4 == 30:
            raise ValidationError("Nemuzete vyplnit cizí jazyk jako Český jazyk, vyberte neco jineho")




