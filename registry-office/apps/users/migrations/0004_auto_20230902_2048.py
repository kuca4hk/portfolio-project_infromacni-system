# Generated by Django 3.2.19 on 2023-09-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_persondetail_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondetail',
            name='dataBox',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='citizenship',
            field=models.IntegerField(choices=[(4, 'Afghánská islámská republika'), (8, 'Albánská republika'), (10, 'Antarktida'), (12, 'Alžírská demokratická a lidová republika'), (16, 'Území Americká Samoa'), (20, 'Andorrské knížectví'), (24, 'Angolská republika'), (28, 'Antigua a Barbuda'), (31, 'Ázerbájdžánská republika'), (32, 'Argentinská republika'), (36, 'Australské společenství'), (40, 'Rakouská republika'), (44, 'Bahamské společenství'), (48, 'Království Bahrajn'), (50, 'Bangladéšská lidová republika'), (51, 'Arménská republika'), (52, 'Barbados'), (56, 'Belgické království'), (60, 'Bermudy'), (64, 'Bhútánské království'), (68, 'Mnohonárodní stát Bolívie'), (70, 'Bosna a Hercegovina'), (72, 'Botswanská republika'), (74, 'Bouvetův ostrov'), (76, 'Brazilská federativní republika'), (84, 'Belize'), (86, 'Britské území v Indickém oceánu'), (90, 'Šalomounovy ostrovy'), (92, 'Britské Panenské ostrovy'), (95, 'Kosovská republika'), (96, 'Stát Brunej Darussalam'), (100, 'Bulharská republika'), (104, 'Republika Myanmarský svaz'), (108, 'Burundská republika'), (112, 'Běloruská republika'), (116, 'Kambodžské království'), (120, 'Kamerunská republika'), (124, 'Kanada'), (132, 'Kapverdská republika'), (136, 'Kajmanské ostrovy'), (140, 'Středoafrická republika'), (144, 'Šrílanská demokratická socialistická republika'), (148, 'Čadská republika'), (152, 'Chilská republika'), (156, 'Čínská lidová republika'), (158, 'Čínská republika (Tchaj-wan)'), (162, 'Území Vánoční ostrov'), (166, 'Území Kokosové (Keelingovy) ostrovy'), (170, 'Kolumbijská republika'), (174, 'Komorský svaz'), (175, 'Departement Mayotte'), (178, 'Konžská republika'), (180, 'Konžská demokratická republika'), (184, 'Cookovy ostrovy'), (188, 'Kostarická republika'), (191, 'Chorvatská republika'), (192, 'Kubánská republika'), (196, 'Kyperská republika'), (203, 'Česká republika'), (204, 'Beninská republika'), (208, 'Dánské království'), (212, 'Dominické společenství'), (214, 'Dominikánská republika'), (218, 'Ekvádorská republika'), (222, 'Salvadorská republika'), (226, 'Republika Rovníková Guinea'), (231, 'Etiopská federativní demokratická republika'), (232, 'Stát Eritrea'), (233, 'Estonská republika'), (234, 'Faerské ostrovy'), (238, 'Falklandy (Malvíny)'), (239, 'Jižní Georgie a Jižní Sandwichovy ostrovy'), (242, 'Fidžijská republika'), (246, 'Finská republika'), (248, 'Provincie Alandy'), (250, 'Francouzská republika'), (254, 'Francouzská Guyana'), (258, 'Francouzská Polynésie'), (260, 'Francouzská jižní a antarktická území'), (262, 'Džibutská republika'), (266, 'Gabonská republika'), (268, 'Gruzie'), (270, 'Gambijská republika'), (275, 'Palestinská autonomní území'), (276, 'Spolková republika Německo'), (288, 'Ghanská republika'), (292, 'Gibraltar'), (296, 'Republika Kiribati'), (300, 'Řecká republika'), (304, 'Grónsko'), (308, 'Grenada'), (312, 'Region Guadeloupe'), (316, 'Teritorium Guam'), (320, 'Guatemalská republika'), (324, 'Guinejská republika'), (328, 'Guyanská kooperativní republika'), (332, 'Republika Haiti'), (334, 'Heardův ostrov a MacDonaldovy ostrovy'), (336, 'Vatikánský městský stát'), (340, 'Honduraská republika'), (344, 'Zvláštní administrativní oblast Čínské lidové republiky Hongkong'), (348, 'Maďarsko'), (352, 'Islandská republika'), (356, 'Indická republika'), (360, 'Indonéská republika'), (364, 'Íránská islámská republika'), (368, 'Irácká republika'), (372, 'Irsko'), (376, 'Stát Izrael'), (380, 'Italská republika'), (384, 'Republika Pobřeží slonoviny'), (388, 'Jamajka'), (392, 'Japonsko'), (398, 'Republika Kazachstán'), (400, 'Jordánské hášimovské království'), (404, 'Keňská republika'), (408, 'Korejská lidově demokratická republika'), (410, 'Korejská republika'), (414, 'Kuvajtský stát'), (417, 'Kyrgyzská republika'), (418, 'Laoská lidově demokratická republika'), (422, 'Libanonská republika'), (426, 'Lesothské království'), (428, 'Lotyšská republika'), (430, 'Liberijská republika'), (434, 'Libyjský stát'), (438, 'Lichtenštejnské knížectví'), (440, 'Litevská republika'), (442, 'Lucemburské velkovévodství'), (446, 'Zvláštní administrativní oblast Čínské lidové republiky Macao'), (450, 'Madagaskarská republika'), (454, 'Malawiská republika'), (458, 'Malajsie'), (462, 'Maledivská republika'), (466, 'Republika Mali'), (470, 'Maltská republika'), (474, 'Martinik'), (478, 'Mauritánská islámská republika'), (480, 'Mauricijská republika'), (484, 'Spojené státy mexické'), (492, 'Monacké knížectví'), (496, 'Mongolsko'), (498, 'Moldavská republika'), (499, 'Černá Hora'), (500, 'Montserrat'), (504, 'Marocké království'), (508, 'Mosambická republika'), (512, 'Sultanát Omán'), (516, 'Namibijská republika'), (520, 'Republika Nauru'), (524, 'Nepálská federativní demokratická republika'), (528, 'Nizozemsko'), (531, 'Země Curaçao'), (533, 'Aruba'), (534, 'Svatý Martin (NL)'), (535, 'Bonaire, Svatý Eustach a Saba'), (540, 'Nová Kaledonie'), (548, 'Republika Vanuatu'), (554, 'Nový Zéland'), (558, 'Nikaragujská republika'), (562, 'Nigerská republika'), (566, 'Nigerijská federativní republika'), (570, 'Niue'), (574, 'Území Norfolk'), (578, 'Norské království'), (580, 'Společenství Severní Mariany'), (581, 'Menší odlehlé ostrovy USA'), (583, 'Federativní státy Mikronésie'), (584, 'Republika Marshallovy ostrovy'), (585, 'Republika Palau'), (586, 'Pákistánská islámská republika'), (591, 'Panamská republika'), (598, 'Nezávislý stát Papua Nová Guinea'), (600, 'Paraguayská republika'), (604, 'Peruánská republika'), (608, 'Filipínská republika'), (612, 'Pitcairnovy ostrovy'), (616, 'Polská republika'), (620, 'Portugalská republika'), (624, 'Republika Guinea-Bissau'), (626, 'Demokratická republika Východní Timor'), (630, 'Portorické společenství'), (634, 'Stát Katar'), (638, 'Region Réunion'), (642, 'Rumunsko'), (643, 'Ruská federace'), (646, 'Rwandská republika'), (652, 'Společenství Svatý Bartoloměj'), (654, 'Svatá Helena, Ascension a Tristan da Cunha'), (659, 'Federace Svatý Kryštof a Nevis'), (660, 'Anguilla'), (662, 'Svatá Lucie'), (663, 'Společenství Svatý Martin'), (666, 'Územní společenství Saint Pierre a Miquelon'), (670, 'Svatý Vincenc a Grenadiny'), (674, 'Republika San Marino'), (678, 'Demokratická republika Svatý Tomáš a Princův ostrov'), (682, 'Království Saúdská Arábie'), (686, 'Senegalská republika'), (688, 'Srbská republika'), (690, 'Seychelská republika'), (694, 'Republika Sierra Leone'), (702, 'Singapurská republika'), (703, 'Slovenská republika'), (704, 'Vietnamská socialistická republika'), (705, 'Slovinská republika'), (706, 'Somálská federativní republika'), (710, 'Jihoafrická republika'), (716, 'Zimbabwská republika'), (724, 'Španělské království'), (728, 'Jihosúdánská republika'), (729, 'Súdánská republika'), (732, 'Saharská arabská demokratická republika'), (740, 'Surinamská republika'), (744, 'Špicberky a Jan Mayen'), (748, 'Svazijské království'), (752, 'Švédské království'), (756, 'Švýcarská konfederace'), (760, 'Syrská arabská republika'), (762, 'Republika Tádžikistán'), (764, 'Thajské království'), (768, 'Tožská republika'), (772, 'Tokelau'), (776, 'Království Tonga'), (780, 'Republika Trinidad a Tobago'), (784, 'Stát Spojené arabské emiráty'), (788, 'Tuniská republika'), (792, 'Turecká republika'), (795, 'Turkmenistán'), (796, 'Ostrovy Turks a Caicos'), (798, 'Tuvalu'), (800, 'Ugandská republika'), (804, 'Ukrajina'), (807, 'Republika Severní Makedonie'), (818, 'Egyptská arabská republika'), (826, 'Spojené království Velké Británie a Severního Irska'), (831, 'Bailiwick Guernsey'), (832, 'Bailiwick Jersey'), (833, 'Ostrov Man'), (834, 'Tanzanská sjednocená republika'), (840, 'Spojené státy americké'), (850, 'Americké Panenské ostrovy'), (854, 'Burkina Faso'), (858, 'Uruguayská východní republika'), (860, 'Republika Uzbekistán'), (862, 'Bolívarovská republika Venezuela'), (876, 'Teritorium Wallisovy ostrovy a Futuna'), (882, 'Nezávislý stát Samoa'), (887, 'Jemenská republika'), (894, 'Zambijská republika'), (999, 'Ostatní')]),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='citizenshipCode',
            field=models.IntegerField(choices=[(3, 'Czech Republic'), (5, 'Permanent resident in the Czech Republic'), (6, 'Temporary resident in the Czech Republic'), (7, 'Asylum seeker or applicant for subsidiary protection'), (9, 'Citizenship unknown, unspecified')]),
        ),
    ]