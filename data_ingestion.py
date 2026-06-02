import pandas as pd
import os

folder = "Data/Raw"

for file in os.listdir(folder):

    if file.endswith(".csv") or file.endswith(".xlsx"):

        print("=" * 60)
        print("FILE:", file)

        path = os.path.join(folder, file)

        if file.endswith(".csv"):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
        