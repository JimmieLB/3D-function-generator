import tkinter
import math
from tkinter import Canvas,Tk
canvas = tkinter.Canvas()
canvas.pack(side='top',fill='both', expand='yes')
import math
def abs(a):
    if(a<0):
        a*=-1
    return a
def map(a,amax,bmax):
    b =  bmax * (a/amax)
    if(b > bmax):
        b = bmax
    if(b < 0):
        b = 0
    return b
def toHex(a):
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    red = a[0]
    green = a[1]
    blue = a[2]
    red = hex_chars[math.floor(red/16)] + hex_chars[red%16]
    green = hex_chars[math.floor(green/16)] + hex_chars[green%16]
    blue = hex_chars[math.floor(blue/16)] + hex_chars[blue%16]
    return '#'+red+green+blue
class triangle:
    def __init__(self,point1,point2,point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

# class lightSource:
#     def __init__(self, xa, ya,xpz,ypz):
#         self.xangle = xa
#         self.yangle = ya
#         self.xpz = xpz
#         self.ypz = ypz
#     def shade(self,tri):
#         point1 = tri.point1
#         point2 = tri.point2
#         normalX = 1-(point2[0] - point1[0])
#         normalX = (self.X(point2)-self.X(point1))/normalX
#         normalY = 1-((400 - point2[1]) - (400 - point1[1]))
#         normalY = (self.Y(point2)-self.Y(point1))/normalY
#         diffX = normalX - self.xangle
#         diffY = normalY - self.yangle
#         gray = (diffX + diffY)/2
#         gray = gray * 255
#         gray = abs(gray)
#         gray = int(gray)
#         if(gray > 255): gray = 255
#         # return rgb(gray,gray,gray)
#     def X(self, point):
#         return int(point[0] + (point[2] * self.xpz))
#     def Y(self, point):
#         return int(400 - (point[1] + point[2] * self.ypz))

class renderer:
    def __init__(self):
        self.xpz = -.6 # X intervals per Z interval
        self.ypz = -.25 # Y intervals per Z interval
    def X(self, point):
        return int(point[0] + (point[2] * self.xpz))
    def Y(self, point):
        return int(400 - (point[1] + point[2] * self.ypz))
    def render(self, triangle):
        point1 = triangle.point1
        point2 = triangle.point2
        point3 = triangle.point3
        l1 = [self.X(point1),self.Y(point1),self.X(point2),self.Y(point2)]
        l2 = [self.X(point2),self.Y(point2),self.X(point3),self.Y(point3)]
        l3 = [self.X(point3),self.Y(point3),self.X(point1),self.Y(point1)]
        # line1 = Line(l1[0],l1[1],l1[2],l1[3])
        # line2 = Line(l2[0],l2[1],l2[2],l2[3])
        # line3 = Line(l3[0],l3[1],l3[2],l3[3])
        # filler = light.shade(triangle)
        filler = [int(map(self.Y(point1),400,255)),int(map(point1[0],100,150)),int(map(self.X(point1),1000,255))]
        filler = toHex(filler)
        stroke = "#1F1F1F"
        canvas.create_polygon(l1[0],l1[1],l1[2],l1[3],l2[0],l2[1],l2[2],l2[3],l3[0],l3[1],l3[2],l3[3],fill=filler,outline=stroke,width=.5)


render = renderer()

# def square(x,y,z,s):
#     x1 = x + s
#     y1 = y + s 
#     z1 = z + s
#     tri1 = triangle([x,y,z],[x,y1,z],[x1,y,z])
#     tri2 = triangle([x,y,z],[x,y1,z],[x1,y1,z])
#     render.render(tri1)
#     render.render(tri2)

def equation():
    xshift = 20
    yshift = 100
    def eq(x,z):
        try:
            # equat = x**2 + z**2
            # equat = 1.5 * (x**2 + z**2)*(math.sin(x)+math.sin(z))/(x*z)
            equat = 40 + 30 * math.sin(x/2) + 30 * math.sin(z/2)
            # equat = 10 * math.sqrt(400 - (x-10)**2 - (z-10)**2) #Sphere
            return equat + yshift
        except:
            return None
    x = 0
    scaler = 20
    yshift = 400 - yshift
    # canvas.create_line(xshift*scaler,yshift,400,yshift,fill="red")
    # canvas.create_line(0,yshift-(xshift*scaler-scaler*5.2)*render.xpz,xshift*scaler,yshift,fill = "green")
    # canvas.create_line(xshift*scaler,yshift,xshift*scaler,0,fill="blue")
    yshift = 400 - yshift
    count = 50
    while(x < count):
        z = 0
        while(z < count):
            z+=1
            if(eq(x,z) != None and eq(x-1,z) != None and eq(x,z-1) != None and eq(x-1,z-1) != None):
                point1 = [(x+xshift)*scaler,eq(x,z),z*scaler]
                point2 = [(x+xshift)*scaler-scaler,eq(x-1,z),z*scaler]
                point3 = [(x+xshift)*scaler, eq(x,z-1),z*scaler-scaler]
                point4 = [(x+xshift)*scaler-scaler, eq(x-1,z-1),z*scaler-scaler]
                render.render(triangle(point1,point2,point3))
                render.render(triangle(point2,point3,point4))
        x+=1
    
def cube(x,y,z,s):
    x1 = x + s
    y1 = y + s
    z1 = z + s
    back1 = triangle([x,y,z],[x,y1,z],[x1,y1,z])
    back2 = triangle([x,y,z],[x1,y,z],[x1,y1,z])
    
    left1 = triangle([x,y,z],[x,y1,z],[x,y,z1])
    left2 = triangle([x,y1,z],[x,y,z1],[x,y1,z1])
    
    right1 = triangle([x1,y,z],[x1,y1,z1],[x1,y,z1])
    right2 = triangle([x1,y1,z1],[x1,y1,z],[x1,y,z])
    
    top1 = triangle([x1,y1,z1],[x,y1,z],[x1,y1,z])
    top2 = triangle([x1,y1,z1],[x,y1,z],[x,y1,z1])
    
    bottom1 = triangle([x1,y,z],[x,y,z1],[x,y,z])
    bottom2 = triangle([x,y,z1],[x1,y,z],[x,y,z])
    
    front1 = triangle([x,y,z1],[x1,y,z1],[x,y1,z1])
    front2 = triangle([x1,y1,z1],[x1,y,z1],[x,y1,z1])
    
    render.render(back1)
    render.render(back2)
    render.render(bottom1)
    render.render(bottom2)
    render.render(left1)
    render.render(left2)
    render.render(right1)
    render.render(right2)
    render.render(top1)
    render.render(top2)
    render.render(front1)
    render.render(front2)

equation()
canvas.mainloop()