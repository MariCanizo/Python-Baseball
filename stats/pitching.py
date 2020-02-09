import pandas as pd
import matplotlib.pyplot as plt

from data import games

# DataFrame that includes only plays
plays = games[games['type'] == 'play']

# Rows of the plays DataFrame that contain the letter K in the event column
strike_outs = plays[plays['event'].str.contains('K')]

# Group the strike_outs DataFrame by year and then game_id
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

# Convert the groupby object to a DataFrame and name it the column that was created
strike_outs = strike_outs.reset_index(name='strike_outs')

# Convert to Numeric 
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

# plot
strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()