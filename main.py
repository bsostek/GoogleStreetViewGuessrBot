from aiCode import getLocation
from gameWindow import startGame,getScreenshot,closeGame

# Start up the game
startGame()

# Take the screenshot
img= getScreenshot()
 
# Get the location of the screenshot
location=getLocation(img)

# Print the location
print(location)







