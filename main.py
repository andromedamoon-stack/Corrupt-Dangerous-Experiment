#Creator: Sarah W (Andromedamoon)

#inventory for items
inventory = ["flashlight","knife","bandage","pipe","sword"]


class Player(object):
  playerHealth = 65
  playerDefense = 18
  playerAttack = 4


# classes for boss fights
class Experiment(object):
  enemyHealth = 80
  enemyDefense = 20
  enemyAttack = 8
 

class Dr_Frankenstien(object):
  enemyHealth = 50
  enemyDefense = 12
  enemyAttack = 2
  

class Igor(object):
  enemyHealth = 50
  enemyDefense = 12
  enemyAttack = 3
 

def attack():
  global enemyHealth
  global enemyAttack
  global enemyDefense
  global playerAttack
  global playerDefense
  global playerHealth
  
  playHealth = playHealth - enemyAttack 
  enemyHealth = enemyHealth - playerAttack
  
  if playerHealth <= 0:
    loose()



def intro():
  print()
  print("Everything is dark")
  print()
  print("A flash of lightning briefly illuminates the room")
  print()
  print("You see a light switch on the wall just a few feet in front of you. You flip the switch")
  print()
  print("You hear a whirl of a generator starting as the light turn on")
  print()

  print("There is a  body  on an operating table in the middle of the room on a platform directly below the opening in the ceiling.")
  print()
  print('“I’m inside a laboratory?” ')
  print()

  print("The face has a few stitch marks on his face. Electrodes stick out from both sides of his neck.")
  print()

  print("You see a trapdoor behind the platform")
  print("......")
  print("Quickly, choose a path! The doctor will be here any moment!")
  print()
  print("Path One")
  print("""
▀█▀ █▀█ ▄▀█ █▀█ █▀▄ █▀█ █▀█ █▀█
░█░ █▀▄ █▀█ █▀▀ █▄▀ █▄█ █▄█ █▀▄""")
  print()
  print("Path two")
  print("""
█░█░█ ▄▀█ █ ▀█▀   ▄▀█ █▄░█ █▀▄   █░█ █ █▀▄ █▀▀
▀▄▀▄▀ █▀█ █ ░█░   █▀█ █░▀█ █▄▀   █▀█ █ █▄▀ ██▄""")

  print()
  firstPath = input("What path will you choose (1/2)  ")
  if firstPath == '1':
    print()
    path1()
  elif firstPath == '2':
    print()
    path2()


def path1():
  print("After going down the trap door you you seem to be inside a basement")
  print()
  print("The halls stretch on forever, layers of dust cover the walls and floor and you can see quite a few cobwebs.")
  print()
  print()
  print("To your right is a supply closet.")
  print("""
█▀▀ █░█ █▀▀ █▀▀ █▄▀   ▀█▀ █░█ █▀▀   █▀█ █▀▀ █▀▀ █ █▀▀ █▀▀   █▀▀ █▀█ █▀█   ▄▀█ █▄░█ █▄█
█▄▄ █▀█ ██▄ █▄▄ █░█   ░█░ █▀█ ██▄   █▄█ █▀░ █▀░ █ █▄▄ ██▄   █▀░ █▄█ █▀▄   █▀█ █░▀█ ░█░

█▀ █░█ █▀█ █▀█ █░░ █ █▀▀ █▀ ▀█
▄█ █▄█ █▀▀ █▀▀ █▄▄ █ ██▄ ▄█ ░▄""")
  supplyCloset = input("Y/N:  ")
  if supplyCloset == 'Y' or supplyCloset == 'y':
    print()
    path1supply()
  else:
    print()
    path1_pathCon()

def path1supply():
   print()
   print("You see a flashlight on one of the shelves.")
   print()
   pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
   if pickup == 'y' or pickup == 'Y':
    addToInventory("flashlight")
   else:
    print()
    print("You leave the flashlight on the shelf")
    path1_pathCon()

def path1_pathCon():
  print()
  print("After traversing down the basement hall for a few minutes you can see that the hallway splits off into two paths")
  print()
  
  print("You see a piece of pip on the ground near some rubble.")
  pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
  
  if pickup == 'y' or pickup == 'Y':
      addToInventory("pipe")
  else:
      print("You leave the pipe where it is.")

  print()
  print("on the left leads is another short hallway that leads to a red door. On the right there is stone steps that go down a level into a dark path. You can hear the sounds of running water coming from down below in the dark path")
  print("""
█░█░█ █░█ ▄▀█ ▀█▀   █▀█ ▄▀█ ▀█▀ █░█   █░█░█ █ █░░ █░░   █▄█ █▀█ █░█   ▀█▀ ▄▀█ █▄▀ █▀▀ ▀█
▀▄▀▄▀ █▀█ █▀█ ░█░   █▀▀ █▀█ ░█░ █▀█   ▀▄▀▄▀ █ █▄▄ █▄▄   ░█░ █▄█ █▄█   ░█░ █▀█ █░█ ██▄ ░▄""")
  path_redDark = input("Red/Dark")
  if path_redDark == 'Red' or path_redDark == 'red':
    print()
    path1_red()
  else:
    print()
    path1_flashlightCheck()

def path1_red():
  print()
   
def path1_flashlightCheck():
  print()
  print() 
  print("The path ahead looks  dark, you can’t continue on without a light source")
  print()
  look = input("Do you want to see if you have anything in your inventory that could help you? (Y/N)")
  if look == 'Y' or look == 'y':
    print_inventory()
  else:
    # if player does not have flashlight they cannot go down the stairs
    if "flashlight" not in inventory:
      print("You cannot go down there without a light source")
      print()
      print("While deciding what path to take you feel something hit you from behind. You black out")
      loose()
    else:
     print()
     path1_dark()

def path1_dark():
  print()

def path1_left():
  print()
  
def path1_right():
  print()

def path2():
 print()

  
def path2a():
 print()

def path2a_desk():
  print()

  def path2_boss():
  print()

def path2c_door():
  print()
  
def path2b():
  print()
  print("You wait....")
  print()
  print("............")
  print()
  print("............")
  print()
  print(" You eventually wait so long that you eventually fall asleep")
  loose()

  
def path3():
  print()

  
def path3_library():
  
def path3_foyer():
  
def path3_drBoss():
  

  
def win():
  print()

def win2():
  print()


def loose():
 print()
 print("..........")
 print("..........")
 print('"What happened?... Where am i?"')
 print()
 print()
 print("you are now the one strapped to the operating table in the laboratory.")
 print("you hear the sounds of people shuffling around you and the sounds of mad laughter.")


def playAgain():
  print(""""""
█▀▄ █▀█   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ ▀█
█▄▀ █▄█   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀█ █▄█ █▀█ █ █░▀█ ░▄""")
  answer = input("(Y/N):   ")
  if answer == 'Y' or answer == 'y':
        intro()
  else:
        print("""
█▀ █▀▀ █▀▀   █▄█ █▀█ █░█   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
▄█ ██▄ ██▄   ░█░ █▄█ █▄█   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")
        sys.exit()
      



        
# adds items to inventory

def addToInventory(item):
  inventory.append(item)

  
def print_inventory():
  for i in inventory:
    print(i)
    path1_flashlightCheck()



        
 ## main function ##

print()
print()
print()
print("""
░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝
██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░░██║██████╔╝░░░██║░░░
██║░░██╗██║░░██║██╔══██╗██╔══██╗██║░░░██║██╔═══╝░░░░██║░░░
╚█████╔╝╚█████╔╝██║░░██║██║░░██║╚██████╔╝██║░░░░░░░░██║░░░
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░░░░╚═╝░░░

██████╗░░█████╗░███╗░░██╗░██████╗░███████╗██████╗░░█████╗░██╗░░░██╗░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗██╔══██╗██║░░░██║██╔════╝
██║░░██║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝██║░░██║██║░░░██║╚█████╗░
██║░░██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗██║░░██║██║░░░██║░╚═══██╗
██████╔╝██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║╚█████╔╝╚██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░

███████╗██╗░░██╗██████╗░███████╗██████╗░██╗███╗░░░███╗███████╗███╗░░██╗████████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗██║████╗░████║██╔════╝████╗░██║╚══██╔══╝
█████╗░░░╚███╔╝░██████╔╝█████╗░░██████╔╝██║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░██╔══██╗██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
███████╗██╔╝╚██╗██║░░░░░███████╗██║░░██║██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░""")
print()
print()
startGame = input("Do you dare to enter? (Y/N): ")
if startGame == 'n' or startGame == 'N':
  print("""
█▀▄▀█ ▄▀█ █▄█ █▄▄ █▀▀   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
█░▀░█ █▀█ ░█░ █▄█ ██▄   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")

elif startGame == 'y' or startGame == "Y":
  intro()
