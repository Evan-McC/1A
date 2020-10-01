def combat(playerHP):

  enemy = 12

  punch = 2
  cut = 5
  kick = 3
  hit = 50

  while(True):

    print("Player HP", playerHP)
    print("Enemy HP", enemy)
    print('''What would you like to do
          a. punch
          b. cut
          c. kick
          d. hit
          ''')
    playerchoice = input()

    if playerchoice == "punch":
      enemy = enemy - punch
    if playerchoice == "cut":
      enemy = enemy - cut
    if playerchoice == "kick":
      enemy = enemy - kick
    if playerchoice == "hit":
      enemy = enemy - hit

    if(enemy <= 0):
      break
combat(20)   
