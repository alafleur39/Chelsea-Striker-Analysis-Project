import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Player': ['Goncalo Ramos', 'Jonathan David', 'Myron Boadu', 'Emanuel Emegha', 
               'Chris Wood', 'Mika Biereth', 'Mateo Retegui'],
    'Club': ['PSG', 'Lille', 'Monaco', 'Stuttgart', 
             'Nottingham Forest', 'Sturm Graz', 'Genoa'],
    'Goals': [7, 16, 7, 13, 7, 12, 19],  
    'Shots': [42, 56, 20, 55, 51, 37, 80],
    'Goal_Conversion': [0.1667, 0.2857, 0.35, 0.2364, 0.3725, 0.3243, 0.2875],
    'xG': [10.6, 15.4, 5.6, 15.2, 11.1, 10, 16],
    'xG_per_Shot': [0.2472, 0.275, 0.28, 0.2764, 0.2176, 0.2703, 0.20],
    'Shot_Distance': [10, 15.4, 11.9, 12.4, 14.5, 11.9, 12.6],
    'Age': [22, 24, 23, 21, 32, 21, 24]  
}


df = pd.DataFrame(data)


plt.figure(figsize=(10,6))
plt.barh(df['Player'], df['xG_per_Shot'], color='skyblue')
plt.xlabel('xG per Shot')
plt.title('xG per Shot - Striker Shortlist')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('xg_per_shot_shortlist.png')  # <-- save as PNG
plt.close()


plt.figure(figsize=(10,6))
plt.barh(df['Player'], df['Goal_Conversion'], color='lightgreen')
plt.xlabel('Goal Conversion Rate')
plt.title('Goal Conversion Rate - Striker Shortlist')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('goal_conversion_shortlist.png')
plt.close()


plt.figure(figsize=(10,6))
plt.barh(df['Player'], df['Shot_Distance'], color='salmon')
plt.xlabel('Average Shot Distance (yards/meters)')
plt.title('Shot Distance - Striker Shortlist')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('shot_distance_shortlist.png')
plt.close()
