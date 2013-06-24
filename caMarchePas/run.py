import sys
sys.path.append('./libs')

from Roulette import Roulette 
from PlayColours import PlayColours
     
myColours=PlayColours()

myColor=myColours.RED

roulette=Roulette()

roulette.choiseColor(myColours)
roulette.play(myColours)

