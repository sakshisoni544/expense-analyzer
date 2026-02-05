def process_expenses(fileName):
    fileHandler = open(fileName)
    expenses = {}
    for lines in fileHandler:
        lines = lines.strip().split(',')
        if len(lines) < 1 or lines[0] == 'date': continue
        month = lines[0][:7]
        category = lines[1]
        amount = float(lines[2])

        if month not in expenses:
            expenses[month] = {}
        if category not in expenses[month]:
            expenses[month][category] = 0
        expenses[month][category] += float(amount)     
    return expenses       