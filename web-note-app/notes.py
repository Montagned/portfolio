import flask
app = flask.Flask("web_note_app")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_notes():
    contactsdb = open("notes.txt")
    content = contactsdb.read()
    contactsdb.close()
    notes = content.split("\n")
    return notes

# This function displays the home.html page
@app.route("/home")
def homepage():
    return get_html("home")

@app.route("/")
def welcome_page():
    html_page = get_html("index")
    return html_page

# by clicking on the "add note button" I'm adding a note to the notes array which I retrieved 
# from the text file, in the meantime I append this value to the notes.txt. 
@app.route("/notes")
def add_note():
    html_notes_page = get_html("notes")
    notes = get_notes()
    text_file = open("notes.txt", "a")
    message = flask.request.args.get("new_note")
    if message != None:
        notes.append(message)
        text_file.write("\n" + message)
    text_file.close()
    actual_note = ""

    for note in notes:
        actual_note += "<p>" + note + "</p>"
        
    return html_notes_page.replace("$$NOTES$$", actual_note)

# By opening this page the content of the text file gets displayed in different paragraphs
@app.route("/notes")
def notes_page():
    html_page = get_html("notes")
    notes = get_notes()
    actual_note = ""

    for note in notes:
        actual_note += "<p>" + note + "</p>"

    return html_page.replace("$$NOTES$$", actual_note)

# By opening this page through the search button I'm looping through the array
# which I retrieved from the text file notes.txt
@app.route("/search")
def search_page():
    found_note = ""
    html_page = get_html("notes")
    message = flask.request.args.get("searched_note")
    notes = get_notes()
    for note in notes:
        if note.lower().find(message.lower()) != -1:
            found_note += "<p>" + note + "</p>"

    return html_page.replace("$$NOTES$$", found_note)