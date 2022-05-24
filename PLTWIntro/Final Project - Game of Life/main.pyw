import mechanics as mech
from graphics import GameOfLifeGUI
import time
import threading


#Global variables/configurations
debug = False
mech.GameOfLifeGridScan.debug = False

#Create game and GUI objects with starting configurations
game = mech.GameOfLifeGridScan(sizeX = 60, sizeY = 20, startConfig=[[17,2],[18,2],[19,2],[18,0],[19,1],[30,16],[31,16],[29,16]])
GUI = GameOfLifeGUI()


def toggleCellClickEvent(x,y):
    game.toggleCells([[x+30,-1*y+9]])


#Main function only runs if this is the main script
def main():
    #Intialize start stop behavior
    gameTimer = time.time()
    GUI.speedEntry.set(8)
    if(GUI.speedEntry.get() != '' and GUI.speedEntry.get().isnumeric()): gameFrequency = 1/float(GUI.speedEntry.get())
    GUI.popLabel.set(f'Current cell population: {game.getPop()}')
    GUI.genLabel.set(f'Current generation: {game.getGen()}')
    game.enabled = False
    GUI.playPause.configure(command=game.toggleEnabled)
    GUI.bindClickEvent(toggleCellClickEvent)
    frameCount = 0
    timer = time.time()

    #Main loop
    while True:
        #Graphics event runs at unrestrained speeds
        GUI.drawAll([[square[0]-30,square[1]-10] for square in game.getLiveCells()])
        GUI.update()
        frameCount += 1
        if frameCount == 20:
            GUI.fpsLabel.configure(text=f'FPS: {frameCount/(time.time()-timer):.0f}')
            frameCount = 0
            timer = time.time()

        #Game update timing 8hz
        if gameTimer + gameFrequency < time.time():
            #Run an iteration
            game.iterate()
            GUI.popLabel.set(f'Current cell population: {game.getPop()}')
            GUI.genLabel.set(f'Current generation: {game.getGen()}')
            gameTimer = time.time()
            if(GUI.speedEntry.get() != '' and GUI.speedEntry.get().isnumeric()): gameFrequency = 1/float(GUI.speedEntry.get())

if __name__ == "__main__":
    main()