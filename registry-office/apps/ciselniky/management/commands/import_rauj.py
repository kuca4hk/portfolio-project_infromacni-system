import pandas as pd
from django.core.management import BaseCommand
from ...models import OBECB


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument("paths", nargs="+", type=str)

    def handle(self, *args, **kwargs):
        # if "paths" not in kwargs:
        #     print("paths are missing")
        #     return
        #
        # for file_path in kwargs["paths"]:
        file_path = "C:/Users/Jakub Kucera/Desktop/Projects/ITG/registry-office/registry-office/functions/ciselniky/RAUJ.xlsx"
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                id = int(row.values[0]) if not pd.isna(row.values[0]) else None
                name = row.values[1] if not pd.isna(row.values[1]) else None

                if id is not None or name is not None:
                    data = OBECB(id=id, name=name)
                    data.save()
            print(f"Data from {file_path} imported successfully.")
        except Exception as e:
            print(f"Error importing data from {file_path}: {str(e)}")
