#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? ₹"))
tip_percentage=float(input("What percentage tip would you like to give? 10,12, or 15? "))
person=int(input("HOw many pepole to split the bill? "))
tip=((bill)*(tip_percentage/100))/(person)
round(tip,2)
pay=round((bill/7)+tip,2)#this could also give 1.9 as answer when 3.8/2 it will not give 1.90
pay="{:.2f}".format(pay)
print(f"Each person should pay: ₹{pay}")