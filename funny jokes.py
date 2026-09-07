
# 1 - Import the random module
import random


# 2 - Create subjects
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declare war on",
    "orders",
    "celebrates",
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a Plate of Samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate",
]


# 3 - Start the headline generation loop
while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input(
        "\nDo you want another headline? (yes/no): "
    ).strip().lower()

    if user_input == "no":
        break


# Print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
