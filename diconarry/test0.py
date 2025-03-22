Games = {
    "FPS": ["TitanFall2", "BioShock1","CallOfDuty"],
    "RPG":["TheWitcher3","MiddleEarth","FF7"],
    "HackandSash":["GodofWar","DarkSiders2","DMC5"]
}

"""""
Games["FPS"].append("GTFO")
print(Games)
Games["FPS"].remove("GTFO")
print(Games)
"""
for genre , games  in Games.items():
    print(f"the game genre is {genre.title()} , and the number of games in each genre {len(games)}")

    
        


    

       