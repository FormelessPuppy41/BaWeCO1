import pandas as pd
import numpy as np
import pyomo.environ as pyo

import openpyxl

from icecream import ic

# Problem is most likely due to the working directory. This must be changed to os.chdir("/path/to/TrainAllocation1") with import os. 
file_path = "Railway services-2024.xlsx"

try:
    df = pd.read_excel(io=file_path, engine="openpyxl")
    ic(df.head())

except FileNotFoundError:
    print(f"File '{file_path}' not found. Please check the file path.")