import sqlite3

connection = sqlite3.connect('expense-analyzer-v2')
cursor = connection.cursor()

cursor.executescript('''
drop table if exists monthly_expenses;
create table monthly_expenses (month text, category text, amount text, primary key(month, category))                     
''')

def save_data(expenses):
    for (month, categories) in expenses.items():
     for (category, amount) in categories.items():
        cursor.execute('insert into monthly_expenses (month, category, amount) values (?, ?, ?)', (month, category, amount))
    connection.commit()    

def fetch_data():
   totals = {}
   query = 'select * from monthly_expenses order by month'
   for data in cursor.execute(query):
      month = str(data[0])
      category = str(data[1])
      amount = float(data[2])
      if(month) not in totals:
         totals[month] = {}
      if(category) not in totals[month]:
         totals[month][category] = 0
      totals[month][category] += float(amount)
   return totals       