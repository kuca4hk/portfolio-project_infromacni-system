import json
import datetime

# Načte JSON soubor
vstupni_soubor = 'input/input.json'  # Nahraďte cestu k vašemu vstupnímu JSON souboru
vystupni_soubor = f"output/{datetime.datetime.now().strftime('%d.%m.%Y-export.json')}"

with open(vstupni_soubor, 'r', encoding='utf-8') as soubor:
    data = json.load(soubor)

# Odstraní klíč "full" z každého objektu v poli
for polozka in data:
    if "full" in polozka:
        polozka.update(polozka["full"])
        del polozka["full"]

# Uloží upravená data do nového souboru s aktuálním datem jako název souboru
with open(vystupni_soubor, 'w', encoding='utf-8') as soubor:
    json.dump(data, soubor, indent=2, ensure_ascii=False)

print(f'Klíč "full" byl odstraněn a data byla uložena do souboru {vystupni_soubor}')
