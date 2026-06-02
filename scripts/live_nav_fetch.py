import requests
import pandas as pd
import os

scheme_codes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "NIPPON": 118632,
    "AXIS": 119092,
    "KOTAK": 120841
}

save_folder = "Data/Raw"

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = os.path.join(
            save_folder,
            f"{fund_name}_NAV.csv"
        )

        nav_df.to_csv(
            file_path,
            index=False
        )

        print(f"Saved {fund_name}")

    else:
        print(f"Failed for {fund_name}")