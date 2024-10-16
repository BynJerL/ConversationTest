const dialog = [
    { speaker: "System", text: "Somewhere, deep inside the dungeon" },
    { speaker: "Jake", text: "Patrice, we’ve reached a crossroads. There are two paths ahead." },
    { speaker: "Jake", text: "One leads to the lower chambers, the other might take us closer to the exit." },
    { speaker: "Jake", text: "I think we should decide carefully. What do you think?" }
];

const decisions = {
    lower: [
        { speaker: "Patrice", text: "Let’s head to the lower chambers. There might be something valuable down there." },
        { speaker: "Jake", text: "Alright, but stay on your guard. It’s dangerous down there." },
        { speaker: "System", text: "They descend deeper into the dungeon, the air growing colder and the sounds of creatures echoing in the distance." }
    ],
    exit: [
        { speaker: "Patrice", text: "I think we should move toward the exit. We need to regroup and recover." },
        { speaker: "Jake", text: "You’re right. We’ll come back better prepared." },
        { speaker: "System", text: "They make their way toward the exit, avoiding dangerous traps and creatures, but losing the opportunity to explore further." }
    ]
};

let currentIndex = 0;
let currentDialog = dialog;

const dialogText = document.getElementById("dialog-text");
const nextBtn = document.getElementById("next-btn");
const choicesDiv = document.getElementById("choices");

function displayDialog(index) {
    const currentLine = currentDialog[index];
    dialogText.innerText = `${currentLine.speaker}: ${currentLine.text}`;
    
    if (index < currentDialog.length - 1) {
        // Show "Next" button if there are more lines to display
        nextBtn.style.display = "inline-block";
        choicesDiv.innerHTML = "";  // Ensure decision buttons are hidden
    } else {
        // Hide the "Next" button and show the decision options at the end of the initial dialog
        nextBtn.style.display = "none";
        makeDecision();
    }
}

function makeDecision() {
    choicesDiv.innerHTML = `
        <button onclick="choose('lower')">Go to the lower chambers</button>
        <button onclick="choose('exit')">Head toward the exit</button>
    `;
}

function choose(path) {
    currentDialog = decisions[path];
    currentIndex = 0;
    choicesDiv.innerHTML = "";  // Hide decision buttons after choosing
    displayDialog(currentIndex); // Start the new path dialog
}

nextBtn.addEventListener("click", () => {
    currentIndex++;
    if (currentIndex < currentDialog.length) {
        displayDialog(currentIndex);
    }
});

// Start the initial dialog
displayDialog(currentIndex);
