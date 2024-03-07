print("Welcome to the tip calculator.\n")

t_bill = float(input("What was the total bill?\n"))
p_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
c_people =int(input("How many people to split the bill?\n"))

total = round((t_bill + (t_bill * (p_tip / 100))) / c_people, 2)

print(f"Each person should pay: ${total}")
