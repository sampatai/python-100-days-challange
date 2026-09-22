print("Welcome to the rollercoaster!")

height=int(input("What is your height in cm? "))
bill=0

if height>=120:
   print("You can ride the rollercoaster!")
   age=int(input("How old you are? "))
   if age<=12:
       bill=5
       print("Child tickets are $5")
   elif age<=18:
       bill=10
       print("Youth tickets are $10")
   else:
       bill=15
       print("Adult tickets are $15")
wants_photo=input("Would you like to see a photo? (y/n)")
if wants_photo=="y":
    bill+=3
    print(f"Your final bill is {bill}")
else:
   print("Sorry, you cannot ride the rollercoaster!")