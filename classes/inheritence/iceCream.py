class resturant():
   
 def __init__(self,resturant_name , cuisine_type ):
  self.resturant_name = resturant_name
  self.cuisine_type = cuisine_type
  self.number_served = 48


 def describe(self):
   print(self.resturant_name , self.cuisine_type)
 def open(self):
   return print('it open ')   
 def set_number_served(self, n):
     self.number_served = n
     
 def print(self):
   print("the number of served costumer is :" + str(self.number_served))

 def increment(self, inc):
    self.number_served += inc
   
   

    
   

 

rest = resturant('cooki','sea food')

print(rest.resturant_name)
print(rest.cuisine_type)

rest.describe()
rest.open()


resturant = resturant('name', 'type')

print("\n"+str(resturant.number_served))
rest.set_number_served(2)
rest.increment(4)
rest.print()

class IceCreamStand(resturant):
  
  def __init__(self, resturant_name, cuisine_type):
    super().__init__(resturant_name, cuisine_type)
    self.flavors = ""