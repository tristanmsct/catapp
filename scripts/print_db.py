#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:03:08 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://guaiguai:mdp@localhost:5432/postgres')

df = pd.read_sql("cat", engine)

print(df)
