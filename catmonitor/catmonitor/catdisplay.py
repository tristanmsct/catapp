#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from catmonitor.settings import get_settings

settings = get_settings()

engine = create_engine(f"""postgresql://guaiguai:mdp@{settings.PG_HOST}:5432/postgres""")

df = pd.read_sql("cat", engine)

st.title("Hello and welcome to the universal cat monitoring tool")

st.header("BEHOLD THE MAGIFICENT CATS OF THE WORLD")

st.dataframe(df, width=800, hide_index=True)

st.bar_chart(data=df, x="nom", y="poids")
