#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

import pandas as pd
from fastapi import FastAPI
from sqlalchemy import create_engine

from catapi.data_models import Masse_Input

engine = create_engine('postgresql://guaiguai:mdp@postgresql:5432/postgres')
app = FastAPI()


@app.get("/")
async def root():
    """Create root endpoint for the API"""
    return {"message": "ok"}


@app.post("/masse")
async def get_cat_weight(input: Masse_Input):
    weight = pd.read_sql(f"""SELECT poids FROM public.cat WHERE cat.nom='{input.name}'""", engine)

    if len(weight) > 0:
        res = {"poids": weight.loc[0, "poids"]}
    else:
        res = {"message": "Unkown cat !"}

    return res
