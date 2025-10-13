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
print(df)


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
Interpolate()   
check other data , obzerbe then fill it 

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
"""

df.interpolate(method="linear" ,axis=0, inplace= True)


data2 ={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df2 = pd.DataFrame(data)
print('Before Interpoletion')


