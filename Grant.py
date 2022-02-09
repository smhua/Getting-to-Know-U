from numpy import double
import pandas as pd

df = pd.read_excel("FY21GrantExpbyPI reformat.xlsx")
df.dropna(inplace=True)
empid = df["Emplid"]


for n in range(len(empid)):
    id = str(empid[n])
    id = id[1:-2]
    empid[n] = int(id)


df["Emplid"] = empid
    
df1 = pd.read_excel("PI 2018 Expen_per_ASF.xlsx", sheet_name="Data for Pivot")
df1.dropna(subset= ["PDPI EMPL ID"], inplace=True)

dept_dict = dict(zip(df1["PDPI EMPL ID"], df1["PI Dept"]))
dept_name = []



for x in empid:
    if x in dept_dict:
        dept = dept_dict[x]
        dept_name.append(dept)
    else:
        dept_name.append("Unknown")

df["PI Dept"]= dept_name

df.to_excel("FY21GrantExpbyPI NEW.xlsx", index= False) 