import random

print('Welcome to Rock, Paper ,Scissor Game.\nType "0" for Rock, "1" for Paper, "2" for Scissor.')
my_input = int(input("Your choice : "))
choice_name = ["Rock", "Paper", "Scissor"]
random_choice = random.randint(0, 2)
print(f"You choose : {choice_name[my_input]}")
print(f"Computer choose : {choice_name[random_choice]}")
if my_input > random_choice:
    print("You win!!!")
elif my_input == 0 and random_choice == 2:
    print("You win!!!")
elif my_input == random_choice:
    print("Its a draw!!!")
else:
    print("You Loose.")
