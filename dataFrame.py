import pandas as pd
#from Student import Student

lst = []

df = pd.DataFrame(lst, columns = ['id', 'Name', 'Last Name', 'Time Checked'])
df.to_csv(r'/Users/yermukhanbet/PycharmProjects/dataBase/venv/lib/python3.7/known/students_dataset.csv')
print(df)