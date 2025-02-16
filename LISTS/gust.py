dinner_guests = ['hitler', 'osauth' , ' filler', 'john'];
print(dinner_guests)

for x in dinner_guests:
    print( x, "You are invited to dinner")


print(dinner_guests[1], "could not make it")

dinner_guests[1] = 'semantha'
print(dinner_guests[1], "is coming instead")
print(dinner_guests)

for x in dinner_guests:
    print( x, "You are invited to dinner")


dinner_guests.insert(0,'bob');
dinner_guests.insert(3,"random");
dinner_guests.append('nquick');

print(dinner_guests);