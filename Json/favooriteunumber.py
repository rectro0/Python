import json
from readFromJson import show_favorite
filename= 'fav.json'
number = show_favorite()
if number:
    print('I know your favorite number is : '+ number)
else:
    number = input('favorite number :')
    with open(filename ,'w')as f_obj :
        json.dump(number)       
