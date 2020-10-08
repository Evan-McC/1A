import random

enemy_hp = random.randint (5, 20)
HP = random.randint (5, 20)


def combat(HP,enemy_hp):
  
  while(True):
    
    print(HP, "HP")
    print(enemy_hp, "Enemy's HP")
    choice = input("attack or block >> ")
    attack = random.randint (5, 10)
    block = random.randint (4, 7)
    enemy_atk = random.randint (5, 10)

    if choice == "attack":
      print("you did", attack, "damage")
      enemy_hp = enemy_hp - attack
      HP = HP - enemy_atk
      print("the enemy hit you for", enemy_atk, "damage")

    if choice == "block":

      if enemy_atk <= block:
        print("the enemy hit you for", enemy_atk, "damage")
        enemy_atk = 0
        print("you succesfully blocked the attack")
      if enemy_atk >= block:
        HP = HP - enemy_atk
        print("the enemy hit you for", enemy_atk, "damage")
        print("you failed to block, you got hit")

    if HP <= 0:
      print("your HP is at", HP)
      print("the enemy's HP is", enemy_hp)
      print("You Lost The Fight")
      break

    if enemy_hp <= 0:
      print("the enemy's HP is", enemy_hp)
      print("your HP is at", HP)
      print("You Have Won the Fight")
      break

combat(HP,enemy_hp)
