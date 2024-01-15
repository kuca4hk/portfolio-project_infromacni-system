import pandas as pd
from django.core.management import BaseCommand
from ...models import STPR


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
        file_path = "C:/Users/Jakub Kucera/Desktop/Projects/ITG/registry-office/registry-office/functions/ciselniky/STPR.xlsx"
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                id = int(row.values[0]) if str(row.values[0]) != "nan" else None
                name = row.values[1] if str(row.values[1]) != "nan" else None
                code_2 = str(row.values[2]) if str(row.values[2]) != "nan" else None
                code_3 = str(row.values[3]) if str(row.values[3]) != "nan" else None

                if id is not None or name is not None:
                    data = STPR(id=id, name=name, code_2=code_2, code_3=code_3)
                    data.save()
            print(f"Data from {file_path} imported successfully.")
        except Exception as e:
            print(f"Error importing data from {file_path}: {str(e)}")
