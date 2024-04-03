import pandas as pd
import numpy as np
import pyomo.environ as pyo

import openpyxl

from icecream import ic

path_Excel_File = "Railway services-2024.xlsx"
df = pd.read_excel(io=path_Excel_File, engine="openpyxl")

ic(df.head())