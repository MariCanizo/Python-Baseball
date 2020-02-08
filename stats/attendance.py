# How has All-star game attendance changed over time?
import pandas as pd
import matplotlib.pyplot as plt

import data

attendance = data.games.loc[(data.games['type'] == 'info') & (data.games['multi2'] == 'attendance'), ['year', 'multi3']]

# Change colmuns names
attendance.columns = ['year', 'attendance']

# Convert to Numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')
plt.show()