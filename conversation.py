dialogs = [
    ("A", "Hello..."),
    ("A", "It's been a long time since we last met."),
    ("A", "How are you?"),
    # Decision point for B
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

def get_decision():
    print("\nB: How should I respond?")
    print("1. I'm doing well, thanks!")
    print("2. Not great, to be honest.")
    print("3. Busy as usual, you know.")
    
    decision = input("Choose your response (1, 2, or 3): ")
    return decision

# Start of conversation
show_dialog(dialogs[:3])

# Decision point for "B"
decision = get_decision()

if decision == "1":
    branch_dialogs = [
        ("B", "I'm doing well, thanks!"),
        ("A", "That's great to hear!"),
        ("A", "What have you been up to lately?"),
        ("B", "Just the usual stuff. How about you?"),
        ("A", "Same here, keeping busy."),
    ]
elif decision == "2":
    branch_dialogs = [
        ("B", "Not great, to be honest."),
        ("A", "Oh no, I'm sorry to hear that."),
        ("A", "Is everything okay?"),
        ("B", "Yeah, just dealing with some personal stuff."),
        ("A", "I'm here if you need someone to talk to."),
    ]
elif decision == "3":
    branch_dialogs = [
        ("B", "Busy as usual, you know."),
        ("A", "Yeah, I can relate. Life has been hectic."),
        ("A", "But it's good to stay productive, right?"),
        ("B", "Absolutely! Can't complain."),
        ("A", "Glad to hear you're doing well."),
    ]
else:
    print("Invalid choice! Let's go with a default response.")
    branch_dialogs = [
        ("B", "I'm doing well, thanks!"),
        ("A", "That's great to hear!"),
        ("A", "What have you been up to lately?"),
        ("B", "Just the usual stuff. How about you?"),
        ("A", "Same here, keeping busy."),
    ]

# Continue the conversation based on the decision
show_dialog(branch_dialogs)
