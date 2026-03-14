import pandas as pd
import numpy as np


Names=["Uday","Aman","Naman","Badal"]
Maths=[67,54,60,89]
Science=[87,56,43,89]
English=[54,38,96,54]

Dicti={
    "Names":Names,
    "Maths":Maths,
    "Science":Science,
    "English":English
}

df=pd.DataFrame(Dicti)

df["Average"]=np.round(df[["Maths","Science","English"]].mean(axis=1),2)

df["Result"]=np.where(df["Average"]>=60,"Pass","Fail")

conditions=[
df["Average"]>=85,
(df["Average"]>=70) & (df["Average"]<85),
(df["Average"]>=60) & (df["Average"]<70),]

choices=["A","B","C"]

df["Grade"]=np.select(conditions,choices,default="D")










print("      | | | STUDENTS REPORT | | |")
print()
print(df)
print()

print("      ×××FAILED STUDENTS×××")
print()
print(df[df["Average"]<60])
print()

print("     ^^^ABOVE 75avg STUDENTS^^^")
print()
print(df[df["Average"]>=75])
print()

print("    ---STUDENTS WHO FAILED IN SCIENCE---")
print()
print(df[df["Science"]<40])
print()

print("NO ONE +++")

print()

print("    (A) GRADE STUDENTS ")
print()
print(df[df["Grade"]=="A"])
print()


print('NO ONE ---')
