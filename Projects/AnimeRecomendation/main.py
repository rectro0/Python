import requests 
import pandas as pd 


all_anime = []
pages = 1

while True:
  
 url = f"https://api.jikan.moe/v4/anime?page={pages}"

 response = requests.get(url)

 if (response.status_code == 200):
   data = response.json()
   anime_list = data["data"]
   print("Data fetched!") 
 

 
 
   if not anime_list :
    break
 

   for anime in anime_list :
    all_anime.append({
     "title" : anime["title"],
     "episodes" : anime["episodes"],
     "status" : anime ["status"],
      "rating": anime["rating"],
      "genres": [genre["name"] for genre in anime["genres"]],
     
    })

  
    print(f'page fetched {pages}') 
    pages += 1
 else :
   print(f"Data fetching failed {response.status_code}")
   break
df = pd.DataFrame(all_anime)
print(df.head())   