# Generated by Django 3.2.19 on 2023-09-03 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciselniky', '0001_initial'),
        ('scholl_class', '0006_studentdetail_methodofschoolattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='codeChange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailKOD_VETY', to='ciselniky.kod_vety'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='codeLanguageOfGraduation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailForeignLanguage', to='ciselniky.foreignlanguage'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='codeRepeat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailExamType', to='ciselniky.examtype'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='endReason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailKOD_UKON', to='ciselniky.kod_ukon'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='formAttendence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailPRIZN_ST', to='ciselniky.prizn_st'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='formOfEducation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ciselniky.fst'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.let_psd'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='interruption',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailPRERUS', to='ciselniky.prerus'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='kindOfEducation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailDRST', to='ciselniky.drst'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='language_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.foreignlanguage'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='language_2',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.foreignlanguage'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='language_3',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.foreignlanguage'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='language_4',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.foreignlanguage'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='lenghtOfEducationProgram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailDELST', to='ciselniky.delst'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='methodOfSchoolAttendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailZPUSOB', to='ciselniky.zpusob'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='resultOfGraduation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailSucces', to='ciselniky.success'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='startReason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailKOD_ZAH', to='ciselniky.kod_zah'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='yearsOfStudy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentDetailLET_PSD', to='ciselniky.let_psd'),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studyFieldST_SKOLY', to='ciselniky.st_skoly'),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='language_o',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studyFieldFieldLanguage_o', to='ciselniky.fieldlanguage'),
        ),
        migrations.AlterField(
            model_name='studyfield',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ciselniky.st_skoly'),
        ),
    ]
