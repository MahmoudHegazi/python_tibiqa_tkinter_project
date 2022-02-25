from tkinter import *
import random
import keyboard
import time
import threading

mainloop_started = threading.Event()
root = Tk()
mychamp = None

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width) - ((screen_width)/2))
y_cordinate = 0
cWidth = 500
cHeight = 400
square = 50
monsters_limit = 5
monsters = []
static_mythra = []
root.geometry("{}x{}+{}+{}".format(int(screen_width/2), int(screen_height), x_cordinate, y_cordinate))

w = Canvas(root, width=cWidth, height=cHeight, highlightthickness=1, highlightbackground="black")
# (rightLeft_start, topBottom_start, width, height)
#w.create_rectangle(0, 0, 50, 50, fill="red", outline = 'yellow')


character_actions = []

oldepoch = time.time()
def fun(event):
    print(event.keysym, event.keysym=='a')
    print(event)

def t():
    return oldepoch


def moveChamp(event):
    # this very important point in game and in later levels it define how speed of user in attack or in move later
    # can have delay for move that with boots and delay for attack q and w and e and r depend on training and level
    global oldepoch
    global mychamp
    game_speed_delay = time.time() - oldepoch >= 0.50
    if game_speed_delay:
        oldepoch = time.time()
    else:
        return False
    if event.keysym.lower() == 'right':
        w.delete(mychamp)
        print('moved right')
        character_actions.append("right")        
    elif event.keysym.lower() == 'left':
        print('moved left')
        character_actions.append("left")
    elif event.keysym.lower() == 'up':
        print('moved up')
        character_actions.append("up")
    elif event.keysym.lower() == 'down':
        print('moved up')
        character_actions.append("down")
    elif event.keysym.lower() == 'q':
        print('spell q')
        character_actions.append("q")
    elif event.keysym.lower() == 'w':
        print('spell w')
        character_actions.append("w")
    elif event.keysym.lower() == 'e':
        print('spell e')
        character_actions.append("e")
    elif event.keysym.lower() == 'r':
        print('spell r')
        character_actions.append("r")
    else:
        return False
    

def can_add_monster():
    addok = random.choice([True, False, False, False, False,True, False])
    return addok
def createMythra(width, height, square):
    shapeW = int(width / square)
    shapeH = int(height / square)
    rows = []
    columns = []
    row_data = createRowAndColumn(shapeW, square)
    col_data = createRowAndColumn(shapeH, square)
    index = 0
    
    for x in range(shapeH):
        for dim in row_data:
            squre_color = 'lightgreen'
            #if can_add_monster() and len(monsters) <= monsters_limit:
            #    monsters.append({'name': 'ghoul', 'index':len(monsters)+1})
            #    squre_color = 'brown'
            # here we create for now static map and append all squares
            map_sqaure = w.create_rectangle(dim['x'],
                               col_data[index]['x'],
                               dim['y'],
                               col_data[index]['y'],
                               fill=squre_color,
                               outline = 'yellow',
                               tags=("floor_square",)
                               )
            static_mythra.append(map_sqaure)
        index += 1
    print(monsters)




def createRowAndColumn(limit, sqaure):
    rowList = []
    advancedSqaure = sqaure
    lowSqaure = advancedSqaure - advancedSqaure
    for square in range(limit):
        rowList.append({'x': lowSqaure, 'y': advancedSqaure})
        advancedSqaure += sqaure
        lowSqaure += sqaure
    return rowList






img = PhotoImage(file = "C:\\Users\\Mahmoud\\Desktop\\gamebg.png")


createMythra(cWidth, cHeight, square)
mychamp = w.create_rectangle(0, 0, 50, 50, fill="blue", outline = 'yellow', tags=("champion",))

w.pack()
root.bind("<KeyRelease>", moveChamp)
root.mainloop()


#print(createRowAndColumn(5, 50))
#sw.create_rectangle(10, 50, 10, 200, fill="green", outline = 'blue')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')
#shapeW = (width / square)
#shapeH = (height / square)
#squaresCount = shapeW * shapeH

#from pynput.keyboard import Key, Listener

#def on_press(key):
#    print('{0} pressed'.format(
#        key))

#def on_release(key):
#    print('{0} release'.format(
#        key))
#    if key == Key.esc:
#        # Stop listener
#       return False

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
