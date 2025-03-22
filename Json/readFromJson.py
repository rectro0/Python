import json

def show_favorite() :
    filename= 'fav.json'

    with open(filename) as obj :
        n= json.load(obj)

    