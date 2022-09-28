from openpyxl import Workbook,load_workbook
import postgresql
import pandas as pd
import numpy as np
import matplotlib as plt
import os
import glob
#wb = load_workbook('/Users/senan/Desktop/list.xlsx')
wb =pd.read_excel('/Users/senan/Desktop/list.xlsx')
wb.head()
test=wb.filter(items=['Alias','Gender','Age','BMI'])
#print(test)
#test.dropna(['No'], axis =1)
wb.drop(columns=['No'], axis =1)
bmi_idx = []
for b in wb["BMI"]:
    if b <= 24.9:
        bmi_idx.append(0)
    elif 25 <= b < 29.9:
        bmi_idx.append(1)
    elif 29.9 <= b:
        bmi_idx.append(2)
    else:
        bmi_idx.append(None)
wb["BMI_idx"] = bmi_idx
age_idx = []
for age in wb["Age"]:
    if age <= 39:
        age_idx.append(0)
    elif 40 <= age <= 59:
        age_idx.append(1)
    elif 60 <= age:
        age_idx.append(2)
    else:
        bmi_idx.append(None)
wb["Age_idx"] = age_idx
#for r in wb["Region"].dropna().unique():
for g in wb["Gender"].dropna().unique():
    for b in sorted(wb["BMI_idx"].dropna().unique()):
        for age in sorted(wb["Age_idx"].dropna().unique()):
        #print(r, g, b)
            res = wb.loc[((wb['Gender'] == g) & (wb['BMI_idx'] == b)  & (wb['Age_idx'] == age)) ,'Alias']
            print("Combination: ", g, b, age)
            for it in  res.to_list():
                print(f"\t{it}")
            print("\n")
