Hello, this is a sample project created.

#Files present are as follows:
expense.csv - data file
processor.py - python while which take up the csv data, create a dict of dict which has month data
divided in categories with amounts
database.py - python file which crrates sql connection , consume data from processor file and store
it in db, then also provides a method to fetch the data from db
analyzer.py - python file, which combines processor and database file, it takes up file , passes it to the processor, recive dict of dict, send it to db file and get back data from db
this file also holds all of our routes created by using flask

the routes avaiable are as follows:
/ - home route - it returns just a string hello message
/monthly - it returns all the months and their accomodated total
/highest - it returns all the highest categories per month
/months/<month> - it takes up query param month and returns the categories present in that month
/months/<month>/highest - it returns the highest category of passed month
/months - it returns all the months present

to run the project, run analyzer file, then test routes on browser
