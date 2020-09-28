#Health
  #Health is 100 points, cant increase once lost health,
  #Bandages only stop bleeding damage, which you lose health over time
def health (HP):
  HP == 100
  print (HP)

def bleeddamage (bleed):
  bleed == (HP - 1)

#Loot
#Layed out common(80%) to rare(5%)
loot = ["Gold_Coin", "Bandage", "Torch", "Damaged_Shield", "Rusted_Dagger", "Invisibility_Potion"]

def Gold_Coin (points):
  Gold_Coin ==  1 point
  Gold_Coin == 80% Drop
  
def Bandage (heal):
  bleed == 0
  Bandage == 65% Drop

def Torch (light):
  burn dmg == 5
  light == 100%
    Loot Drop == 100%
    Slime == 150% Damage
    monsters == 100% Perception 
      Bat + Spider == 0% perception 
  Torch == 35% Drop

def Damaged_Shield (protect):
  Use == 25% Break
  protect == 100 DEF
  Damaged_Shield == 25% Drop

def Rusted_Dagger (attack):
  Use == 20% Break
  attack == 10 DMG
  if monster == 1 attack:
    monster == Stun
    Escape == 100%
  Rusted_Dagger == 15% Drop

def Invisibility_Potion (invisible):
  monsters == 0% Perception
  Invisibility_Potion == 5 Rooms
  Invisibility_Potion == 5% Drop

#Monster Encounters
#Layed out easiest(Common)(20%) to hard(rare)(1%)
monsters = ["Bat", "Giant Rat", "Slime", "Goblin", "Golem"]

def Bat (enemy_1):
  Bat_spawn == 20%
  Bat_perception == 80%
  Bat_attack == -5 HP
  Bat_HP == 5
  Escape == 85%

def Giant_Rat (enemy_2):
  Giant_Rat_spawn == 10%
  Giant_Rat_perception == 80%
  Giant_Rat_attack == -10 HP
  Giant_Rat_HP == 15
  Escape == 55%

def Slime (enemy_3):
  Slime_spawn == 7%
  Slime_perception == 20%
  Slime_attack == -5 HP
  Slime_HP == 10
  Escape == 60%

def Goblin (enemy_4):
  Goblin_spawn == 4%
  Goblin_perception == 80%
  Goblin_attack == -10 HP
  Goblin_HP == 20
  Drop_Loot == 75%
  Escape 40%

def Golem (enemy_5):
  Golem_spawn == 1%
  Golem_perception == 75%
  Golem_HP == 60
  #Goblins have a higher drop loot chance on everything
  #Golem ineffective to "Rusted Knife" and one hits the "Damaged Shield", Invis is effective against Golem

#Title Screen
print ("**********Text-Based Dungeon Crawler**********")
print ("")

while(True):
#Start
  qstart = ("Would you like to play a game")
  print(qstart)
  print("")
  astart = (input("Yes, or No >> "))

  if(astart == "Yes" or astart == "yes"):
    cont = True
  else:
    print("")
    print("You miss out on a grand adventure, what a shame.")
    break

  print("")
  print("We begin this story as a child, while you were playing in the  forest, you fell down into a hole, but whats worse is that you fell right into the center of an dungeon.")
  print("")
  print("You are not strong enough to fight the monsters, you must      escape quickly & quietly")
  print("")
  print("")
  print("")
  print("You wake up, you are surronded by darkness, the only light     comes from hole in the roof.")
  print("")

#tutorial on inpsect input
#Player finds corpse with 1 bandage, 1 torch, & 5 Coins
#Player given info on bandage and torch
#Player starts out with a choice of left or right 
  #Player can have 4 directions to travel in other situations
#Random chance of encounter of corpses(Collectibles)
#Smaller random chance for monster encounter
  #If player returns to a room previously explored, do not generate new room
