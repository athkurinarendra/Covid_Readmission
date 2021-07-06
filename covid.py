# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:18:46 2021

@author: admin
"""

import pandas as pd
df = pd.read_csv("covid-19.csv")
df.head()

def clean_name(name):
    return name.lower().strip().replace(" ", "_").replace(",", "_").replace("-", "_")


df.rename(columns=clean_name, inplace=True)

df.head()