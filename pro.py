import csv
import pandas as pd
import statistics as st

df = pd.read_csv('data.csv')

data = df['values'].tolist()

stdev = st.stdev(data)
print('standard deviation = ',stdev)