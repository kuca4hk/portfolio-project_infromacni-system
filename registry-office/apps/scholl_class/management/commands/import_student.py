import datetime

import pandas as pd
from django.core.management import BaseCommand
from ...models import ForeignLanguage
from ...models import Student, StudentDetail, StudyField, Class
from ...models import Person, PersonDetail, Organization, VirtualOperation
from ...models import (FieldLanguage, ExamType, Success, KOD_VETY, ROCNIK, KOD_ZMEN, KOD_ZAH, KOD_UKON, PRIZN_ST, ZPUSOB,
                       PRERUS, ST_SKOLY, DRST, DELST, FST)
from ....ciselniky.models import Sex, InsuranceCompany, OKRESB, OBECB, STUPEN, KSTPR, ODHL, STPR
from ....users.models import Address


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        def extrahovat_text_a_cisla(pred_text):
            # Rozdělit řetězec na části podle čárky
            casti = pred_text.split(',')

            if len(casti) >= 2:
                text_pred_carkou = casti[0].strip()  # Extrahovat text a odstranit mezery na začátku a konci
                cisla_pred_carkou = casti[1].strip()  # Extrahovat čísla a odstranit mezery na začátku a konci

                return text_pred_carkou, cisla_pred_carkou
            else:
                # Pokud v řetězci není čárka, vrátíme None pro oba části
                return None, None

        file_path = "C:/Users/Jakub Kucera/Desktop/Projects/ITG/registry-office/registry-office/functions/ciselniky/person_v5.xlsx"
        try:

            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                surname = str(row.values[0]) if str(row.values[0]) != "nan" else None
                name = row.values[1] if str(row.values[1]) != "nan" else None
                emial = row.values[2] if str(row.values[2]) != "nan" else None
                parrentfamily1 = row.values[3] if str(row.values[3]) != "nan" else None
                parrentfamily2 = row.values[4] if str(row.values[4]) != "nan" else None
                phoneNumber = int(row.values[5]) if str(row.values[5]) != "nan" else None
                adress_street = row.values[9] if str(row.values[9]) != "nan" else None
                insurancecode = int(row.values[11]) if str(row.values[11]) != "nan" else None
                datelastreport = row.values[12] if str(row.values[12]) != "nan" else None
                codeofschool = str(row.values[13]) if str(row.values[13]) != "nan" else None
                castofschool = int(row.values[14]) if str(row.values[14]) != "nan" else None
                identificationnumber = int(row.values[15]) if str(row.values[15]) != "nan" else None
                # birthnumber = row.values[15] if str(row.values[15]) != "nan" else None
                sex = str(row.values[16]) if str(row.values[16]) != "nan" else None
                birtDate = row.values[17] if str(row.values[17]) != "nan" else None
                citizenshipcode = row.values[18] if str(row.values[18]) != "nan" else None
                citizenshipid = str(row.values[19]) if str(row.values[19]) != "nan" else None
                # previousSchool = row.values[19] if str(row.values[19]) != "nan" else None
                # previousSchoolCode = int(row.values[20]) if str(row.values[20]) != "nan" else None
                # educationid = str(row.values[21]) if str(row.values[21]) != "nan" else None
                city = str(row.values[20]) if str(row.values[20]) != "nan" else None
                okres = str(row.values[21]) if str(row.values[21]) != "nan" else None
                previousSchool = str(row.values[22]) if str(row.values[22]) != "nan" else None
                izoz = str(row.values[23]) if str(row.values[23]) != "nan" else None
                startReason = row.values[24] if str(row.values[24]) != "nan" else None
                validSince = row.values[25] if str(row.values[25]) != "nan" else None
                education_v2 = str(row.values[26]) if str(row.values[26]) != "nan" else None
                enddate = str(row.values[27]) if str(row.values[27]) != "NaT" else None
                endreason = row.values[28] if str(row.values[28]) != "nan" else None
                methodOfSchoolAttendace = row.values[29] if str(row.values[29]) != "nan" else None
                interruption = row.values[30] if str(row.values[30]) != "nan" else None
                classId = row.values[31] if str(row.values[31]) != "nan" else None
                studyFiledId = row.values[32] if str(row.values[32]) != "nan" else None
                kindOfEducation = row.values[33] if str(row.values[33]) != "nan" else None
                name_of_class = row.values[34] if str(row.values[34]) != "nan" else None
                lenghtOfEducationProgramId = row.values[35] if str(row.values[35]) != "nan" else None
                formOfEducation = row.values[36] if str(row.values[36]) != "nan" else None
                language_o = row.values[37] if str(row.values[37]) != "nan" else None
                language_1 = row.values[38] if str(row.values[38]) != "nan" else None
                language_2 = row.values[39] if str(row.values[39]) != "nan" else None
                language_3 = int(row.values[40]) if str(row.values[40]) != "nan" else None
                language_4 = int(row.values[41]) if str(row.values[41]) != "nan" else None
                financing = row.values[42] if str(row.values[42]) != "nan" else None
                kod_zk = row.values[43] if str(row.values[43]) != "nan" else None
                codeReapet = row.values[44] if str(row.values[44]) != "nan" else None
                codeLanguageOfGraduation = row.values[45] if str(row.values[45]) != "nan" else None
                resultOfGraduation = row.values[46] if str(row.values[46]) != "nan" else None
                resultOfGraduationId = row.values[47] if str(row.values[47]) != "nan" else None
                dateOfGraduation = row.values[48] if str(row.values[48]) != "nan" else None
                seriesofCertificate = row.values[49] if str(row.values[49]) != "nan" else None
                numberofCertificate = row.values[50] if str(row.values[50]) != "nan" else None
                seriesofTeachingSheet = row.values[51] if str(row.values[51]) != "nan" else None
                numberofTeachingSheet = row.values[52] if str(row.values[52]) != "nan" else None
                codechange = row.values[54] if str(row.values[54]) != "nan" else None
                dateofchange = row.values[55] if str(row.values[55]) != "NaT" else None
                codeSentence = row.values[56] if str(row.values[56]) != "nan" else None
                validSince_v2 = row.values[57] if str(row.values[57]) != "nan" else None
                validTo = row.values[58] if str(row.values[58]) != "NaT" else None
                identificationnumber = str("0" + str(identificationnumber))
                print(identificationnumber)
                try:
                    person_detail_identification_number = PersonDetail.objects.filter(
                        identificationCode=identificationnumber).last()
                    student_id_number = Student.objects.filter(personId=person_detail_identification_number.id).first()
                except Exception as e:
                    print(e)
                    person_detail_identification_number = None
                    student_id_number = None

                if language_3 == "2":
                    language_3 = "02"

                ulice, mesto = extrahovat_text_a_cisla(adress_street)
                print(ulice, mesto)

                organization = Organization.objects.all().first()
                print(organization)
                print(isinstance(organization, Organization))

                education = STUPEN.objects.filter(name=startReason).first()
                class_id = Class.objects.filter(name=name_of_class).first()
                code_of_start = KOD_ZAH.objects.filter(name=education_v2).first()
                print(code_of_start)
                studyfiled = StudyField.objects.filter(name=lenghtOfEducationProgramId).first()
                sex_id = Sex.objects.get(name=sex)
                try:
                    insuranceCompany = InsuranceCompany.objects.get(name=insurancecode)
                except Exception as e:
                    print(e)
                    insuranceCompany = None
                kstpr = KSTPR.objects.filter(name=citizenshipcode).first()
                okresB = OKRESB.objects.get(name=okres)
                obec = OBECB.objects.filter(name=city).first()
                adress = Address.objects.filter(region=okresB.id, city=obec.id, street=ulice).first()
                grade = ROCNIK.objects.filter(name=interruption).first()
                prizn_st = PRIZN_ST.objects.filter(name=classId).first()
                code_zmen = KOD_ZMEN.objects.filter(name=codechange).first()
                delst = DELST.objects.get(id=40)
                drst = DRST.objects.get(id=41)
                fst = FST.objects.get(name=language_1)
                zpusob = ZPUSOB.objects.get(name=studyFiledId)
                virtualoperation = VirtualOperation.objects.all().first()
                codes = KOD_VETY.objects.filter(name=codeSentence).first()
                lan_1 = ForeignLanguage.objects.filter(id=language_3).first()
                lan_2 = ForeignLanguage.objects.filter(id=language_4).first()
                previous = ODHL.objects.filter(name=previousSchool).first()
                citizen = STPR.objects.filter(name=citizenshipid).first()
                kod_ukon = KOD_UKON.objects.filter(name=endreason).first()
                if enddate is not None:
                    enddate = enddate.strip('“”')
                    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d %H:%M:%S')

                izoz = str(izoz).rstrip('0').rstrip('.')
                if izoz is not None:
                    if len(izoz) == 8:
                        izoz = "0" + izoz
                    elif len(izoz) == 6:
                        izoz = "000" + izoz
                print(izoz)
                if person_detail_identification_number == identificationnumber and student_id_number == identificationnumber:

                    if endreason is None:
                        continue
                    else:
                        code_end = KOD_UKON.objects.filter(name=endreason).first()

                    print(code_end)
                    personDetail = PersonDetail(personId=person_detail_identification_number.id, nactiveReasonId=0, firstName=name, lastName=surname,
                                                birthName=surname, birthOn=birtDate, sex=sex_id,
                                                identificationCode=identificationnumber, familyStatus=1, citizenship=citizen,
                                                citizenshipCode=kstpr, insuranceCompany=insuranceCompany, birthAddressId=adress,
                                                permanentAddressId=adress, temporaryAddressId=adress, contactAddressId=adress, validSince=validSince,
                                                previousSchool=previous, education=education, previousSchoolCode=izoz)
                    personDetail.save()
                    studentDetail = StudentDetail(studentId=student_id_number.id, endDate=enddate, endReason=code_end.id if code_end is not None else "",
                                                  lassId=class_id.id, startDate=validSince,
                                                  startReason=code_of_start.id,
                                                  obligatorySchoolAttendenceYears="A",
                                                  studyFieldId=studyfiled.id, yearsOfStudy="9", grade=grade.id,
                                                  formAttendence=prizn_st.id, interruption=kindOfEducation,
                                                  codeChange=code_zmen.id, lenghtOfEducationProgram=delst.id,
                                                  kindOfEducation=drst.id, formOfEducation=fst.id,
                                                  methodOfSchoolAttendance=zpusob.id, financing=1,
                                                  virtualOperationId=virtualoperation.id,
                                                  organizationID=organization,
                                                  validSince=validSince_v2, validTo=validTo, codeSentence=codes.id,
                                                  language_1=lan_1.id, language_2=lan_2.id, language_3="", language_4="", zmen_dat=dateofchange,

                                                  )
                    studentDetail.save()
                else:
                    person = Person(organizationId=organization, personTypeId=1)
                    person.save()
                    print(person)
                    personDetail = PersonDetail(personId=person, inactiveReasonId=0, firstName=name, lastName=surname,
                                                birthName=surname, birthOn=birtDate, sex=sex_id,
                                                identificationCode=identificationnumber, familyStatus=1, citizenship=citizen,
                                                citizenshipCode=kstpr, insuranceCompany=insuranceCompany, birthAddressId=adress,
                                                permanentAddressId=adress, temporaryAddressId=adress, contactAddressId=adress, validSince=validSince,
                                                previousSchool=previous, education=education, previousSchoolCode=izoz
                                                )
                    personDetail.save()
                    student = Student(personId=person, organizationId=organization)
                    student.save()
                    studentDetail = StudentDetail(StudentId=student, classId=class_id, startDate=validSince, startReason=code_of_start, obligatorySchoolAttendenceYears="A",
                                                  endDate=enddate, endReason=kod_ukon,
                                                  studyFieldId=studyfiled, yearsOfStudy="9", grade=grade, formAttendence=prizn_st, interruption=kindOfEducation,
                                                  codeChange=code_zmen, lenghtOfEducationProgram=delst, kindOfEducation=drst, formOfEducation=fst,
                                                  methodOfSchoolAttendance=zpusob, financing=1, virtualOperationId=virtualoperation, organizationID=organization,
                                                  validSince=validSince_v2, validTo=validTo, codeSentence=codes, language_1=lan_1, language_2=lan_2, zmen_dat=dateofchange
                                                  )
                    studentDetail.save()

        except Exception as e:
            print(f"Error importing data from {file_path}: {str(e)}")
