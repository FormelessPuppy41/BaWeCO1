import pandas as pd
import numpy as np
import pyomo.environ as pyo

import openpyxl

from icecream import ic

df = pd.read_excel(io="Railway services-2024.xlsx", engine="openpyxl")

ic(df.head())