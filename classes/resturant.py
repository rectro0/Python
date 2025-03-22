class resturant():
   
 def __init__(self,resturant_name , cuisine_type):
  self.resturant_name = resturant_name
  self.cuisine_type = cuisine_type


 def describe(self):
   print(self.resturant_name , self.cuisine_type)
 def open(self):
   return print('it open ')   

 

rest = resturant('cooki','sea food')

print(rest.resturant_name)
print(rest.cuisine_type)

rest.describe()
rest.open()


 