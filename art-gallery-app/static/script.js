//Defining a constant for the div which will receive the custumer preference images
const parent = document.getElementById("parent");

//Defining a constant for the button to add first name
const addFullNameButton = document.getElementById("addFullNameButton");

// Defining a constant for the text box which is receiving the first name
const textBox = document.getElementById("textBox");

// Defining a constant for the button which will log out by clearing the local storage

const clearButton = document.getElementById("clearButton");
const textBoxClear = document.getElementById("textBoxClear");

function addFullName() {
    storageFullName = textBox.value;
    localStorage.setItem("Full name", storageFullName);
    history.go(0);
    }

function logOut() {
    localStorage.clear();
    history.go(0);
}

// Defining two constants for the buttons that add a preference in the art choice
const impressionismChoiceButton = document.getElementById("impressionismChoiceButton");
const expressionismChoiceButton = document.getElementById("expressionismChoiceButton");

function addImpressionismChoice() {
    localStorage.setItem("preference", "impressionism");
}

function addExpressionismChoice() {
    localStorage.setItem("preference", "expressionism");
}

// Event listeners to add full name to the local storage and to clear it

addFullNameButton.addEventListener("click", addFullName);

clearButton.addEventListener("click", logOut);

impressionismChoiceButton.addEventListener("click", addImpressionismChoice);
expressionismChoiceButton.addEventListener("click", addExpressionismChoice);

// Defining a constant for the welcome message to the costumer
const welcomeMessage = document.getElementById("welcomeMessage");

// Defining code in order to display the costumer's full name...

let costumerFullName = localStorage.getItem("Full name");
if (costumerFullName != null && costumerFullName != "") {
    const message = document.createElement("h2");
    message.innerHTML = "Dear " + costumerFullName + ", here are some artworks that may be of interest for you...";
    welcomeMessage.appendChild(message);
}

//  and his/her art preferences

// creating constants to store the dfifferent images in two different arrays(line 56 and 57)
const bohèmienne = "static/renoir-bohèmienne.jpg";
const balancoire = "static/renoir-balancoire.jpeg";
const autoportrait = "static/renoir-autoportrait.jpg";
const canoeists = "static/renoir-canoeists.jpeg";
const scream = "static/munch-the-scream.jpg";
const dancers = "static/nolde-candle-dancers.jpg";
const junks = "static/nolde-junks.jpg";
const vrouwenkop = "static/jawlensky-vrouwenkop.jpg";
imprImagesArray = [bohèmienne, balancoire, autoportrait, canoeists];
exprImagesArray = [scream, dancers, junks, vrouwenkop];

let preferenceItem = localStorage.getItem("preference");
if (preferenceItem != null) {
    parent.className = "imagesContainer";
    if (preferenceItem == "impressionism") {
        for (let i = 0; i < imprImagesArray.length; i++) {
            const impressionismImages = document.createElement("img");
            impressionismImages.className = "preferenceImage";
            impressionismImages.src = imprImagesArray[i];
            parent.appendChild(impressionismImages);
            }
    } else if (preferenceItem == "expressionism") {
        for (let i = 0; i < exprImagesArray.length; i++) {
            const expressionismImages = document.createElement("img");
            expressionismImages.className = "preferenceImage";
            expressionismImages.src = exprImagesArray[i];
            parent.appendChild(expressionismImages);
            }
        } 
                            }

const followUsButton = document.getElementById("followUsButton");
const getItemBox = document.getElementById("getItemBox");
getItemBox.style.visibility = "hidden";

function retreiveInfos() {
    let preference = localStorage.getItem("preference");
    let fullName = localStorage.getItem("Full name");
    let followerInfos = fullName + ", art preference: " + preference;
    

    getItemBox.value = followerInfos;
    console.log(followerInfos);

}
console.log(followUsButton);
console.log(getItemBox);

followUsButton.addEventListener("click", retreiveInfos)