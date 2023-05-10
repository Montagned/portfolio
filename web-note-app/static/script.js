// Defining constant for the space where the stored user's first name will be displayed
const title = document.getElementById("title");
console.log(title);

// Defining a constant for the textbox above the buttons
const textBox = document.getElementById("textBox");
console.log(textBox);

//Defining a constant for the button to add first name
const addFirstNameButton = document.getElementById("addFirstNameButton");
console.log(addFirstNameButton);

function addFirstName() {
    storageFirstName = textBox.value;
    localStorage.setItem("item", storageFirstName);
    title.innerHTML = "Welcome to the web note app " + textBox.value + "!";
}

// Displaying the data stored in the local storage on the HTML page, global scope
let storageItem = localStorage.getItem("item"); // getting the item key from localStorage

if (storageItem != null) {
        const newItems = document.createElement("p");
        newItems.innerHTML = storageItem;
        newItems.className = "newItemsColor";
        title.innerHTML = "Welcome back to the web note app " + newItems.innerHTML + " !";
        console.log(newItems);
}

addFirstNameButton.addEventListener("click", addFirstName);