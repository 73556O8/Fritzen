'''
Fritsen Drinking Game
73556O8
'''

# imports
import dice
from functions import *

import time
import sys
import random

# from tqdm import tqdm

# variables
mylist = [1,2,3,4,5,6,7,8]


# main menu
print('''
---------------------------------------------------

    HEEEEEUUUUUUJ LEKKER FRITSEN
    PAK JE DRANK EN GENIET VAN HET SPELLETJE

      ########        ##########
      **********     $$$$$$$$$$$
      ********  **  $$  $$$$$$$$
      ********  **  $$  $$$$$$$$
      ******** **    $$ $$$$$$$$ 
       *********      $$$$$$$$$

---------------------------------------------------\n
Python 3.6.9                        Dylan Wesselink
''')

# for i in tqdm(mylist):
#     time.sleep(1)

main = input('''
---------------------------------------------------
                M A I N     M E N U
---------------------------------------------------
                    (a) Start
                    (b) Settings
                    (c) Dices

                    > ''')

if main == "a":
    ap()
    playerNames()
    sips = int(input("\n\t\tAmount of points per sip: "))
elif main == "b":
    settings()
elif main != "a" or "b":
    print("\n\t\tDit klopt niet, doe a of b")
else:
    print("\n\t\tJeeeezus jij bent al dronken, ga slapen")
    sys.exit(1)

starter = random.choice(names)
print(f"\n\t\t{starter} starts!")

 