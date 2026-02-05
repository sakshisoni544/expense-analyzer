from processor import process_expenses
from database import save_data, fetch_data
from flask import Flask, jsonify
app = Flask(__name__)

csvData = process_expenses('./data/expense.csv')
save_data(csvData)
fetchedData = fetch_data()
# monthly_expenses = {}
# category_wise_expenses = []
# for (month, categories) in data.items():
#     print('Month is: ', month)
#     print(month, categories)
#     category_wise_expenses = []
#     for (c, amount) in categories.items():
#         category_wise_expenses.append((amount,c))
#         monthly_expenses[month] = monthly_expenses.get(month, 0) + amount
#     category_wise_expenses.sort(reverse=True)
#     print(f'Highest of the month {month}', category_wise_expenses[0], '\n' )    

@app.route("/")
def home():
   return 'This is home page of application'
        

@app.route('/monthly')
def monthly():
    monthly_expenses = {}
    for (month, categories) in fetchedData.items():
     for (category, amount) in categories.items():
        monthly_expenses[month] = monthly_expenses.get(month, 0) + amount
    return jsonify(monthly_expenses)

@app.route('/highest')
def highest():
    result = []
    for (month, categories) in fetchedData.items():
     category_wise_expenses = [] 
     for (c, amount) in categories.items():
        category_wise_expenses.append((amount,c))
        category_wise_expenses.sort(reverse=True)
     result.append({"month": month, "category": category_wise_expenses[0]})
    return jsonify(result) 

@app.route('/months/<month>')
def monthWise(month):
   return jsonify(fetchedData.get(month, {}))

@app.route('/months/<month>/highest')
def monthHighest(month):
   result = []
   for category,amount in fetchedData.get(month, {}).items():
      result.append((amount,category))

   result.sort(reverse=True)  
   if len(result) > 0:
    return({"month": month, "category": result[0][1], "amount": result[0][0]})
   else:
      return({'error': 'Month not found'})
   
@app.route('/months')
def months():
   available_months = []
   for months,categories in fetchedData.items():
      available_months.append(months)
   return jsonify(available_months)   


      


if __name__ == '__main__':
    app.run(debug=True)





