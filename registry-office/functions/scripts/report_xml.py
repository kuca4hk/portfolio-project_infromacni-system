import xml.etree.ElementTree as ET
from datetime import datetime
from pprint import pprint
from typing import List, Dict
import json


def create_xml(json_file_path: str, output_file_path: str = "final/s181105527_01.xml", author: str = "Jakub Kučera", phone_number: str = "773 275 800",
               author_email: str = "jakub.kucera@itgymnazium.cz") -> None:

    # Načtěte data z JSON souboru
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    now: datetime = datetime.now()
    now_array: List = [now.year, now.month, now.day, now.hour, now.minute, now.second]

    for i in range(len(now_array)):
        now_array[i] = "{:02}".format(now_array[i])

    root: ET.Element = ET.Element('Vykaz', verze="SS.007")

    ET.SubElement(root, "Vygen").text = "1. IT Gymnázium vlastní systém"
    ET.SubElement(root, "autor").text = author
    ET.SubElement(root, "telefon").text = phone_number
    ET.SubElement(root, "e-mail").text = author_email
    ET.SubElement(root, "soubor").text = "s181105527_01"
    # ET.SubElement(root, "vytvoreno").text = "30.09.2023"
    ET.SubElement(root, "vytvoreno").text = "{}.{}.{} {}:{}:{}".format(now_array[2], now_array[1], now_array[0],
                                                                       now_array[3], now_array[4], now_array[5])

    for row in json_data:
        veta = ET.SubElement(root, "veta")
        for key, value in row.items():
            if not key:
                continue
            ET.SubElement(veta, key).text = str(value)

    xml_str = ET.tostring(root, encoding='utf8').decode('utf8')

    # Uložte XML do výstupního souboru
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(xml_str)


create_xml(json_file_path="output/11.10.2023-export.json")
