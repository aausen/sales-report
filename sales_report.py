"""Generate sales report showing total melons each salesperson sold."""

# Create new lists for salespeople and melons sold
salespeople = []
melons_sold = []

# Opens the file
f = open('sales-report.txt')
# loops through the text 
for line in f:
    line = line.rstrip()
    entries = line.split('|')

# Assigns the entries to new variables to use later in the code
    salesperson = entries[0]
    # makes melon an integer so we can work with it
    melons = int(entries[2])
    # if the new entry is in the list, it will make a variable called position with the first instance of their name
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
    # It will add melons if already in the list
        melons_sold[position] += melons
    # If not in the list, it will add the information to the list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# this will print the name of the salesperson and how many melons they sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
