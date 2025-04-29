import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("big5_striker_shooting_statsupdated.csv") # read in csv file


df = df.rename(columns={
    'Player': 'name',
    'Squad': 'club',
    'Gls': 'goals',
    'Sh': 'shots',
    'SoT': 'shots_on_target',
    'Dist': 'shot_distance',
    'xG': 'xG',
    'npxG': 'npxG',
    '90s': 'nineties_played'
})

df['season'] = '2024/25'

df = df[[
    'name', 'club', 'goals', 'shots', 'shots_on_target',
    'shot_distance', 'xG', 'npxG', 'nineties_played', 'season'
]]


engine = create_engine("mysql+pymysql://root:powrandy28@localhost/chelsea_striker_analysis")
df.to_sql('strikers', con=engine, if_exists='append', index=False)

print("✅ Full striker CSV inserted into MySQL.")