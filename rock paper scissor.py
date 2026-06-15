import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor): ").strip().title()
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Match Tie!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer wins")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer wins")
    else:
        print("Paper covers Rock = You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper = You win")
    else:
        print("Rock smashes Scissor = Computer wins")

else:
    print("Invalid choice! Enter Rock, Paper, or Scissor.")