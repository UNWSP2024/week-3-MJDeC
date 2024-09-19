# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

#Taking user dog order using number inputs.
dog_type=float(input("Enter 1 for Hot Dog or 2 for Chili Dog."))
cheese=float(input("If you would like cheese, press 1. Else, press 0."))
peppers=float(input("Press 1 to add peppers to your dog. Else, press 0."))
onions=float(input("For onions, press 1. Else, press 0."))
you_idiot="Please enter a real menu selection, you idiot."

dog_cost=0
cheese_cost=0
pepper_cost=0
onion_cost=0

#Determining user choice prices.
if dog_type==1:
  dog_cost=3.50
elif dog_type==2:
  dog_cost=4.50
else:
  print(you_idiot)

if cheese==1:
  cheese_cost=.50
elif cheese==0:
  cheese_cost=0
else:
  print(you_idiot)

if peppers==1:
  pepper_cost=.75
elif peppers==0:
  pepper_cost=0
else:
  print(you_idiot)

if onions==1:
  onion_cost=1.00
elif onions==0:
  onion_cost=0
else:
  print(you_idiot)

#Calculating costs.
subtotal=(dog_cost+cheese_cost+pepper_cost+onion_cost)
tax=(.07*subtotal)
total=(subtotal+tax)

#Final display.
print('Your subtotal is $', subtotal)
print('Your tax is $', format(tax, '.2f'))
print('Your grand total is $', format(total, '.2f'))
