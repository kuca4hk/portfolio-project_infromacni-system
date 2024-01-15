# Generated by Django 3.2.19 on 2023-09-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholl_class', '0003_auto_20230824_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='language_1',
            field=models.IntegerField(choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default='0'),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='language_2',
            field=models.IntegerField(blank=True, choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default='0', null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='language_3',
            field=models.IntegerField(blank=True, choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default='0', null=True),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='language_4',
            field=models.IntegerField(blank=True, choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default='0', null=True),
        ),
        migrations.AddField(
            model_name='studyfield',
            name='language_o',
            field=models.CharField(choices=[(0, 'Nevyučuje se cizímu jazyku'), (1, 'Albánský jazyk'), (2, 'Anglický jazyk'), (3, 'Arabský jazyk'), (4, 'Bulharský jazyk'), (5, 'Čínský jazyk'), (6, 'Dánský jazyk'), (7, 'Finský jazyk'), (8, 'Francouzský jazyk'), (9, 'Hebrejský jazyk'), (10, 'Holandský jazyk'), (11, 'Italský jazyk'), (12, 'Japonský jazyk'), (13, 'Lužickosrbský jazyk'), (14, 'Maďarský jazyk'), (15, 'Mongolský jazyk'), (16, 'Německý jazyk'), (17, 'Norský jazyk'), (18, 'Polský jazyk'), (19, 'Portugalský jazyk'), (20, 'Rumunský jazyk'), (21, 'Ruský jazyk'), (23, 'Slovinský jazyk'), (24, 'Srbochorvatský jazyk'), (25, 'Španělský jazyk'), (26, 'Švédský jazyk'), (27, 'Turecký jazyk'), (28, 'Vlámský jazyk'), (29, 'Slovenský jazyk'), (30, 'Český jazyk'), (31, 'Bengálský jazyk'), (32, 'Hindský jazyk'), (33, 'Tibetský jazyk'), (34, 'Latinský jazyk'), (35, 'Indonéský jazyk'), (36, 'Perský jazyk'), (37, 'Řecký klasický jazyk'), (38, 'Řecký novodobý jazyk'), (39, 'Jazyk sanskrt'), (41, 'Jazyk ivrit'), (51, 'Běloruský jazyk'), (52, 'Chorvatský jazyk'), (54, 'Srbský jazyk'), (55, 'Ukrajinský jazyk'), (61, 'Vietnamský jazyk'), (62, 'Romský jazyk'), (63, 'Korejský jazyk'), (64, 'Thajský jazyk')], default='0', max_length=1),
        ),
    ]
