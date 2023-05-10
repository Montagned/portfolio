import flask
import datetime

app = flask.Flask("Gallery")

renoir = datetime.date(1841, 2, 25)
nolde = datetime.date(1867, 8, 7)
kandinsky = datetime.date(1866, 12, 16)
jawlensky = datetime.date(1864, 3, 13)
monet = datetime.date(1840, 11, 14)
munch = datetime.date(1862, 12, 12)

# Constructor for the Artwork objects
class Artwork :

    def __init__(self, artwork_name, author, height, width, date, museum, place, image_file):
        self.artwork_name = artwork_name
        self.height = height
        self.width = width
        self.author = author
        self.date = date
        self.museum = museum
        self.place = place
        self.image_file = image_file

    def find_age(self, birth):
        return self.artwork_name + " was painted by " + self.author + " at the age of " + str(self.date - birth)

#Artwork OBJECTS

# 1) Bohèmienne by Renoir

bohèmienne = Artwork("La Bohèmienne", "Auguste Renoir", 85, 59, 1868, "Alte Nationalgalerie", "Berlin", "renoir-bohèmienne.jpg")

# 2) Canoeists by Renoir

canoeists = Artwork("Le Déjeuner des canotiers", "Auguste Renoir", 130, 173, 1881, "The Philips Collection", "Washington", "renoir-canoeists.jpeg")

# 3) Autoportrait by Renoir

autoportrait = Artwork("Autoportrait", "Auguste Renoir", 39, 31, 1875, "Clark Art Intitute", "Williamstown, Massachusetts", "renoir-autoportrait.jpg")

# 4) balancoire by Renoir

balancoire = Artwork("La balançoire", "Auguste Renoir", 92, 73, 1876, "Musée d'Orsay", "Paris", "renoir-balancoire.jpeg")

# 5) Candle dancers by Emil Nolde

dancers = Artwork("Candle dancers", "Emil Nolde", 100, 86, 1912, "Nolde Stiftung Seebüll", "Neukirchen", "nolde-candle-dancers.jpg")

# 6) Junks by Emil Nolde

junks = Artwork("Junks", "Emil Nolde", 24, 33, 1913, "Nolde Stiftung Seebüll", "Neukirchen", "nolde-junks.jpg")

# 7) Vrouwenkop by Alexej von Jawlensky

vrouwenkop = Artwork("Vrouwenkop", "Alexej von Jawlensky", 55, 51, 1911, "Gemeentemuseum", "Den Haag", "jawlensky-vrouwenkop.jpg")

# 8) Murnau mit Kirche by Wassily Kandinsky

murnau = Artwork("Murnau mit Kirche", "Wassily Kandinsky", 64, 50, 1910, "Städtische Galerie im Lenbachhaus", "München", "kandinsky-murnau.jpg")

# 9) Scream by Edvard Munch

scream = Artwork("The scream (Norwegian: Skrik)", "Edvard Munch", 91, 73, 1893, "National Gallery", "Oslo", "munch-the-scream.jpg")

# 10) Etang des ninfee by Claude Monet

ninfee = Artwork("Etang des Ninfee", "Claude Monet", 89, 93, 1899, "Musée Puskin", "Moscow", "monet-étang-des-ninfee.jpg")


# Through the index.html route, I'm displaying the html content...

def get_html(page):
    html_file = open(page + ".html")
    html_content = html_file.read()
    html_file.close()

    return html_content

#  as well as writing the user's Full name into the text-file

@app.route("/")
def get_index():
    html_page = get_html("index")

    text_file = open("followersInfos.txt", "a")
    
    follower_info = flask.request.args.get("followersInfos")
    if follower_info != None:
        text_file.write("\n" + follower_info)

    text_file.close()

    return html_page
    
# This page will display all the expressionist artworks
@app.route("/expressionism")
def get_expressionism():
    html_page = get_html("expressionism")

    return html_page

# This page will display all the impressionist artworks
@app.route("/impressionism")
def get_impressionism():
    html_page = get_html("impressionism")
    return html_page

# Building a function in order to create automatically all the objects from the class

def create_object(painting, canvas, painter_birth):
    message = " was born on {:%A, %d %B, %Y}. "
    painting_info = ("<div class='frame_info'><img src='static/"+ canvas + "'" + " height=400 width=340></div>" + "<br>" 
                    + "<p class='paragraph'>" + "Artwork name: " + str(painting.artwork_name) + " <br>" 
                    + "Height: " + str(painting.height)  + " <br>" 
                    + "Width: " + str(painting.width)  + " <br>"
                    + "Date of creation: " + str(painting.date) + " <br>"
                    + "Museum: " + str(painting.museum) + " <br>"
                    + "Location: " + str(painting.place)   + " <br>"
                    + painting.author + message.format(renoir) + "<br>"
                    + painting.find_age(painter_birth.year) + "</p>")
    return painting_info
                
# With this route I'm retrieving informations from the different artwork objects,
# in order to create an info page for each artwork
@app.route("/info")
def get_info():
    html_page = get_html("info")

    message = " was born on {:%A, %d %B, %Y}. "
    if flask.request.args.get("bohèmienne"):
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(bohèmienne, bohèmienne.image_file, renoir))
    elif flask.request.args.get("canoeists"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(canoeists, canoeists.image_file, renoir))
    elif flask.request.args.get("autoportrait"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(autoportrait, autoportrait.image_file, renoir))
    elif flask.request.args.get("balancoire"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(balancoire, balancoire.image_file, renoir))
    elif flask.request.args.get("vrouwenkop"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(vrouwenkop, vrouwenkop.image_file, jawlensky))
    elif flask.request.args.get("scream"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(scream, scream.image_file, munch)) 
    elif flask.request.args.get("murnau"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(murnau, murnau.image_file, kandinsky))    
    elif flask.request.args.get("dancers"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(dancers, dancers.image_file, nolde))
    elif flask.request.args.get("junks"): 
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(junks, junks.image_file, nolde))   
    elif flask.request.args.get("ninfee"):
        return html_page.replace("$$ARTWORK_INFOS$$", create_object(ninfee, ninfee.image_file, monet))


# Retrieving the users names from the text file once the owner of the website,
#  typed the right password: g@llery.

@app.route("/preferences")
def get_followersInfos():
    html_page = get_html("preferences")

    text_file = open("followersInfos.txt")
    text_content = text_file.read()
    followers = text_content.split("\n")
    text_file.close()
    password = flask.request.args.get("password")
    log_out = flask.request.args.get("log out")
    
    actual_follower = ""
    for follower in followers:
        if follower != "":
            actual_follower += "<p>" + follower + "<p>"
    text_file.close()
    
    if password == "g@llery":
        return html_page.replace("$$PREFERENCES$$", actual_follower)
    elif log_out == "log out":
        return html_page.replace("$$PREFERENCES$$", "<h4>You've logged out successfully!</h4>")
    elif password == None or password == "":
        return html_page.replace("$$PREFERENCES$$", "")
    elif password != "g@llery":
        return html_page.replace("$$PREFERENCES$$", "<h4>Sorry, wrong password!</h4>")
    