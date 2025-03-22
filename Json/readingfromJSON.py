file = 'guests.txt'

with open(file , 'a') as file_object :
    guest= input('name? :')
while(True):
    if guest== 'quit':
        break
    else:
        file_object.write(guest+"\n")
 









    