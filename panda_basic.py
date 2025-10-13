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

df = pd.DataFrame(data)
print("sample DataFrame")
print(df)


#......................................................................................
print("\nDescriptive Statistics")
print(df.describe())

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





 