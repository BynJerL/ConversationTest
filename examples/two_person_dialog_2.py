dialog = [
    ("System", "Somewhere, inside the dungeon"),
    ("Girl", "Jake, are you still okay?"),
    ("Jake", "Don\'t worry. I\'m still in good shape."),
    ("Jake", "By the way, how\'s your mana recovery? I hope you didn\'t push yourself too hard."),
    ("Girl", "I have about 65% of my mana left. I need 35% more, but this should be enough."),
    ("Jake", "Alright, you can recover fully at the basecamp."),
    ("Jake", "As long as you stay with me, you\'ll be safe, Patrice."),
    ("Patrice", "*chuckles* Okay, I\'ll stick with you.")
]
    
def show_dialog(dialogs):
    past_speaker = None

    for dialog in dialogs:
        current_speaker = dialog[0]

        if current_speaker != past_speaker:
            print(f"\n{current_speaker}:")
        
        print(f"{dialog[1]}", end="")
        input()  # Wait for user input to simulate continuation

        past_speaker = current_speaker
    
show_dialog(dialog)