#Benjamin Flores
#Ben's Theater

#Functions
def theater():
    print("Welcome to Ben's theater")

    type= input("Would you like to watch a movie or tv-show?")
#This is movie route
    if type == "movie":
        genre= input("Got it, would you like to watch a horror or comedy movie?")
        if genre == "horror":
            print("I suggest you go see scream.")
        elif genre == "comedy":
            print("I suggest you go see white chicks.")
    if type == "tv show":
        genre= input("Got it, would like to watch a rom-com or action?")
        if genre == "rom-com":
            print("I suggest you go watch friends.")
        elif genre == "action":
            print("I suggest you go watch the rookie.")
#Main
theater()
