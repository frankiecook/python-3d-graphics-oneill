#############
# Main File #
#############
import math
from myMath import *
from myShapes import *
from myCanvas import *
from myTransformation import *
from myIlluminationModels import *
from myGeometry import *
from myRayTracing import *
from myVariables import *
from tkinter import *

# ************************ Initialize Shape Objects ********************* #
redSphere = sphere("Red Sphere")
redSphere.centerPoint = vector3(100,-90,-100)
redSphere.radius = 85
redSphere.localColor = [0.9,0.1,0.9]
redSphere.reflectWeight = 0
redSphere.refractWeight = 0
redSphere.localWeight = 0.5
objects.append(redSphere)

greenSphere = sphere("Green Sphere")
greenSphere.centerPoint = vector3(-100,-100,150)
greenSphere.radius = 75
greenSphere.localColor = [0.1,0.9,0.5]
greenSphere.reflectWeight = 0
greenSphere.refractWeight = 0.5
greenSphere.localWeight = 0.5
objects.append(greenSphere)

checkerBoard = plane("checkerboard")
checkerBoard.reflectWeight = 0.2
checkerBoard.refractWeight = 0
checkerBoard.localWeight = 0.9
objects.append(checkerBoard)
# ************** #

# ************************ Clutter of Random Functions ********************* #
# Z buffer creation
# zBuffer should not be on objects, it's for the entire scene
# to clean code, put in scene-type class
def createZBuffer(row, col):
    arr = []
    
    for r in range(row):
        tempArr = []
        for c in range(col):
            # fill with default
            tempArr.append(d)
        arr.append(tempArr)
    
    return arr
    
def drawObjects(objects):
    # define zBuffer for all objects to be drawn
    zBuffer = createZBuffer(CanvasHeight, CanvasWidth)

    # setting 7: Ray Tracing
    if (renderSetting == 7):
        renderImage(vector3(1,1,-1), c, CanvasHeight, CanvasWidth)

    print(len(objects))
    
rScale = 0.5
# **************************************************************************
# Everything below this point implements the interface
def reset():
    c.w.delete(ALL)
    curObject.reset()
    drawObjects(objects)

def larger():
    c.w.delete(ALL)
    scale(curObject,1.1)
    drawObjects(objects)

def smaller():
    c.w.delete(ALL)
    scale(curObject,.9)
    drawObjects(objects)

def forward():
    c.w.delete(ALL)
    translate(curObject,[0,0,-10])
    drawObjects(objects)

def backward():
    c.w.delete(ALL)
    translate(curObject,[0,0,10])
    drawObjects(objects)

def left():
    c.w.delete(ALL)
    translate(curObject,[-10,0,0])
    drawObjects(objects)

def right():
    c.w.delete(ALL)
    translate(curObject,[10,0,0])
    drawObjects(objects)

def up():
    c.w.delete(ALL)
    translate(curObject,[0,10,0])
    drawObjects(objects)

def down():
    c.w.delete(ALL)
    translate(curObject,[0,-10,0])
    drawObjects(objects)

def xPlus():
    c.w.delete(ALL)
    rotateX(curObject,rScale)
    curObject.update()
    drawObjects(objects)

def xMinus():
    c.w.delete(ALL)
    rotateX(curObject,-rScale)
    curObject.update()
    drawObjects(objects)

def yPlus():
    c.w.delete(ALL)
    rotateY(curObject,rScale)
    curObject.update()
    drawObjects(objects)

def yMinus():
    c.w.delete(ALL)
    rotateY(curObject,-rScale)
    curObject.update()
    drawObjects(objects)

def zPlus():
    c.w.delete(ALL)
    rotateZ(curObject,rScale)
    curObject.update()
    drawObjects(objects)

def zMinus():
    c.w.delete(ALL)
    rotateZ(curObject,-rScale)
    curObject.update()
    drawObjects(objects)

#################################
# left / right keyboard arrow selection
################################
def newSelection(value=1):
    global curObject
    
    index = objects.index(curObject)
    index += value
    
    objsLength = len(objects)

    if (index > objsLength-1):
        index -= (objsLength)
    elif (index < 0):
        index += (objsLength)

    updateCurObject(objects[index])

def updateCurObject(obj):
    global curObject
    # update selection color
    if (curObject != 0):
        curObject.selectColor = "black"
        curObject.selectWidth = 2
    obj.selectColor = "white"
    obj.selectWidth = 5
    curObject = obj
    
    global curPointCloud
    
    global curDefualtPointCloud
    curDefualtPointCloud = obj.defaultPointCloud

# temporary selection function for buttons
def newSelectionL():
    newSelection(-1)
    drawObjects(objects)
def newSelectionR():
    newSelection(1)
    drawObjects(objects)

# set current object
updateCurObject(objects[0])

root = Tk()
outerframe = Frame(root)
outerframe.pack()

# canvas creation is attached to a canvas object
# canvas object has access to draw functions
#w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
c = myCanvas("nice", CanvasWidth, CanvasHeight)
c.w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)

drawObjects(objects)
c.w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

downButton = Button(translatecontrols, text="DN", command=down)
downButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

selectioncontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
selectioncontrols.pack(side=LEFT)

selectioncontrolslabel = Label(selectioncontrols, text="Selection")
selectioncontrolslabel.pack()

leftSelect = Button(selectioncontrols, text="left", command=newSelectionL)
leftSelect.pack(side=LEFT)

rightSelect = Button(selectioncontrols, text="right", command=newSelectionR)
rightSelect.pack(side=LEFT)

root.mainloop()
