# V A R I A B L E S
names = []

# I M P O R T S
from os import system, name 
from time import sleep 


# F U N C T I O N S
# get user input
def amountPlayers():
    global ap
    ap = input("\n\t\tAmount of players: ")
    print("\n")
    return ap

def playerNames():
    for i in range(int(ap)):
        i += 1
        global names
        print(f"\t\tName {i}: ", end=' '),
        names.append(str(input()))
    return names

# settings menu
def settings():
    print("\t\tThis is the settings menu")

#throw the dices
def throw():
    print("ENTER to throw")
  
# clear function
def clear():  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

# scoreboard screen
def score():
    print(names)

# terminate the game
def quit():
    _ = system('^C') 

# throw function /w physical dices
def throwPhysical():
    print("\n\t\tTHROW NOW")
    sleep(4)
    
    global collectPoints = int(input('''
                    Enter amount of points

                    >  '''))

    return collectPoints

def pointsTurn(x):
    return 5*x

class person():

    amount_players = 0
    raise_scoring = collectPoints

    def scores(self, fname, scoring):
        self.fname = fname
        self.scoring = int(scoring)

    def scoreInfo(self):
        return '{} {}'.format(self.fname, self.scoring)

    def apply_points(self):
        self.scoring = int(self.scoring + self.raise_scoring)


