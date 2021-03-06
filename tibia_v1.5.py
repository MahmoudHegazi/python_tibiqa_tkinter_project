import tkinter
from tkinter import *
import random
import keyboard
import time
import threading
import socket

mainloop_started = threading.Event()
root = Tk()
mychamp = None

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
x_cordinate = int((screen_width) - ((screen_width)/2))

root.geometry(str(screen_width) + "x" + str(screen_height))
def print_width():
   print("The width of Tkinter window:", root.winfo_width())
   print("The height of Tkinter window:", root.winfo_height())



y_cordinate = 0
cWidth = 500
cHeight = 400
square = 50
ts = 50
champ_size = 50
monsters_limit = 5
monsters = []
static_mythra = []

cx = screen_width - 1026
#root.geometry("{}x{}+{}+{}".format(screen_width, screen_height, 0, 0))

w = Canvas(root, width=cWidth, height=cHeight, highlightthickness=1, highlightbackground="black")
# (rightLeft_start, topBottom_start, width, height)
#w.create_rectangle(0, 0, 50, 50, fill="red", outline = 'yellow')




character_actions = []

oldepoch = time.time()
def fun(event):
    print(event.keysym, event.keysym=='a')
    print(event)


champ_position = {'x': 0,'y':0}
champ_compas = {'right': True, 'left': False, 'up': False, 'down': True}
const_last_right = cWidth - champ_size
const_lastt_down = cHeight - champ_size

mythra_squares = []

#champ_position['y']

s = None
def startSocket():   
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def updateCompasX(x, obj_size):
    global champ_compas
    # height of area mythra for now it city but now it small
    global cHeight

    last_right = cWidth - champ_size
    
    checkright = x + obj_size
    if checkright <= last_right:
        print("can have monster or attack from DOWN side >")
        champ_compas['right'] = True
    else:
        champ_compas['right'] = False
    # 2 d mean always update the deminsins together (right and left ) (up and down) spertly and happy result
    checkleft = x - obj_size
    if checkleft >= 0:
        # up to
        print("can have monster or attack from LEFT side <")
        champ_compas['left'] = True
    else:
        champ_compas['left'] = False
        
def updateCompasY(y, obj_size):
    global champ_compas
    # height of area mythra for now it city but now it small
    global cHeight

    last_down = cHeight - obj_size
    
    checkdown = y + obj_size
    if checkdown <= last_down:
        print("can have monster or attack from DOWN side V")
        champ_compas['down'] = True
    else:
        champ_compas['down'] = False
    # 2 d mean always update the deminsins together (right and left ) (up and down) spertly and happy result
    checkup = y - obj_size
    if checkup >= 0:
        # up to
        print("can have monster or attack from DOWN side ^")
        champ_compas['up'] = True
    else:
        champ_compas['up'] = False

def updatecompas(x,y,obj_size):
    updateCompasX(x, obj_size)
    updateCompasY(y, obj_size)
    return True

###### w.delete(mychamp) #####                   
# new move technique 2db here with tkinter can used for create any map with character and can move  him conintue db level2 socket level3

def moveRight():
    global champ_size
    global champ_position
    champ_position['x'] += champ_size
    w.moveto(mychamp,champ_position['x'],champ_position['y'])
    print('>Right Dim (X): ' , champ_position['x'])
    ## check posible right squares note here we did check after new position of hero so it <= last_right_sqaure (note any last right)
    # update compass right
    updatecompas(champ_position['x'],champ_position['y'],champ_size)

def moveDown():
    global champ_size
    global champ_position
    champ_position['y'] += champ_size
    w.moveto(mychamp, champ_position['x'], champ_position['y'])
    print('^Down Dim (Y): ' , champ_position['y'])
    # here heart of new technhuqe which depend on every thing later compas
    updatecompas(champ_position['x'],champ_position['y'],champ_size)

def moveLeft():
    champ_position['x'] -= champ_size 
    w.moveto(mychamp, champ_position['x'], champ_position['y'])
    print('<left Dim (X): ' , champ_position['x'])
    # save character action also it can used for game bots repeater and action recoreder
    # update compass left
    updatecompas(champ_position['x'],champ_position['y'],champ_size)


def moveUp():
    champ_position['y'] -= champ_size
    w.moveto(mychamp, champ_position['x'], champ_position['y'])
    print('^UP Dim (Y): ' , champ_position['y'])
    # update comppas up
    updatecompas(champ_position['x'],champ_position['y'],champ_size)
    
def moveChamp(event):
    # this very important point in game and in later levels it define how speed of user in attack or in move later
    # can have delay for move that with boots and delay for attack q and w and e and r depend on training and level
    global oldepoch
    global mychamp
    global current_right
    global square
    global champ_size
    global current_left
    global champ_position
    global champ_compas
    global const_last_right #champ last right vice verca will be with 0
    global const_lastt_down #champ last down vice verca will be 0
    global cWidth
    global cHeight
    # print(mychamp)
    
    game_speed_delay = time.time() - oldepoch >= 0.10
    if game_speed_delay:
        oldepoch = time.time()
    else:
        return False

    ###### Champ Controllers movments and compass update for action #####       
    if event.keysym.lower() == 'right':
         
        if champ_position['x'] < (const_last_right):
            moveRight()           
            character_actions.append("right")
            
    elif event.keysym.lower() == 'left':
        if champ_position['x'] > 0:
            moveLeft()
            character_actions.append("left")
            
    elif event.keysym.lower() == 'up':
        if champ_position['y'] > 0:
            moveUp()               
            character_actions.append("up")
            
    elif event.keysym.lower() == 'down':
        
        if champ_position['y'] < const_lastt_down:
            moveDown()
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

    print(champ_compas)




def can_add_monster():
    addok = random.choice([True, False, False, False, False,True, False])
    return addok
def createMythra(width, height, square):
    global ts
    shapeW = int(width / square)
    shapeH = int(height / square)
    rows = []
    columns = []
    row_data = createRowAndColumn(shapeW, square)
    col_data = createRowAndColumn(shapeH, square)
      

    datarow = createRow(shapeW, square)
    col_index = 1

    print("here", shapeH)

    # here loop for height so it start at first row then every time in loop down and draw new raw
    for col in range(shapeH):
        # here we create screen row and will used in camera moved (note this squares will come from db later)
        for row in datarow:
            drawFloorObject(square, row['x'], int(row['y']) + (int(col_index * square) - square), 'green','lightgreen',"floor_square", 'floor')
        col_index += 1

    print("We Have : ",len(static_mythra)," Map Squares ")


def drawFloorObject(tsquare, x,y, color, border, name="floor_square", obj_type='floor'):
    squre_color = color
    map_sqaure = w.create_rectangle(x,
                                    y,
                                    x+tsquare,
                                    y+tsquare,
                                    fill=color,
                                    outline = border,
                                    tags=(name,obj_type)
                                    )
    static_mythra.append(map_sqaure)



def createRowAndColumn(limit, sqaure):
    rowList = []
    advancedSqaure = sqaure
    lowSqaure = advancedSqaure - advancedSqaure
    for square in range(limit):
        rowList.append({'x': lowSqaure, 'y': advancedSqaure})
        advancedSqaure += sqaure
        lowSqaure += sqaure
    return rowList

def createRow(limit, sqaure):
    rowList = []
    advancedSqaure = 0
    lowSqaure = sqaure
    for square in range(limit):
        rowList.append({'x': advancedSqaure, 'y': 0})
        advancedSqaure += sqaure
    return rowList







img = PhotoImage(file = "C:\\Users\\Mahmoud\\Desktop\\gamebg.png")


s = startSocket()
print(s)
createMythra(cWidth, cHeight, square)
mychamp = w.create_rectangle(0, 0, 50, 50, fill="blue", outline = 'yellow', tags=("champion",))





#buttonExample2 = tkinter.Button(root,
#                           text="Button 1",
#                           width=5,
#                           height=5)

#buttonExample1.grid(column=0, row=0)
#buttonExample2.pack(side=TOP, anchor=NE)

#buttonExample3.pack(side=TOP,padx=0, pady=0)

print(vars(w))

w.config(bg='red')
w.pack(side = LEFT, anchor=W, fill='both', expand=True)
bottomframe = Frame(root, background="bisque")


#bottomframe.place(x=600, y=0, anchor="nw", width=385, height=460)



redbutton = Button(bottomframe, text="Red", fg="red", width=8)
redbutton.pack( side = LEFT)

greenbutton = Button(bottomframe, text="Brown", fg="brown", width=8)
greenbutton.pack( side = LEFT )

bluebutton = Button(bottomframe, text="Blue", fg="blue", width=8)
bluebutton.pack( side = LEFT )

bottomframe.pack( fill="y", side=tkinter.TOP, anchor=NE, expand=True)

#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)fukhismother


#Button(root, text="Click0", command=print_width).pack(padx=0,pady=0,fill='x', height=50, width=50)
#Button(root, text="Click1", command=print_width).pack(padx=15,pady=5)

#playbutton = w.create_rectangle(screen_width /2  - 150, 75, screen_width, 75, fill="red",tags="playbutton")
#playtext = w.create_text(110, 50, text="Play", font=("Papyrus", 12), fill='blue',tags="playbutton")
#setting_b = Button(root, text="Click", command=print_width)
#setting_b.pack(padx=15,pady=5)

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
# notes map is cloection of mythra togther in directions for example thais on right everything depend on champ compas  as noob will make mythra just 1 canvas size right will enter thais better than nothing
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
