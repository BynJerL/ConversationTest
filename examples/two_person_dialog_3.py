dialog = [
    ("System", "Somewhere, deep inside the dungeon"),
    ("Jake", "Patrice, we’ve reached a crossroads. There are two paths ahead."),
    ("Jake", "One leads to the lower chambers, the other might take us closer to the exit."),
    ("Jake", "I think we should decide carefully. What do you think?"),
]

decisions = {
    "lower": [
        ("Patrice", "Let’s head to the lower chambers. There might be something valuable down there."),
        ("Jake", "Alright, but stay on your guard. It’s dangerous down there."),
        ("System", "They descend deeper into the dungeon, the air growing colder and the sounds of creatures echoing in the distance."),
    ],
    "exit": [
        ("Patrice", "I think we should move toward the exit. We need to regroup and recover."),
        ("Jake", "You’re right. We’ll come back better prepared."),
        ("System", "They make their way toward the exit, avoiding dangerous traps and creatures, but losing the opportunity to explore further."),
    ]
}

def show_dialog(dialogs):
    past_speaker = None

    for dialog in dialogs:
        current_speaker = dialog[0]

        if current_speaker != past_speaker:
            print(f"\n{current_speaker}:")
        
        print(f"{dialog[1]}", end="")
        input()  # Wait for user input to simulate continuation

        past_speaker = current_speaker

def make_decision():
    print("\nWhich path will you choose?")
    print("1. Lower chambers")
    print("2. Exit")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        return "lower"
    elif choice == "2":
        return "exit"
    else:
        print("Invalid choice, try again.")
        return make_decision()

# Show initial dialog
show_dialog(dialog)

# Make a decision
decision = make_decision()

# Show the result of the decision
show_dialog(decisions[decision])