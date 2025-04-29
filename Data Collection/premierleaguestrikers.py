import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://fbref.com/en/comps/Big5/shooting/players/Big-5-European-Leagues-Stats'
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


table = soup.find('table', {'id': 'stats_shooting'})

if table:
    df = pd.read_html(str(table))[0]

    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(0)

    print(df.columns)

    numeric_cols = ['Gls', 'Sh', 'SoT', 'Dist', 'xG', 'npxG', '90s']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

   
    if 'Pos' in df.columns:
        df = df[df['Pos'].str.contains('FW', na=False)]

    
    df = df[['Player', 'Squad', 'Gls', 'Sh', 'SoT', 'Dist', 'xG', 'npxG', '90s']]

   
    df.to_csv('big5_striker_shooting_statsupdated.csv', index=False)
    print("✅ Saved to big5_striker_shooting_statsupdated.csv")

else:
    print("❌ Could not find shooting stats table.")
