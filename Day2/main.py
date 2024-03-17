#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Greeting
print("Welcome to the tip calculator!")
#bill total
total = float(input("What was the total of the bill? "))
#percentage to tip
tip = int(input("What percentage would you like to tip? "))
#How many people
people = int(input("How many ways to split the check?"))
#math
tip_percentage = tip/100
tip_total = tip_percentage * total
total_with_tip = total + tip_total
owes = total_with_tip/people
#How much each owes
print(f"Each person owes ${owes}.")

