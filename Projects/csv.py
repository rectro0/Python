import json
import pygal

file = r'D:\visual_studio\Python\Learning\Projects\population_data.json'


with open(file ,'r') as file:
    pop_data = json.load(file)



    



for i in pop_data:
    if i['Year']== '2010' and i['Country Name']== 'Algeria':
        country = i['Country Name']
        year = i['Year']
        print(country +": " +str(year))

     
        

  