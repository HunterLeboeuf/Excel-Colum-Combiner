import pandas as pd
from openpyxl import load_workbook


df = pd.read_excel("C:\\Users\\Hunter\\Desktop\\test.xlsx")


# List's to grab each column 
list1 = [ ]
list2 = [ ]
list3 = [ ]

# Gather the data using pandas 
list1 = df.loc[:, "t1"]
list2 = df.loc[:, "t2"]

# Combine both column 1 and column 2 for column 3 using extend 
list3.extend(list1)
list3.extend(list2)

# Loads the workbook to print list 3 to 
wb = load_workbook('C:\\Users\\Hunter\\Desktop\\test.xlsx')
ws = wb.active

# row incrementer set below title of row
v = 2
# Loop through list3 and add it to to specified location V is to increment the row change column to location needed to print the comined list 
for x in list3:
    ws.cell(column=3, row=v, value=x)
    v = v + 1
    
# Save the workbook change to your xlsx file path     
wb.save('C:\\Users\\Hunter\\Desktop\\test.xlsx')