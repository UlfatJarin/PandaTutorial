#installation 
# create virtual environment
# # python -m venv myenv
# activate 
# # myenv\Scripts\activate

#pip install pandas
import pandas as pd

# read data from CSV file into a dataframe....................................................

#df = pd.read_csv("SampleSuperstore.xlsx - Orders.csv")
#print(df)



#creating data .......................................................................
data ={
    "Name":['ulfat','jarin','richi'],
    "Age" :[10,20,30],
    "City":["Dhaka","laxmipur","noakhali"]
}

df =pd.DataFrame(data)
print(df)

#data save......................................................................................
#df.to_csv("output.csv",index = False) #to remove index number
#df.to_excel("Output.xlsx") #to remove index number
#df.to_json("Output.json",index=False) #to remove index number

"""
1- understand the data set
2- identify the problem
3- path next steps

"""


#rows .................................................
#head(n) tail(n) #defult n=5
df = pd.read_csv("SampleSuperstore.xlsx - Orders.csv")
 
print('Display 10 rows of first')
#print(df.head(10))

print("\n")

print('Display 10 rows of last')
#print(df.tail(10))


#problems.............................................................
"""
1- how many colums ,rows ?
2- what types of data?
3- missing data?


info()
method 

 1- number of rows and cloums
 2- colum name
 3- int64 float64 object
 4- non null counts
 5- memory usage of data frame 

"""
"""print("\n")
df = pd.read_csv("SampleSuperstore.xlsx - Orders.csv")

print('Displaying the info of data set')
print(df.info())"""

#
"""data ={
    "Name":['ulfat','jarin','richi'],
    "Age" :[10,20,30],
    "City":["Dhaka","laxmipur","noakhali"]
}
df = pd.DataFrame(data)
print('Displaying the info of data set')
print(df.info())"""

#describe.py........................................................................
data ={
    "Name":['ulfat','jarin','richi','saniyat', 'ayan','israt','omi','purni'],
    "Age" :[10,20,30,40,50,60,70,80],
    #"City":["Dhaka","laxmipur","noakhali","Dhaka","laxmipur","noakhali","munsigangh","rajbari"],
    "Salary":[100000,20000,30000,40000,50000,60000,45000,35000],
    "Performance_Score": [85,97,56,98,46,89,46,97]
}
#display the database
df = pd.DataFrame(data)
print("sample DataFrame")
print(df)


"""
#......................................................................................
print("\nDescriptive Statistics") #sumary 
print(df.describe())
count - non missing value 
mean  -  avarage
std - standerad deviation
    - small std  - avarage ar close vlaues
    - large std  - avarage ar teky deffrance besi 
min - minimum value
max - maximum value

25% - lowest values
50% - middele values
75% - highest valuses

"""
#.........................................................................
'''
1- how big is your dataset
2- what are the names of columns

shapes and columns
shape (row ,coulmn)
column


print(f'Shape: { df.shape}')
print(f'Column Names: {df.columns}')
'''
#..................................................................................
"""
1- select  specific column
2- filter rows
3-combine multiple conditions

1- square brackets
2- booleans conditons

selecting columns
1- a series
2- dataframe multiple columns of data

colum =df["Column NAme "]
colums =df["Column1","Column2",....]

print("Names (single Column return series)")
name = df['Name']
print(name)
subset = df[["Name","Salary"]]
print('\nSubset with Name and salary') #multicolumn
print(subset)


filtering rows
1- boolean indexing

#based on a single conditon
filtered_rows = df[df["Salary"]>50000]

high_salary = df[df['Salary']>50000]
print("Empolyees with salary  >  5000")
print(high_salary)


#combined multiple condition
filtered_rows = df[df["Sa;ary"]>50000 & (df["Column2] <800000)]

#and condition
filterd = df[(df['Salary']>40000) & (df['Age']>30)]
print("Employees whose salary >40K & age>30")
print(filterd)
#or condition
filterd = df[(df['Performance_Score']>90) | (df['Age']>35)]
print("Employees whose performance_score >40K | age>35")
print(filterd)
"""


"""#create a new colum .....................................................................
df["Bonus"] = df['Salary'] * 0.1
print(df)"""

"""#.....................................................................................
#using insert() method - direct access  to add a colum 
#df.insert(loc, "column_name" , some data )
df.insert(0, "Employee ID" , [10,20,30,40,50,60,70,80])
print(df)"""

"""print('\n')
#updating values.........................................................................
#.loc[]
#df.loc[row_index , " Colum Name"] = row value
df.loc[0 ,'Salary'] = 150000
print(df)"""

"""print('\n')
#update multiple values..................................................................
#increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print(df)"""


"""#removing columns.........................................................................
#df.drop(columns =["CoumnName"],inplace = true)    implace modify the coulmns
print("modified data")
df.drop(columns= ["Performance_Score"], inplace= True)
print(df) """

"""#removing multiple columns.........................................................................
#df.drop(columns =["CoumnName"], inplace = true)    implace modify the coulmns
print("modified data")
df.drop(columns= ["Performance_Score","Age"], inplace= True)
print(df)"""





 