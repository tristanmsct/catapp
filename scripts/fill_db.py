#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:03:08 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://guaiguai:mdp@localhost:5432/postgres')

df = pd.DataFrame(
    [
        [1, "Guaiguai", 5.7, "ventru"],
        [2, "Papuche", 4, "sournoise"],
        [3, "Croquetus", 6, "affamé"],
    ],
    columns=["idCat", "nom", "poids", "caracteristique"]
)

df.to_sql("cat", engine, index=False, if_exists='replace')
