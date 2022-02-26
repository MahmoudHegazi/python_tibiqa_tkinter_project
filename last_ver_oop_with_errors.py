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

#root.geometry(str(screen_width) + "x" + str(screen_height))
def print_width():
   print("The width of Tkinter window:", root.winfo_width())
   print("The height of Tkinter window:", root.winfo_height())




y_cordinate = 0
cWidth = (root.winfo_screenwidth() * 2) - 200
cHeight = 1000
square = 50
ts = 50
champ_size = 50
monsters_limit = 5
monsters = []
static_mythra = []



cx = screen_width - 1026
root.geometry("{}x{}+{}+{}".format(screen_width, screen_height, 0, 0))

w = Canvas(root, width=800, height=cHeight, highlightthickness=1, highlightbackground="black")


mythra = None


character_actions = []

oldepoch = time.time()
def fun(event):
    print(event.keysym, event.keysym=='a')
    print(event)



champ_position = {'x': 0,'y':0}
champ_compas = {'right': True, 'left': False, 'up': False, 'down': True}
const_last_right = cWidth - champ_size
const_lastt_down = cHeight - champ_size

# helper function
def conditionalArray(t=20, f=1):
    cond_array = []
    findex = 0
    for i in range(t):
        if findex < f and random.choice([True, False]):
            cond_array.append(False)
            findex += 1
        cond_array.append(True)
    return cond_array


class Camera:
    global cnv
    global champ_pos
    global champ_size
    global champ_compass    
    global cameraXR
    def __init__(self,w,champ_compass,champ_pos,champ_size):
        self.cnv=w
        self.champ_size = champ_size
        self.champ_pos = champ_pos
        self.champ_compass = champ_compass
        self.cameraXR = 0
    def track(self,champ_pos):
        print(champ_pos)
    def canCameraRight(self, updatedCompas):
        return updatedCompas['right'] == True
    def move_cameraR(self,compass):
        self.cameraXR += self.champ_size
        w.configure(xscrollincrement=1)
        w.xview_scroll(50, "units")


class Maper:
    global city_id
    global city_title
    global city_obj
    global square
    global city_height
    global city_width
    global mythra
    global static_mythra
    def __init__(self, square, city_id=1, city_title='Mythra', city_obj=[], city_height=2000, city_width=4000):
        self.city_id=city_id
        self.city_title = city_title
        self.static_mythra = city_obj
        self.city_height = city_height
        self.city_width = city_width
        self.square = square

    def createRow(self, limit, sqaure):
        rowList = []
        advancedSqaure = 0
        lowSqaure = sqaure
        for square in range(limit):
            rowList.append({'x': advancedSqaure, 'y': 0})
            advancedSqaure += sqaure
        return rowList        
        
    def drawFloorObject(self, tsquare, x,y, color, border, name="floor_square", obj_type='floor'):
        squre_color = color
        return w.create_rectangle(x,y, x+tsquare, y+tsquare, fill=color, outline = border, tags=(name,obj_type))
            
    def createCity(self, width, height, square):
        shapeW = int(self.city_width / self.square)
        shapeH = int(self.city_height / self.square)
        rows = []
        columns = []
        datarow = self.createRow(shapeW, square)
        col_index = 1
        # here loop for height so it start at first row then every time in loop down and draw new raw
        for col in range(shapeH):
            # here we create screen row and will used in camera moved (note this squares will come from db later)
            #selected_color = random.choice(['lightgreen','brown','green','gray'])
            for row in datarow:
                selected_color = 'green'
                # more incrase first more True , and vice versa with False and second
                tree1 = random.choice(conditionalArray(20, 20))
                tree2 = random.choice(conditionalArray(50, 20))
                tree3 = random.choice(conditionalArray(122, 20))
                tree4 = random.choice(conditionalArray(20, 20))
                tree5 = random.choice(conditionalArray(20, 5000))
                tree = tree1 and tree2 and tree3 and not tree4 and not tree5
                if conditionalArray(1, 5000) and tree:
                    selected_color = 'brown'
                map_sqaure = self.drawFloorObject(square, row['x'], int(row['y']) + (int(col_index * square) - square), selected_color,'lightgreen',"floor_square", 'floor')
                self.static_mythra.append(map_sqaure)
            col_index += 1            
        self.mythra = {'rows': rows,'columns':columns}
        print("We Have : ",len(self.static_mythra)," Map Squares ")
        return self.mythra

class Player:
    global hero
    global name
    global size
    global city
    global champ_position
    global champ_compas
    global current_city
    global character_actions
    
    def __init__(self, hero, name, size, city, current_city, champ_position, champ_compas):
        self.hero = hero
        self.name = name
        self.size = size
        self.city = city
        self.current_city = current_city
        self.champ_position = champ_position
        self.champ_compas = champ_compas
        self.square = square
        self.champ_size = champ_size
        self.character_actions = character_actions
        
    def moveRight(self):
        global app
        app.player.champ_position['x'] += app.player.size
        w.moveto(app.player,app.player.champ_position['x'],app.player.champ_position['y'])

        can_cam_mv_right = app.camera.canCameraRight(app.player.champ_compas)
        if can_cam_mv_right:
            app.camera.move_cameraR(app.player.champ_compas)
            print("moved cam yes")
        updatecompas(app.player.champ_position['x'],app.player.champ_position['y'],app.player.size)

    def moveDown(self):
        app.player.champ_position['y'] += app.player.size
        w.moveto(app.player, app.player.champ_position['x'], app.player.champ_position['y'])
        updatecompas(app.player.champ_position['x'],app.player.champ_position['y'],app.player.size)

    def moveLeft(self):
        app.player.champ_position['x'] -= app.player.size
        w.moveto(app.player, app.player.champ_position['x'], app.player.champ_position['y'])
        updatecompas(app.player.champ_position['x'],app.player.champ_position['y'],app.player.size)

    def moveUp(self):
        app.player.champ_position['y'] -= app.player.champ_size
        w.moveto(app.player, app.player.champ_position['x'], app.player.champ_position['y'])
        updatecompas(app.player.champ_position['x'],app.player.champ_position['y'],app.player.size)

    def moveChamp(self, event):
        # this very important point in game and in later levels it define how speed of user in attack or in move later
        # can have delay for move that with boots and delay for attack q and w and e and r depend on training and level
        global oldepoch
        global app

        game_speed_delay = time.time() - oldepoch >= 0.10
        if game_speed_delay:
            oldepoch = time.time()
        else:
            return False

        ###### Champ Controllers movments and compass update for action #####
        if event.keysym.lower() == 'right':
            if self.champ_position['x'] < (const_last_right):
                self.moveRight()
                self.character_actions.append("right")

        elif event.keysym.lower() == 'left':
            if self.champ_position['x'] > 0:
                self.moveLeft()
                self.character_actions.append("left")
                
        elif event.keysym.lower() == 'up':
            if self.champ_position['y'] > 0:
                self.moveUp()
                self.character_actions.append("up")
                
        elif event.keysym.lower() == 'down':
            if self.champ_position['y'] < const_lastt_down:
                self.moveDown()
                self.character_actions.append("down")
        elif event.keysym.lower() == 'q':
            print('spell q')
            self.character_actions.append("q")
        elif event.keysym.lower() == 'w':
            print('spell w')
            self.character_actions.append("w")
        elif event.keysym.lower() == 'e':
            print('spell e')
            self.character_actions.append("e")
        elif event.keysym.lower() == 'r':
            print('spell r')
            self.character_actions.append("r")
        else:
            return False        
        print(self.champ_compas)
        return self
    
class App:
    global mychamp
    global title
    global root
    global w
    global square    
    global champ_size
    global maper
    global camera
    global player
    global players
    global current_city
    
    def __init__(self, title, root, w, square, city_data=[], city_name='Mythra', current_city='Mythra'):
        self.title = title
        self.root = root
        self.w = w
        self.square = square
        self.current_city = current_city
        self.mychamp = []

        self.players = []
        self.maper = Maper(self.square, 1, city_name, city_data, 2000, 4000)
    def initalCityCanvas(self):
        # Draw layers 
        self.w.config(bg='blue')
        self.w.pack(side = LEFT, anchor=W, fill='both', expand=True)
        # Layer 1 Floor and Floor Objects
        return self.w

    def mapFloorLayers(self):
        # Draw layers 
        self.w.config(bg='blue')
        self.w.pack(side = LEFT, anchor=W, fill='both', expand=True)
        # Layer 1 Floor and Floor Objects
        self.mythra = self.maper.createCity(cWidth, cHeight, square)
        return self.mythra
    
    def addPlayerToMap(self, name, champ_size, city, current_city,champ_position, champ_compas):        
        mychamp = w.create_rectangle(0, 0, 50, 50, fill="blue", outline = 'yellow', tags=("champion",))
        self.player = Player(mychamp, name, champ_size, city, current_city,champ_position, champ_compas)
        self.players.append(mychamp)
        return self.player
        
    def run(self):       
        # this data and champ skilss status health , pk will loaded from db
        # Layer 3 app options buttons back etc not main

        global champ_position
        global champ_compas
        self.initalCityCanvas()
        self.mapFloorLayers()
        # load player data async
        current_plater = self.addPlayerToMap('GM:Python King', 50, 'Mythra', 'Mythra',champ_position, champ_compas)
        self.set_camera(current_plater)
        self.addRightAside()
        self.root.bind("<KeyRelease>", self.player.moveChamp)
        self.root.mainloop()
        
    def set_camera(self, player):
        self.camera = Camera(self.w, player.champ_compas, player.champ_position, player.size)
        return self.camera
        
    def addRightAside(self):
        bottomframe = Frame(self.root, background="bisque")
        redbutton = Button(bottomframe, text="Red", fg="red", width=8)
        redbutton.pack( side = LEFT)
        greenbutton = Button(bottomframe, text="Brown", fg="brown", width=8)
        greenbutton.pack( side = LEFT )
        bluebutton = Button(bottomframe, text="Blue", fg="blue", width=8)
        bluebutton.pack( side = LEFT )
        bottomframe.pack( fill="y", side=tkinter.TOP, anchor=NE, expand=True)
        return True



s = None
def startSocket():   
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def updateCompasX(x, obj_size):
    global app

    last_right = app.maper.city_width - app.square
    
    checkright = x + obj_size
    if checkright <= last_right:
        print("can have monster or attack from DOWN side >")
        app.player.champ_compas['right'] = True
    else:
        app.champ_compas['right'] = False
    # 2 d mean always update the deminsins together (right and left ) (up and down) spertly and happy result
    checkleft = x - obj_size
    if checkleft >= 0:
        # up to
        print("can have monster or attack from LEFT side <")
        app.player.champ_compas['left'] = True
    else:
        app.player.champ_compas['left'] = False
        
def updateCompasY(y, obj_size):
    global app
    # height of area mythra for now it city but now it small

    last_down = app.maper.city_height - obj_size
    
    checkdown = y + obj_size
    if checkdown <= last_down:
        print("can have monster or attack from DOWN side V")
        app.player.champ_compas['down'] = True
    else:
        app.player.champ_compas['down'] = False
    # 2 d mean always update the deminsins together (right and left ) (up and down) spertly and happy result
    checkup = y - obj_size
    if checkup >= 0:
        # up to
        print("can have monster or attack from DOWN side ^")
        app.player.champ_compas['up'] = True
    else:
        app.player.champ_compas['up'] = False

def updatecompas(x,y,obj_size):
    updateCompasX(x, obj_size)
    updateCompasY(y, obj_size)
    return True

###### w.delete(mychamp) #####                   
# new move technique 2db here with tkinter can used for create any map with character and can move  him conintue db level2 socket level3
       

def can_add_monster():
    #conditionalArray(5,40)
    addok = random.choice([True, False, False, False, False,True, False])
    return addok




def createRowAndColumn(limit, sqaure):
    rowList = []
    advancedSqaure = sqaure
    lowSqaure = advancedSqaure - advancedSqaure
    for square in range(limit):
        rowList.append({'x': lowSqaure, 'y': advancedSqaure})
        advancedSqaure += sqaure
        lowSqaure += sqaure
    return rowList




app = App('Mythra City', root, w, square, [], 'Mythra', 'Mythra')

if __name__ == '__main__':
    app.run()



# online socket start make cloud digital ocean and host server when logic join the socket
# img = PhotoImage(file = "C:\\Users\\Mahmoud\\Desktop\\gamebg.png")
# s = startSocket()
# print(s)
#print(root.winfo_width())
#print(mythra)

# Layer 0 Canvas



#buttonExample2 = tkinter.Button(root,
#                           text="Button 1",
#                           width=5,
#                           height=5)

#buttonExample1.grid(column=0, row=0)
#buttonExample2.pack(side=TOP, anchor=NE)

#buttonExample3.pack(side=TOP,padx=0, pady=0)

#print(vars(w))




#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)fukhismother


#Button(root, text="Click0", command=print_width).pack(padx=0,pady=0,fill='x', height=50, width=50)
#Button(root, text="Click1", command=print_width).pack(padx=15,pady=5)

#playbutton = w.create_rectangle(screen_width /2  - 150, 75, screen_width, 75, fill="red",tags="playbutton")
#playtext = w.create_text(110, 50, text="Play", font=("Papyrus", 12), fill='blue',tags="playbutton")
#setting_b = Button(root, text="Click", command=print_width)
#setting_b.pack(padx=15,pady=5)




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
