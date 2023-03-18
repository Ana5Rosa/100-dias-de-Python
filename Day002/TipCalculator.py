print("Welcome to the tip calculator.")
totalBill = input("What was the total bill? $")
totalPercentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
totalPeople = input("How many people to split the bill? ")

totalBill = float(totalBill)
totalPercentage = float(totalPercentage)
totalPeople = float(totalPeople)

totalPercentage /= 100
result = "{:.2f}".format(round(((totalBill * totalPercentage) + totalBill) / totalPeople, 2))

print(f"Each person should pay: ${result}")