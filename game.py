from tkinter import *
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width) - ((screen_width)/2))
y_cordinate = 0

root.geometry("{}x{}+{}+{}".format(int(screen_width/2), int(screen_height), x_cordinate, y_cordinate))

w = Canvas(root, width=250, height=200, highlightthickness=1, highlightbackground="black")
# (rightLeft_start, topBottom_start, width, height)
w.create_rectangle(0, 0, 50, 50, fill="red", outline = 'yellow')

def createRow(limit, sqaure):
    rowList = []
    advancedSqaure = sqaure
    lowSqaure = advancedSqaure - advancedSqaure
    for square in range(limit):
        rowList.append({'x': lowSqaure, 'y': advancedSqaure})
        advancedSqaure += sqaure
        lowSqaure += sqaure
    return rowList

print(createRow(5, 50))
    

def createMythra(width, height, square):
    shapeW = (width / square)
    shapeH = (height / square)
    squaresCount = shapeW * shapeH
    
    mythryaMap = []
    rightLeft_start = 0
    rightLeft_end = 0
    width = 0
    height = 0
    print("hi")
#sw.create_rectangle(10, 50, 10, 200, fill="green", outline = 'blue')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')
#w.create_rectangle(0, 0, 250, 200, fill="green", outline = 'lightgreen')

w.pack()
root.mainloop()
