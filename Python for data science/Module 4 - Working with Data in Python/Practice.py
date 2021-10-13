import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


nba_teams = teams.get_teams()
dict_nba_team = one_dict(nba_teams)

df_teams = pd.DataFrame(dict_nba_team)

df_warriors = df_teams[df_teams['nickname']=='Warriors']
id_warriors = df_warriors[['id']].values[0][0]


game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
warriors_games = game_finder.get_data_frames()[0]

games_home =warriors_games[warriors_games['MATCHUP'] == 'GSW vs. TOR']
games_away = warriors_games[warriors_games['MATCHUP'] == 'GSW @ TOR']

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE', y='PLUS_MINUS',ax = ax)
games_home.plot(x = "GAME_DATE",y="PLUS_MINUS", ax= ax)
ax.legend(["Away","Home"])
plt.show()









# nba_teams = teams.get_teams()
# print(nba_teams)

# df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
# df.to_csv("data.csv")
# print(df.head())

#df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
#print(df['a'] == 1)
