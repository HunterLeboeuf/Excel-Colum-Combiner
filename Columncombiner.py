import pandas as pd
from openpyxl import load_workbook

df = pd.read_excel("C:\\Users\\Hunter\\Desktop\\test.xlsx")
path = "C:\\Users\\Hunter\\Desktop\\test.xlsx"

list1 = [ ]
list2 = [ ]
list3 = [ ]

list1 = df.loc[:, "t1"]
list2 = df.loc[:, "t2"]

list3.extend(list1)
list3.extend(list2)

print(list3)

wb = load_workbook('C:\\Users\\Hunter\\Desktop\\test.xlsx')
ws = wb.active


v = 2
for x in list3:
    ws.cell(column=3, row=v, value=x)
    v = v + 1
    
    
wb.save('C:\\Users\\Hunter\\Desktop\\test.xlsx')