import pandas as pd

#margging or concatagaring...................................
"""
margging
pd.merge(df1,df2, on="Column_Name",how ="type of  join")


"""
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh'],
})

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

df_merged = pd.merge(df_customers , df_orders, on="CustomerID", how="inner")
print("inner join")
#print(df_merged)

print("\n")
df_merged = pd.merge(df_customers , df_orders, on="CustomerID", how='outer')
print("outer join")
#print(df_merged)

print("\n")
df_merged = pd.merge(df_customers , df_orders, on="CustomerID", how='left')
print("left join")
#print(df_merged)

print("\n")
df_merged = pd.merge(df_customers , df_orders, on="CustomerID", how='right')
print("right join")
#print(df_merged)

#cross marge
"""
1st df = m rows
2nd df = n rows
cross marge = m*n
"""

#conctination..............................................................................
"""
data frames combine 
vertically 
horizontally
pd.concate([df1, df2], axis =0, ignore_index= true)

[df1,df2] =
axis = 1

ignore_index = True
"""
df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Mina','Raju']
})
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Mithu','Lali']
})
#defult =vertically
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concat)

print("\n")
#horizontally
df_concat = pd.concat([df_Region1, df_Region2],axis=1, ignore_index=True)
print(df_concat)
