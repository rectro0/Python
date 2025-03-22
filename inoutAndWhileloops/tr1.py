#rental = input("what car would you like :");
#print(rental);

#####

#diner = input("how many people are in the list :")
#dinner = int(diner);
#if dinner <8 :
 #   print("table is ready ")
#else: print("you have to wait ")


#####
#list=[]
#state = True
#while state:
    #message = input("what r your  toppings :")
    #list.append(message)
   # if message == "quit":
  #      state = False 
 #   else:
#        print(message.title()+" has been added to your pizza")



######

#while True :
 #   age = input("how old are you :")

  #  if int(age) == 3 :
   #     print("your tiket is free")
    #    break
    #elif int(age) >=3 and int(age) <= 12 :
     #   print("your tiket is 12$")
      #  break
    #elif int(age) >=12 :
     #   print("your tiket is 15$")
      #  break        

#######

sandwich_orders = ["big mac", "cheese", "chiken tendies", "ham"]
finised_sandwichs=[]

for order in sandwich_orders:
    print("I made your "+ order.title())
    finised_sandwichs.append(order)

print(finised_sandwichs)


########
poll=[]
n=0
while n<6:
 user = input("If you could visit one place in the world, where would you go?");
 poll.append(user)
 n += 1

print(poll)
