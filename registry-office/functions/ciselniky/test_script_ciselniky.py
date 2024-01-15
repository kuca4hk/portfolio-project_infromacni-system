# import pandas as pd
#
#
# def racj_import_to_db(path: str="RAPZ.xlsx"):
#
#     df = pd.read_excel(path)
#     # print(df)
#     for index, row in df.iterrows():
#         # print(row)
#
#         id = str(row.values[0]) if str(row.values[0]) != "nan" else None
#         name = row.values[1] if str(row.values[1]) != "nan" else None
#         if id == None and name == None:
#             pass
#         else:
#             print(id, name)
#
#
# racj_import_to_db()


import json
import urllib
import requests
import pandas as pd
import re
import datetime


def extrahovat_text_a_cisla(pred_text):
    # Rozdělit řetězec na části podle čárky
    pattern = r'(.+?) (\d+),'

    # Použijeme regulární výraz k extrakci názvu ulice a čísla
    match = re.search(pattern, pred_text)

    if match:
        # Pokud jsme našli shodu, uložíme název ulice a číslo do proměnných
        nazev_ulice = match.group(1)
        cislo_domu = match.group(2)
        return nazev_ulice, cislo_domu
    else:
        # Pokud nebyla nalezena shoda, vrátíme None
        return None, None


def import_person(file="person.xlsx"):
    unique_addresses = set()
    index = 0

    df = pd.read_excel(file)
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
        codeSentence = row.values[56] if str(row.values[56]) != "nan" else None
        validSince_v2 = row.values[57] if str(row.values[57]) != "nan" else None
        validTo = row.values[58] if str(row.values[58]) != "NaT" else None
        identificationnumber = str("0" + str(identificationnumber))

        if len(izoz) == 8:
            izoz = "0" + izoz

        print(enddate, endreason)
        if enddate is not None:
            print(datetime.datetime.strptime(enddate, '%Y-%m-%d %H:%M:%S'))


import_person()
