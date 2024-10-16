dialog = [
    ("Man 1", "Life is so hard these days."),
    ("Man 1", "Finding a job is getting harder."),
    ("Man 1", "And prices keep going up every year. It’s so frustrating, y’know?"),
    ("Man 2", "Yeah, but we’ve got to face it."),
    ("Man 2", "We need to survive and look for new opportunities."),
    ("Man 2", "Complaining doesn’t help much. It’s better to focus on the next steps."),
    ("Man 1", "You’re right, friend. But I really need to talk about this."),
    ("Man 1", "As a friend, I want your advice."),
    ("Man 1", "It’s tough out there, but have you found any way to deal with it?"),
    ("Man 2", "Honestly, I don’t have a great solution. I’m just waiting for some good news."),
    ("Man 2", "Right now, I’m relying on my current job, even though the pay is just enough."),
    ("Man 2", "Maybe it’s not the right time for growth, or maybe the opportunities are just hidden."),
    ("Man 1", "Haha! That’s life for you. There’s no easy way to solve problems.")
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
