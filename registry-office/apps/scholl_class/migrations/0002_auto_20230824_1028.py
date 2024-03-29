# Generated by Django 3.2.19 on 2023-08-24 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_alter_organization_osszdistrictid'),
        ('users', '0002_auto_20230824_1028'),
        ('scholl_class', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='operationId',
        ),
        migrations.AddField(
            model_name='student',
            name='organizationId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='studentOrganization', to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='student',
            name='personId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentPerson', to='users.person'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='endReason',
            field=models.IntegerField(blank=True, choices=[(1, 'Úspěšné absolvování'), (2, 'Ukončení vzdělávacího programu bez předepsané zkoušky'), (3, 'Přestup na jinou školu'), (4, 'Nepostoupení do vyššího ročníku, nesplnění podmínek pro konání zkoušky'), (5, 'Zanechání vzdělávání'), (6, 'Vyloučení'), (8, 'Úmrtí'), ('G', 'Ukončení pro cizince (odstěhování)'), ('H', 'Převední do jiné školy (sloučení škol, splynutí, změna IZO)')], null=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='formAttendence',
            field=models.IntegerField(choices=[(1, 'Řádné vzdělávání'), (2, 'Řádné vzdělávání po přerušení vzdělávání'), (3, 'Opakování ročníku'), (4, 'Přeřazení do vyššího ročníku (z důvodu mimořádného nadání)'), (5, 'Zařazení do nižšího ročníku (bez opakování)'), (6, 'Přerušení vzdělávání'), (7, 'Vzdělávání ukončeno')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='formOfEducation',
            field=models.IntegerField(choices=[(10, 'Denní'), (22, 'Dálková'), (23, 'Večerní'), (24, 'Distanční'), (30, 'Kombinovaná')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='obligatorySchoolAttendenceYears',
            field=models.IntegerField(choices=[('A', 'Přijetí do 1.ročníku'), ('B', 'Přijetí do 3.ročníku 6letého gymnázia'), ('C', 'Přijetí do 5.ročníku 8letého gymnázia'), ('D', 'Přijetí do vyššího ročníku (podle § 63 resp. § 95 ŠZ)'), ('E', 'Přestup z jiné školy (podle § 66 odst.4 resp.§ 95 odst.5 ŠZ)'), ('F', 'Přestup z nižšího stupně víceletého gymnázia do 4letého oboru gymnázia'), ('H', 'Převedení z jiné školy (zánik, sloučení škol)')]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='startReason',
            field=models.IntegerField(choices=[('A', 'Přijetí do 1.ročníku'), ('B', 'Přijetí do 3.ročníku 6letého gymnázia'), ('C', 'Přijetí do 5.ročníku 8letého gymnázia'), ('D', 'Přijetí do vyššího ročníku (podle § 63 resp. § 95 ŠZ)'), ('E', 'Přestup z jiné školy (podle § 66 odst.4 resp.§ 95 odst.5 ŠZ)'), ('F', 'Přestup z nižšího stupně víceletého gymnázia do 4letého oboru gymnázia'), ('H', 'Převedení z jiné školy (zánik, sloučení škol)')]),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='code',
            field=models.CharField(choices=[('7941K41', 'Gymnázium')], max_length=255),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='name',
            field=models.CharField(choices=[('7941K41', 'Gymnázium')], max_length=255),
        ),
    ]
