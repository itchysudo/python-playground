print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? £\n"))
people = int(input("How many people are splitting the bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: £{final_amount}\n")
