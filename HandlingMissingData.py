#fixed missing data
#NAN = nota a number
#None = for object data type 

import pandas as pd

data ={
    "Name":['ulfat','Jarin','richi','saniyat', 'ayan','israt','omi','purni'],
    "Age" :[10,None,30,40,50,60,None,80],
    #"City":["Dhaka","laxmipur","noakhali","Dhaka","laxmipur","noakhali","munsigangh","rajbari"],
    "Salary":[100000,None,30000,40000,50000,60000,45000,35000],
    "Performance_Score": [85,None,56,98,46,89,46,97]
}
df = pd.DataFrame(data)
print("sample DataFrame")
#print(df)


"""
to detact missing data...........................................
isnull()
true - NaN is missing 
False - value is present

print(df.isnull())
print(df.isnull().sum()) #column a total missing
"""


#handle missing values.............................................
"""
full remove row or column ..........................................
dropna(axis= 0 , inplace = true) 
axis = 0 , full row remove  
axis = 1 , full column remove
inplace  = true  # orginal value modied
"""
"""df.dropna(inplace= True)
print(df)"""

"""
relace by defult value..............................................
fillna(value , inplace = True)

df.fillna(0, inplace=True)
print(df)
"""



"""
relace by calculative value..............................................
fill with a mean() value     mean  = avarage vlaue

df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)
"""

"""
Interpolate()   .........................................................................................
check other data , obzerbe then fill it 
1- time series data
2- numeric data with trends
3- avoid dropping rows

10
20
NOne = 30
40
50

linear
1 - preserve data integrity    (reallity check kore fill korbe )
2 - smooth trend (continuetity mentain )
3 - avoid data loss

linear , polynomial , time
df.interpolate(method="linear" ,axis=0, inplace= True)


data2 ={
    "Time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}
df2 = pd.DataFrame(data2)

print('Before Interpoletion')
print(df2)
df2['value'] =df2['value'].interpolate(method="linear")
print('After Interpolation')
print(df2)
"""

#sorting & aggrigation......................................................................................................
"""
sorting
sorting data in one columns
df.sort_values(by="CoumnName", ascending=True/False, inplace=True )
df.sort_values(by=["CoumnName","Column2"], ascending=[True/False, true/false], inplace=True )

data3 ={
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28,34,22],
    "salary":[10000,20000,30000]
}

df3 = pd.DataFrame(data3) 

#single columns
df3.sort_values(by ="Age", ascending=False , inplace =True)
print('Sorted Age by Decending')
print(df3)

#multipleCOlumns
df3.sort_values(by =["Age","salary"], ascending=[True, False], inplace =True)
print('Sorted Age & salary by Decending')
print(df3)
"""

#summary .......................................................
"""
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()

data3 ={
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28,34,22],
    "salary":[10000,20000,30000]
}

df3 = pd.DataFrame(data3) 

avg_salary =df['Salary'].mean()
print(avg_salary)
min_salary =df['Salary'].min()
print(min_salary)
max_salary =df['Salary'].max()
print(max_salary)

"""


#grouping........................................................

data4 ={
    "Name": ['Arun', 'Varun', 'Karun','Tarun' ,'Narun'],
    "Age": [28,34,22,34,28],
    "Salary":[50000,60000,45000, 52000, 480000]
}

df4 = pd.DataFrame(data4) 
grouped = df4.groupby("Age")["Salary"].sum()
#print(grouped)
"""
df4.groupby("Age")
age =22>[45000]
age =28>[50000,480000]
age =24 >[60000 , 52000]

[Salary].sum()
age =22>[45000]
age =28>[50000,480000]   = 530000
age =24 >[60000 , 52000] = 11200

"""
#multiple column grp
grouped = df4.groupby(["Age","Name"])["Salary"].sum()
#print(grouped)



#Common aggrigation functions
"""
1- sum() - grp a sum 
2- mean()
3- count()
4- min()
5- max()
6- std()
"""



