aFile=input("Input filename ex)recoords.txt: ")

def getCoordsFromFile(aFile):
    fileopen=open(aFile)
    coords=list()
    for line in fileopen:
        line1=line.split(',')
        coords.append([(line1[0],line1[1]), (line1[2],line1[3].strip())])
    fileopen.close()
    return coords
coords=getCoordsFromFile(aFile)

def drawSquareWithCoords(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
    print (x1,y1,x2,y2)
    t1.goto(x1,y1)
    for i in range(0,4):
        t1.fd(x1-x2)
        t1.rt(90)
drawSquareWithCoords(coords)
wn.exitonclick()