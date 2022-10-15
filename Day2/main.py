print("Welcome to the tip calculator!") 
total = float(input("What is the total bill? $" ))
percentage = int(input("What is the tip percentage? "))
people = int(input("How many people to split the bill with? "))

tip = percentage /100  
total_w_tip = float(tip * total + total)
individual = total_w_tip/ people
final = round(individual, 2)

# individual_total = round(individual, 2)
print(f"Each person owes ${final}")