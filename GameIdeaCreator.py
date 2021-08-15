# witnn's simple game idea creator
import random as rd

env =[
    "Forest","Office","House","City","Cave","Roof","Military Base","Castle","Ocean","Lake","School"
]
goal =[
    "Escape","Kill them all","Take All","Solve Problem"
]
genre =[
    "Action","Strategy","Platformer","Shooter"
]
rules =[
    "Dont jump","Dont die","Dont Fall","Dont Run","Dont Attack"
]
wildcard =[
    "Whale","Shark","Fish","Nuclear","Computer","Plants","Axe","Doctor","Moments","Doors","Vaccine"
]

dict = [env,goal,genre,rules,wildcard]

def GenerateGameIdea():
    idea = "- "
    for i in range(5):
        idea += rd.choice(dict[i]) + " - "
    return idea

print(GenerateGameIdea())
