from datetime import datetime

import pandas as pd
from django.core.management import BaseCommand
from ...models import OBECB, OKRESB
from ...models import Address
import re


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument("paths", nargs="+", type=str)

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
        file_path = "C:/Users/Jakub Kucera/Desktop/Projects/ITG/registry-office/registry-office/functions/ciselniky/adress.xlsx"
        try:
            unique_addresses = set()

            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                city = str(row.values[0]) if str(row.values[0]) != "nan" else None
                okres = row.values[1] if str(row.values[1]) != "nan" else None
                adress = row.values[2] if str(row.values[2]) != "nan" else None
                veta = adress
                steet, descriptiveNumber = extrahovat_text_a_cisla(adress)

                if okres == "Praha-východ" or okres == "Praha východ":
                    okres = "Praha - východ"

                    # Použití regulárního výrazu k nalezení čísla za čárkou
                matches_zipcode = re.findall(r'(\d+)\s+(\d+)', veta)

                zipcode = None
                if matches_zipcode:
                    for match in matches_zipcode:
                        cislo_za_carkou = match[0]
                        cislo_za_mezou = match[1]
                        zipcode = cislo_za_carkou + " " + cislo_za_mezou
                else:
                    zipcode = 00000
                if adress in unique_addresses:
                    continue

                # Add the address to the set of unique addresses
                unique_addresses.add(adress)
                if city == None and okres == None:
                    pass
                else:
                    if city == "Brandýs nad Labem" or city == "Brandýs nad Labem - Stará Boleslav":
                        city = "Brandýs nad Labem-Stará Boleslav"
                    elif city == "Praha 9-Vinoř":
                        city = "Praha 9"
                    okres = okres
                    print(city)
                    city = OBECB.objects.filter(name=city).first()
                    okres = OKRESB.objects.get(name=okres)
                    print(city)
                    a = Address(street=steet, descriptiveNumber=descriptiveNumber, city=city, zipCode=zipcode, region=okres, state="CZ", validFrom=datetime.now())
                    a.save()
        except Exception as e:
            print(f"Error importing data from {file_path}: {str(e)}")
