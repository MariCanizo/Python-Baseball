import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()

game_frames = []
for game_file in game_files :
    game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# DataFrame that contains all of the data from all of the event files
games = pd.concat(game_frames)

# Clean up some of the data
# dataframe.loc[row condition, [columns]] = new value
games.loc[games['multi5'] == '??', 'multi5'] = ''

# Associate each row of data with the proper game ID
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# Fill all the values for all rows on the identifiers DataFrame.
identifiers = identifiers.fillna(method='ffill')

# Change colmuns names
identifiers.columns = ['game_id', 'year']

games = pd.concat([games, identifiers], axis=1, sort=False)

games = games.fillna(' ')

games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

print(games.head())