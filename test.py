import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

traffic = pd.read_csv('C:\\Users\\RepairExample_English.csv')
time = traffic['timestamp']
timedf = pd.DataFrame(time)
timedf
timedf['timestamp'] = timedf['timestamp'].apply(lambda e: e.split(' ')[0])
timedf['timestamp'] = timedf['timestamp'].apply(lambda e: e.split('-')[0])
timedf
df['name'] = df['name'].apply(lambda e: e.split()[0])
