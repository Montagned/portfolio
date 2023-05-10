# function to add a note
def add_note():
    text_file = open("notes.txt", "a")
    note = input("Please enter a note: ")
    text_file.write("\n----\n" + note.strip())
    text_file.close()

# function to look for a note
def search_note():
    text_file = open("notes.txt")
    content = text_file.read()
    array_note = content.split("----")
    print(array_note)
    text_file.close()
    message = ""
    user_note = input("Enter a note to search: ")
    for note in array_note:
        if note.find(user_note) != -1:
            message += "\n----\n" + note
    
    if message == "":
        print("Nothing found!")
    else:
        print(message)
    
# Comunicate with the user
print("What do you want to do?")
print("Press 1 to add a note")
print("Press 2 to search for notes")
user_input = input(": ")

# invoke function according to user response
if user_input == "1":
    add_note()
elif user_input == "2":
    search_note()
else :
    print("Sorry you can only type 1 or 2!")