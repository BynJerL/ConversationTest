const dialog = [
    { speaker: "System", text: "Somewhere, deep inside the dungeon" },
    { speaker: "Jake", text: "Patrice, are you still okay?" },
    { speaker: "Jake", text: "By the way, how about your mana recovery? I hope you didn’t force yourself." },
    { speaker: "Patrice", text: "I’m at 65% of my total mana capacity. Still need 35% more, but it should be enough for now." },
    { speaker: "Jake", text: "Alright, you can recover more when we reach the basecamp." },
    { speaker: "Jake", text: "As long as you stick with me, you’ll be safe, Patrice." },
    { speaker: "Patrice", text: "*chuckles* Okay, I’ll stick with you." },
    { speaker: "System", text: "Suddenly, a choice appears:" }
];

const choices = [
    { choiceText: "Fight the approaching enemy", outcome: [
        { speaker: "Jake", text: "We have no choice, Patrice, prepare for battle!" },
        { speaker: "Patrice", text: "I’m ready!" }
    ]},
    { choiceText: "Retreat to the basecamp", outcome: [
        { speaker: "Jake", text: "We need to fall back to the basecamp!" },
        { speaker: "Patrice", text: "Alright, let's move quickly!" }
    ]}
];

let currentIndex = 0;
let currentDialog = dialog;

const dialogText = document.getElementById("dialog-text");
const nextBtn = document.getElementById("next-btn");
const decisionBtnContainer = document.getElementById("decision-btn-container");
const retryBtn = document.getElementById("retry-btn");

function displayDialog(index) {
    const currentLine = currentDialog[index];
    dialogText.innerText = `${currentLine.speaker}: ${currentLine.text}`;

    if (index < currentDialog.length - 1) {
        nextBtn.style.display = "inline-block";
        decisionBtnContainer.style.display = "none";
        retryBtn.style.display = "none";  // Hide retry button until the end
    } else {
        nextBtn.style.display = "none";
        decisionBtnContainer.style.display = "flex";  // Show choices after last dialog
        retryBtn.style.display = "none";
    }
}

function handleChoice(outcome) {
    currentDialog = outcome;
    currentIndex = 0;
    decisionBtnContainer.style.display = "none";  // Hide decisions after making a choice
    displayDialog(currentIndex);
}

function retryDialog() {
    currentDialog = dialog;
    currentIndex = 0;
    decisionBtnContainer.style.display = "none";
    nextBtn.style.display = "inline-block";
    displayDialog(currentIndex);
}

nextBtn.addEventListener("click", () => {
    currentIndex++;
    if (currentIndex < currentDialog.length) {
        displayDialog(currentIndex);
    } else if (currentDialog === dialog) {
        nextBtn.style.display = "none";  // Hide next button after the last regular dialog
        decisionBtnContainer.style.display = "flex";  // Show decision buttons
    }
});

retryBtn.addEventListener("click", retryDialog);

// Add event listeners to the decision buttons dynamically
choices.forEach((choice, index) => {
    const btn = document.createElement("button");
    btn.innerText = choice.choiceText;
    btn.addEventListener("click", () => {
        handleChoice(choice.outcome);
        retryBtn.style.display = "inline-block";  // Show retry button after decision outcome
    });
    decisionBtnContainer.appendChild(btn);
});

// Start the initial dialog
displayDialog(currentIndex);
