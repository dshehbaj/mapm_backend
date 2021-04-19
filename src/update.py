"""
Python script for downloading and cleaning covid and life expectancy data.
"""

import pandas as pd
from datetime import date, timedelta

def update_expectancy():
    fips_url = "https://raw.githubusercontent.com/kjhealy/fips-codes/" + \
      "master/state_and_county_fips_master.csv"
    fips_df = pd.read_csv(fips_url)
    fips_df["fips"] = \
      fips_df["fips"].astype(str).apply(lambda x: (5 - len(x)) * "0" + x)
    fips_df["state"] = fips_df["state"].fillna(-1)
    fips_df = fips_df[fips_df["state"] != -1]
    states = list(fips_df["state"].unique())
    url = "https://ftp.cdc.gov/pub/" + \
      "Health_Statistics/NCHS/Datasets/NVSS/USALEEP/CSV/AK_A.CSV"
    df_dict = {}
    for state in states:
      url = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/" + \
      f"NVSS/USALEEP/CSV/{state}_A.CSV"
      df_dict[state] = pd.read_csv(url)
    for state in df_dict.keys():
      df_dict[state] = df_dict[state][["STATE2KX", "CNTY2KX", "e(0)"]]
      df_dict[state]["STATE2KX"] = \
        df_dict[state]["STATE2KX"].astype(str).apply(lambda x: (2 - len(x)) * "0" + x)
      df_dict[state]["CNTY2KX"] = \
        df_dict[state]["CNTY2KX"].astype(str).apply(lambda x: (3 - len(x)) * "0" + x)
      df_dict[state]["fips"] = df_dict[state]["STATE2KX"] + df_dict[state]["CNTY2KX"]
    life_df = pd.DataFrame()
    for state in df_dict.keys():
      life_df = pd.concat([life_df, df_dict[state]])
    complete_df = pd.merge(life_df, fips_df, on="fips")
    complete_df = complete_df.set_index(["state", "name"])
    data_by_county = complete_df.groupby(["state", "name"])["e(0)"].mean()
    data_by_state = complete_df.groupby(["state"])["e(0)"].mean()
    data_by_state = data_by_state.to_frame()
    data_by_state = data_by_state.reset_index()
    data_by_state.columns = ["state", "age"]
    data_by_state = data_by_state.set_index("state")

    data_by_state.to_csv("../data/life_expectancy/states_life_expectancy.csv")

    data_by_county = data_by_county.to_frame()
    data_by_county = data_by_county.reset_index()
    data_by_county.columns = ["state", "name", "age"]
    data_by_county["cnty"] = data_by_county["name"] + " " + data_by_county["state"]
    data_by_county["cnty"] = data_by_county["cnty"].apply(lambda x: x.lower().replace(" ", "-"))
    data_by_county = data_by_county.set_index("cnty")

    data_by_county.to_csv("../data/life_expectancy/county_life_expectancy.csv")

def update_covid():
    state_names = \
      ["Alaska", "Alabama", "Arkansas", "Arizona",
        "California", "Colorado", "Connecticut", "District of Columbia",
        "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho",
        "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana",
        "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
        "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
        "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada",
        "New York State", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Virginia",
        "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

    state_codes = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD",
              "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH",
              "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/" + \
        "public/data/vaccinations/us_state_vaccinations.csv"
    vax_df = pd.read_csv(url)
    date_str = str(date.today() - timedelta(days=1))
    vax_df = vax_df[vax_df["date"] == date_str]
    vax_df = vax_df.set_index(["location"])
    vax_df = vax_df.loc[state_names]
    cols = [1, 2, 3, 6, 9, 10]
    vax_df.iloc[:, cols] = vax_df.iloc[:, cols].astype(int)
    vax_df["state"] = state_codes
    vax_df = vax_df.reset_index().set_index(["state"])
    vax_df.to_csv("../data/covid/vaccinations.csv")



if __name__ == "__main__":
    update_expectancy()
    update_covid()

