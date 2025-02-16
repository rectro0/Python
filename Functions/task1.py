def make_album(name , title ):
    tracks = input("put the number of tracks: ")
    decinary = {"artist": name, "album": title ,"tracks": tracks}
    return decinary



album = make_album('star ', 'dick')
print(album)


magicians= ['oker','davinci','sick','batman']

def make_great(magicians):
    for mage in magicians:
        msg = "great "+mage.title()+"!"
        print(msg)
make_great(magicians)



 #? arbitrary number of argument in funtion
def sandiwch(*addons):
    for s in addons:
        print(s+" added")


sandiwch("tomato")
sandiwch('pepper','katshup','mayo')


def build_profile(first, last ,**user_info):
 profiles={}
 profiles['first_name'] = first
 profiles['last_name'] = last
 for key , value in user_info.items():
     profiles[key] = value
     return profiles

user_profile = build_profile('sawli' , 'mohammed' , education = 'University' , field = 'computer science')

print(user_profile)



def cars(manufactor , model , **car_info):

    car = {}
    car['company_name'] = manufactor
    car['model_series'] = model

    for key, value in car_info.items():
        car[key] = value
        return car


car_profile = cars('toyota' , 'corrola' , color= 'white' , transmission= 'manual')

print(car_profile)


#* importing functions from files (models)
import diconarry.task1
from LISTS import gust as g

g.dinner_guests()


 