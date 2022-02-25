from tkinter import *
import random
import keyboard

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width) - ((screen_width)/2))
y_cordinate = 0
cWidth = 500
cHeight = 400
square = 50
monsters_limit = 5
monsters = []
root.geometry("{}x{}+{}+{}".format(int(screen_width/2), int(screen_height), x_cordinate, y_cordinate))

w = Canvas(root, width=cWidth, height=cHeight, highlightthickness=1, highlightbackground="black")
# (rightLeft_start, topBottom_start, width, height)
#w.create_rectangle(0, 0, 50, 50, fill="red", outline = 'yellow')




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
            w.create_rectangle(dim['x'],
                               col_data[index]['x'],
                               dim['y'],
                               col_data[index]['y'],
                               fill=squre_color,
                               outline = 'yellow',
                               tags=("floor_square",)
                               )
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

#print(createRowAndColumn(5, 50))




#sw.create_rectangle(10, 50, 10, 200, fill="green", outline = 'blue')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')
#shapeW = (width / square)
#shapeH = (height / square)
#squaresCount = shapeW * shapeH
img = PhotoImage(file = "C:\\Users\\Mahmoud\\Desktop\\gamebg.png")


createMythra(cWidth, cHeight, square)
w.create_rectangle(0, 0, 50, 50, fill="blue", outline = 'yellow', tags=("champion",))
points = [150, 100, 200, 120]

w.pack()
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
root.mainloop()
