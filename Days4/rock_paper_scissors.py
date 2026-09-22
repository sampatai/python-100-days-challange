import random

#random=random.randint(1,100)
#print(f"Welcome to Rock Paper Scissors! {random}")
# random_numer_0to_1=random.random()*10
# print(random_numer_0to_1)
# random=random.randint(0,1)
# if random==1:
#     print("tails")
# else:
#     print("heads")

2
rock = "🪨"
paper = "📄"
scissors = "✂️"

game_images=[rock,paper,scissors]
user_choice=int( input("Enter your choice? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print(f"computer choice :")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You typed an invalid choice.")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==0 and computer_choice==2:
    print("You lose!")
elif computer_choice> user_choice:
    print("You lose!")
elif user_choice>computer_choice:
    print("You win!")
elif computer_choice== user_choice:
    print ("It's a tie!")


