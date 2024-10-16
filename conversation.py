dialogs = [
    ("A", "Hello..."),
    ("A", "It's been a long time since we last met."),
    ("A", "How are you?"),
    ("B", "Me? Good actually."),
    ("B", "And... nice to see you by the way."),
    ("A", "Yeah, it's been too long."),
    ("A", "So, what have you been up to lately?"),
    ("B", "Oh, nothing much, just keeping busy with work."),
    ("B", "What about you? Any exciting news?"),
    ("A", "Well, actually, I've been working on a project lately."),
    ("A", "It's a bit of a secret for now, but I think you'll love it."),
    ("B", "Sounds intriguing! Can't wait to hear more about it."),
    ("B", "When do you plan to reveal this mysterious project?"),
    ("A", "Soon! Just a few more things to sort out."),
    ("B", "I'm excited already! Let me know when you're ready."),
]

pastSpeaker = None
currentSpeaker = None

for dialog in dialogs:
    currentSpeaker = dialog[0]

    if currentSpeaker == pastSpeaker:
        pass
    else:
        print(currentSpeaker + ":")

    print(dialog[1], end="")

    pastSpeaker = currentSpeaker

    input()