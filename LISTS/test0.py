"""
games = ['godofwar', 'ghostrecon', 'monsterhunter', 'reddead', 'gta', 'gtfo']
print(games)
games.append('deepRock')
print(games)
games.remove('ghostrecon')
print(games)
games.sort()
print(games)
games.reverse()
print(games)
"""

games = ["halo", "minecraft", "elden ring", "doom", "cyberpunk"]
print(games.index('elden ring'))
print(games.sort(key=len))
print(games.pop())



G=[]
print('Game Manager')
print("ADD\nDELETE\nSORT\nDISPLAY")
m=input(':')
if m== 'ADD':
 while(True):
    
    x=input('what game do u want to add:')
    if x == 'exit':
         print('Goodbye')
         break
    else:
     G.append(x)
elif m== 'DELETE' :
   while(True):
    
    x=input('what game do u want to delete:')
    if x == 'exit':
         print('Goodbye')
         break
    else:
     if x in G:
      G.remove(x)
     else:
        print('game already removed')
elif m == 'SORT':
   sort=G.sort(key=len)
   print(sort)

elif m== 'exit':
    print('Bye')

   
        