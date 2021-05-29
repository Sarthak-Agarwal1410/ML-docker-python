import pandas as pd
ds=pd.read_csv('/root/SalaryData.csv')
x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary']
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
model=mind.fit(x,y)

print("""
                    |||| Welcome to Salary Predictor App ||||
                          * Press -1 to exit this app *  """)
while(True):
   t=input('Enter number of year experience you have -->> ')
   f=float(t)
   if int(f) < 0 :
      print("Thank You for using our app")
      exit()
   M=model.predict([[f]])
   print("Predicted Salary is :", M, "\n")
