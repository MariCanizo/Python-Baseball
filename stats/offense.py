import pandas as pd
import matplotlib.pyplot as plt

from data import games

#"What is the distribution of hits across innings?"

plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# need just the hits, singles, doubles, triples, and home runs
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# Convert the inning column of the hits DataFrame from strings to numbers
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# Create a dictionary called replacements
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}

# replace() function on the hits['event']
hit_type = hits['event'].replace(replacements, regex=True)

# add a new column with assign()
hits = hits.assign(hit_type=hit_type)

# Group By Inning and Hit Type
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# Save memory by making hits['hit_type'] a categorical column with pd.Categorical()
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

hits = hits.sort_values(['inning','hit_type'])

# Reshape the hits DataFrame for plotting
hits = hits.pivot(index='inning', columns='hit_type', values='count')

# Plot it
hits.plot.bar(stacked=True)
plt.show()
