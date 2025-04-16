import pandas as pd

df2015 = pd.read_csv("2014-15.csv", encoding='utf-8-sig')
df2015['season-end-year'] = 2015
df2016 = pd.read_csv("2015-16.csv", encoding='utf-8-sig')
df2016['season-end-year'] = 2016
df2017 = pd.read_csv("2016-17.csv", encoding='utf-8-sig')
df2017['season-end-year'] = 2017
df2018 = pd.read_csv("2017-18.csv", encoding='utf-8-sig')
df2018['season-end-year'] = 2018
df2019 = pd.read_csv("2018-19.csv", encoding='utf-8-sig')
df2019['season-end-year'] = 2019
df2020 = pd.read_csv("2019-20.csv", encoding='utf-8-sig')
df2020['season-end-year'] = 2020
df2021 = pd.read_csv("2020-21.csv", encoding='utf-8-sig')
df2021['season-end-year'] = 2021
df2022 = pd.read_csv("2021-22.csv", encoding='utf-8-sig')
df2022['season-end-year'] = 2022
df2023 = pd.read_csv("2022-23.csv", encoding='utf-8-sig')
df2023['season-end-year'] = 2023
df2024 = pd.read_csv("2023-24.csv", encoding='utf-8-sig')
df2024['season-end-year'] = 2024

df2015.columns = df2015.columns.str.strip().str.lower()
df2016.columns = df2016.columns.str.strip().str.lower()
df2017.columns = df2017.columns.str.strip().str.lower()
df2018.columns = df2018.columns.str.strip().str.lower()
df2019.columns = df2019.columns.str.strip().str.lower()
df2020.columns = df2020.columns.str.strip().str.lower()
df2021.columns = df2021.columns.str.strip().str.lower()
df2022.columns = df2022.columns.str.strip().str.lower()
df2023.columns = df2023.columns.str.strip().str.lower()
df2024.columns = df2024.columns.str.strip().str.lower()

print("2015 columns:", df2015.columns.tolist())
print("2016 columns:", df2016.columns.tolist())
print("2017 columns:", df2017.columns.tolist())
print("2018 columns:", df2018.columns.tolist())
print("2019 columns:", df2019.columns.tolist())
print("2020 columns:", df2020.columns.tolist())
print("2021 columns:", df2021.columns.tolist())
print("2022 columns:", df2022.columns.tolist())
print("2023 columns:", df2023.columns.tolist())
print("2024 columns:", df2024.columns.tolist())

df_all = pd.concat([df2015,df2016, df2017, df2018, df2019, df2020, df2021, df2022, df2023, df2024], ignore_index=True)
print("Combined rows:", df_all.shape[0])
df_all.to_csv("Combined_data_2015-2024.csv", index=False)
