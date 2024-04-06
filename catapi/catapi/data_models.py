#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

from pydantic import BaseModel


class Masse_Input(BaseModel):
    name: str

