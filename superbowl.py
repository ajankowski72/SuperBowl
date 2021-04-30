# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:15:47 2021

@author: Adam Jankowski
"""

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.pro-football-reference.com/super-bowl/'
dfs = pd.read_html(url)

df = dfs[0]
                                                                                                         
df2 = df[['SB', 'Winner', 'Pts', 'Loser', 'Pts.1', 'MVP', 'Stadium','City','State']]
df3 = df2.rename(columns = {'Pts' : "Winning Team's Points", 'Pts.1' : "Losing Team's Points"})
df3["MVP's Position"] = ['Quarterback', 'Quarterback', 'Wide Receiver', 'Quarterback', 'Quarterback', 'Linebacker', 'Quarterback', 'Linebacker', 'Quarterback', 'Quarterback', 'Quarterback', 'Quarterback', 'Wide Receiver', 'Quarterback', 'Quarterback', 'Wide Receiver', 'Wide Receiver', 'Quarterback', 'Safety', 'Quarterback', 'Linebacker', 'Quarterback', 'Quarterback', 'Running Back', 'Wide Receiver', 'Cornerback', 'Quarterback', 'Running Back', 'Quarterback', 'Quarterback', 'Running Back', 'Quarterback', 'Wide Receiver', 'Quarterback', 'Quarterback', 'Defensive End', 'Quarterback', 'Running Back', 'Running Back', 'Quarterback', 'Quarterback', 'Quarterback', 'Quarterback', 'Defensive End', 'Wide Receiver', 'Wide Receiver', 'Running Back', 'Running Back', 'Safety', 'Quarterback', 'Linebacker', 'Quarterback', 'Quarterback', 'Quarterback', 'Quarterback' ]
df3['Margin of Victory'] = df3["Winning Team's Points"] - df3["Losing Team's Points"]
df3.to_csv('finalsuperbowl.csv')




