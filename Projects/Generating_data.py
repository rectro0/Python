"""import matplotlib.pyplot as plt

squares = [1, 4, 9, 16 ]
plt.plot(squares, linewidth=5) 
plt.title("square numbers", fontsize=24)
plt.scatter(4,9)
plt.show()
##
"""
#dice class 
from random import randint
class Dice :

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
    


dice = Dice()
results = []
for roll_num in range(10):
    result = dice.roll()
    results.append(result)

print(results)