# Generated by Django 3.2.19 on 2023-09-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholl_class', '0004_auto_20230902_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='codeChange',
            field=models.IntegerField(blank=True, choices=[(1, 'Žák/student'), (2, 'Přerušené vzdělávání'), (3, 'Ukončené vzdělávání bez absolvování'), (4, 'Absolvent'), (5, 'Dodatečný odklad povinné školní docházky'), (6, 'Neúspěšné konání zkoušky "cizí osobou"'), (7, 'Úspěšné konání zkoušky "cizí osobou"'), (9, 'Osoba, která nenastoupila ke vzdělávání')], null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='codeLanguageOfGraduation',
            field=models.IntegerField(blank=True, choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='codeOfTest',
            field=models.CharField(default='', editable=False, max_length=1),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='codeRepeat',
            field=models.IntegerField(blank=True, choices=[(1, 'Zkouška v řádném termínu'), (2, 'Náhradní zkouška'), (3, 'Opravná zkouška (po řádné nebo náhradní zkoušce)'), (4, 'Opakovaná zkouška'), (5, 'Opravná zkouška (po opakované zkoušce)')], null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='dateOfGraduation',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='grade',
            field=models.IntegerField(choices=[(1, 'První ročník'), (2, 'Druhý ročník'), (3, 'Třetí ročník'), (4, 'Čtvrtý ročník'), (5, 'Pátý ročník'), (6, 'Šestý ročník'), (7, 'Sedmý ročník'), (8, 'Osmý ročník'), (9, 'Devátý ročník'), ('A', 'Desátý ročník')], default=1),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='interruption',
            field=models.IntegerField(blank=True, choices=[(0, 'Beze změny'), (1, 'Změna vzdělávání (oboru, druhu, formy, délky)'), (2, 'Změna organizace vzdělávání (přestup, přeřazení, vyřazení)'), (5, 'Konání zkoušky (závěrečné, maturitní, absolutoria)'), (6, 'Změna osobních údajů'), (7, 'Změna osobního identifikátoru (RČ)'), (8, 'Poskytnutí podpůrných opatření')], null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='kindOfEducation',
            field=models.IntegerField(choices=[(10, 'Střední'), (21, 'Střední s výučním listem'), (22, 'Zkrácené studium pro získání středního vzdělání s výučním listem'), (31, 'Vyšší odborné v konzervatoři - 6leté'), (32, 'Vyšší odborné v konzervatoři - 8leté'), (34, 'Vyšší odborné ve VOŠ'), (41, 'Střední s maturitní zkouškou'), (42, 'Zkrácené studium pro získání středního vzdělání s maturitní zkouškou'), (43, 'Nástavbové studium'), (61, 'Střední s maturitní zkouškou i výučním listem'), (91, 'Rekvalifikační studium v oboru KKOV, hrazené úřadem práce'), (92, 'Rekvalifikační studium v oboru KKOV, hrazené z jiných zdrojů')], default=41),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='lenghtOfEducationProgram',
            field=models.CharField(blank=True, choices=[('10', 'Jeden rok'), ('15', 'Jeden a půl roku'), ('20', 'Dva roky'), ('25', 'Dva a půl roku'), ('30', 'Tři roky'), ('35', 'Tři a půl roku'), ('40', 'Čtyři roky'), ('45', 'Čtyři a půl roku'), ('50', 'Pět let'), ('60', 'Šest let'), ('80', 'Osm let'), ('90', 'Devět let'), ('A0', 'Deset let')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='numberofCertificate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='numberofTeachingSheet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='resultOfGraduation',
            field=models.IntegerField(blank=True, choices=[(1, 'Prospěl'), (2, 'Prospěl s vyznamenáním'), (3, 'Neprospěl z jednoho předmětu'), (4, 'Neprospěl z více předmětů'), (5, 'Neprospěl - neomluvená neúčast')], null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='seriesOfCertificate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='seriesOfTeachingSheet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='yearsOfStudy',
            field=models.IntegerField(blank=True, choices=[(1, 'První ročník'), (2, 'Druhý ročník'), (3, 'Třetí ročník'), (4, 'Čtvrtý ročník'), (5, 'Pátý ročník'), (6, 'Šestý ročník'), (7, 'Sedmý ročník'), (8, 'Osmý ročník'), (9, 'Devátý ročník'), ('A', 'Desátý ročník')], null=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='financing',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='formOfEducation',
            field=models.IntegerField(choices=[(10, 'Denní'), (22, 'Dálková'), (23, 'Večerní'), (24, 'Distanční'), (30, 'Kombinovaná')], default=10),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='language_o',
            field=models.IntegerField(choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default=0),
        ),
    ]
