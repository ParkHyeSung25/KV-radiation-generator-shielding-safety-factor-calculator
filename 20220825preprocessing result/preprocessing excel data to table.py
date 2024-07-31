import numpy as np
import pandas as pd
import openpyxl

filename = "C:/Users/HyeSungPark/PycharmProjects/pythonProject/RG/20220825xlsx/300kV_concrete.xlsx" #파일명
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]
data = [] 
for row in sheet.rows:
    data.append([
        row[0].value,
        row[1].value,
])
print(data)