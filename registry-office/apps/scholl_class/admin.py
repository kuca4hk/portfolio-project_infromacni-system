import copy
import json

from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Class, StudyField, StudentDetail
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin, ExportActionMixin
import datetime
from ...functions import functions as f
from ...apps.organizations.models import Organization
from ...apps.users.models import Person, PersonDetail
# Register your models here.


class StudentResource(resources.ModelResource):
    full = resources.Field()

    class Meta:
        model = StudentDetail
        formats = ['json']
        fields = ()

    def dehydrate_full(self, student_detail):

        person_detail = PersonDetail.objects.get(personId=student_detail.StudentId.personId)
        # Převedení dat do JSON formátu
        student_sentence = {
            # "RDAT": f.time_format(datetime.datetime.now()),
            "RDAT": "30.09.2023",
            "IZO": student_detail.organizationID.uniqueCode,
            "CAST": "01",
            "RODC": str(person_detail.identificationCode) if person_detail.identificationCode is not None else "",
            "POHLAVI": person_detail.sex.id if person_detail.sex is not None else "",
            "DAT_NAROZ": f.date_convert(person_detail.birthOn),
            "KSTPR": person_detail.citizenshipCode.id if person_detail.citizenshipCode is not None else "",
            "STPR": person_detail.citizenship.id if person_detail.citizenship is not None else "",
            "OBECB": person_detail.permanentAddressId.city.id if person_detail.permanentAddressId.city is not None else "",
            "OKRESB": person_detail.permanentAddressId.region.id if person_detail.permanentAddressId.region is not None else "",
            "ODHL": person_detail.previousSchool.id if person_detail.previousSchool is not None else "",
            "IZOZ": person_detail.previousSchoolCode if person_detail.previousSchoolCode is not None else "",
            "STUPEN": person_detail.education.id if person_detail.education is not None else "",
            "ZAHDAT": f.time_format(person_detail.validSince),
            "KOD_ZAH": student_detail.startReason.id if student_detail.startReason is not None else "",
            "UKONDAT": f.time_format(student_detail.endDate),
            "KOD_UKON": student_detail.endReason.id if student_detail.endReason is not None else "",
            "LET_PSD": student_detail.yearsOfStudy if student_detail.yearsOfStudy is not None else "",
            "ROCNIK": student_detail.grade.id if student_detail.grade is not None else "",
            "PRIZN_ST": student_detail.formAttendence.id if student_detail.formAttendence is not None else "",
            "ZPUSOB": student_detail.methodOfSchoolAttendance.id if student_detail.methodOfSchoolAttendance is not None else "",
            "PRERUS": student_detail.interruption if student_detail.interruption is not None else "",
            "TRIDA": student_detail.classId.name if student_detail.classId is not None else "",
            "OBOR": student_detail.studyFieldId.code.id if student_detail.studyFieldId is not None else "",
            "DRST": student_detail.kindOfEducation.id if student_detail.kindOfEducation is not None else "",
            "DELST": student_detail.lenghtOfEducationProgram.id if student_detail.lenghtOfEducationProgram is not None else "",
            "FST": student_detail.formOfEducation.id if student_detail.formOfEducation is not None else "",
            "JAZYK_O": student_detail.studyFieldId.language_o.id if student_detail.studyFieldId is not None else "",
            "JAZ1": "02",
            "JAZ2": student_detail.language_2.id if student_detail.language_2 is not None else "",
            "JAZ3": "",
            "JAZ4": "",
            "FIN": student_detail.financing,
            "KOD_ZK": "",
            "KOD_OPK": student_detail.codeRepeat.id if student_detail.codeRepeat else "",
            "JAZM": student_detail.codeLanguageOfGraduation.id if student_detail.codeLanguageOfGraduation is not None else "",
            "VYSLCELK": student_detail.resultOfGraduation.id if student_detail.resultOfGraduation is not None else "",
            "ZKDAT": f.time_format(student_detail.dateOfGraduation),
            "SERIE_V": str(student_detail.seriesOfCertificate) if student_detail.seriesOfCertificate is not None else "",
            "CISLO_V": str(student_detail.numberofCertificate) if student_detail.numberofCertificate is not None else "",
            "SERIE_L": str(student_detail.seriesOfTeachingSheet) if student_detail.seriesOfTeachingSheet is not None else "",
            "CISLO_L": str(student_detail.numberofTeachingSheet) if student_detail.numberofTeachingSheet is not None else "",
            "KOD_ZMEN": student_detail.codeChange.id if student_detail.codeChange is not None else "",
            "ZMENDAT": f.time_format(student_detail.zmen_dat),
            "KOD_VETY": student_detail.codeSentence.id if student_detail.codeSentence is not None else "",
            "PLAT_ZAC": f.time_format(student_detail.validSince),
            "PLAT_KON": f.time_format(student_detail.validTo)
        }

        # print(data)
        return student_sentence


@admin.register(StudentDetail)
class StudentDetailAdmin(ExportMixin, admin.ModelAdmin):
    # actions = ['export_as_json']
    resource_class = StudentResource


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    readonly_fields = ['rowCount']


@admin.register(StudyField)
class StudyFieldAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['rowCount']

