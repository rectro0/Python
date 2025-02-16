favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):#sorted loop, printing keys
 print(name.title() + ", thank you for taking the poll.")

 ##nested loop
 # Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

# Show the first 5 aliens:
        for alien in aliens[:5]:
            print(alien)
            print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))