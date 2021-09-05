

import matplotlib.pyplot as plt

def draw_line_x(ox, oy, x, y, length):
    for i in range(length+1):
        ox.append(x+i)
        oy.append(y)
    return ox, oy

def draw_line_y(ox, oy, x, y, length):
    for i in range(length+1):
        ox.append(x)
        oy.append(y+i)
    return ox, oy

def draw_sqr(ox, oy, x, y, length):
    draw_line_x(ox, oy, x, y, length)
    draw_line_x(ox, oy, x, y+length, length)
    draw_line_y(ox, oy, x, y, length)
    draw_line_y(ox, oy, x + length, y, length)
    return ox, oy

def draw_rect(ox, oy, x, y, length, breadth):
    draw_line_x(ox, oy, x, y, length)
    draw_line_x(ox, oy, x, y+breadth, length)
    draw_line_y(ox, oy, x, y, breadth)
    draw_line_y(ox, oy, x + length, y, breadth)

    return ox, oy


def draw_layout():
    ox, oy = [], []

    # Outter Box
    ox, oy = draw_rect(ox, oy, -60, 0, 470,300)

    #Sites Row1
    ox, oy = draw_rect(ox, oy, 40, 240,25, 30)
    ox, oy = draw_rect(ox, oy, 85, 240, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 240, 25, 30)


    ox, oy = draw_rect(ox, oy, 265, 240, 25, 30)
    ox, oy = draw_rect(ox, oy, 310, 240, 25, 30)
   # outer boundry for row1
    ox, oy = draw_rect(ox, oy, 30, 225, 45, 55)
    ox, oy = draw_rect(ox, oy, 75, 225, 45, 55)
    ox, oy = draw_rect(ox, oy, 120, 225, 45, 55)


    ox, oy = draw_rect(ox, oy, 255, 225, 45, 55)
    ox, oy = draw_rect(ox, oy, 300, 225, 45, 55)

    # Sites Row2
    ox, oy = draw_rect(ox, oy, 40, 150, 25, 30)
    ox, oy = draw_rect(ox, oy, 85, 150, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 150, 25, 30)


    ox, oy = draw_rect(ox, oy, 310, 150, 25, 30)
    ox, oy = draw_rect(ox, oy, 355, 150, 25, 30)
    # outer boundry for row2
    ox, oy = draw_rect(ox, oy, 30, 140, 45, 55)
    ox, oy = draw_rect(ox, oy, 75, 140, 45, 55)
    ox, oy = draw_rect(ox, oy, 120, 140, 45, 55)



    ox, oy = draw_rect(ox, oy, 300, 140, 45, 55)
    ox, oy = draw_rect(ox, oy, 345, 140, 45, 55)
    # Sites Row3
    ox, oy = draw_rect(ox, oy, 40,100, 25, 30)
    ox, oy = draw_rect(ox, oy, 85, 100, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 100, 25, 30)



    ox, oy = draw_rect(ox, oy, 310, 100, 25, 30)
    ox, oy = draw_rect(ox, oy,355 , 100, 25, 30)

    # outer boundry for row3

    ox, oy = draw_rect(ox, oy, 30, 85, 45, 55)
    ox, oy = draw_rect(ox, oy, 75, 85, 45, 55)
    ox, oy = draw_rect(ox, oy, 120, 85, 45, 55)



    ox, oy = draw_rect(ox, oy, 300, 85, 45, 55)
    ox, oy = draw_rect(ox, oy, 345, 85, 45, 55)
    # Sites Row4
    ox, oy = draw_rect(ox, oy, 40, 10,25, 30)
    ox, oy = draw_rect(ox, oy, 85, 10, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 10, 25, 30)
    ox, oy = draw_rect(ox, oy, 310, 10, 25, 30)
    ox, oy = draw_rect(ox, oy, 355, 10, 25, 30)

    # outer boundry for row4
    ox, oy = draw_rect(ox, oy, 30, 0, 45, 55)
    ox, oy = draw_rect(ox, oy, 75, 0, 45, 55)
    ox, oy = draw_rect(ox, oy, 120,0, 45, 55)



    ox, oy = draw_rect(ox, oy, 300, 0, 45, 55)
    ox, oy = draw_rect(ox, oy, 345, 0, 45, 55)

    return ox, oy

def draw_empty_space():
    ox, oy = [], []
    ox, oy = draw_sqr(ox, oy, -50, 265, 25)#1
    ox, oy = draw_rect(ox, oy, -50,65,25,135)#2
    ox, oy = draw_sqr(ox, oy,190,240,35)#4
    ox, oy = draw_sqr(ox, oy, 225, 150, 20)#6
    ox, oy = draw_rect(ox, oy, 190,150, 25,35)#5
    ox, oy = draw_rect(ox, oy, -50, 5,40,50 )

    ox, oy = draw_rect(ox, oy, 360, 240, 45,55)#7
    ox, oy = draw_rect(ox, oy, 190,90,30,45)#8
    ox, oy = draw_sqr(ox, oy, 240,5, 25)#10
    ox, oy = draw_rect(ox, oy,230,105,40,30)#9
    ox, oy = draw_sqr(ox, oy,190 , 5, 40)#11

    return ox, oy

plt.figure(figsize=(10, 8))
ox, oy = draw_layout()
plt.plot(ox, oy, "sk")


ox, oy = draw_empty_space()
plt.plot(ox, oy, "sg")
plt.axis("equal")
plt.grid(True)


plt.annotate("1",xy=(-40,275))
plt.annotate("2",xy=(-40,135))
plt.annotate("3",xy=(-35,30))
plt.annotate("4",xy=(205,255))
plt.annotate("5",xy=(195,165))
plt.annotate("6",xy=(230,155))
plt.annotate("7",xy=(375,265))
plt.annotate("8",xy=(200,112))
plt.annotate("9",xy=(245,115))
plt.annotate("10",xy=(245,15))
plt.annotate("11",xy=(200,25))
plt.xlabel('X-Coordinates')
plt.ylabel('Y-Coordinates')
plt.title('Construction Site Layout Plan',fontsize=15,color="red")
plt.figtext(0.905,0.8,"1=Security shed",fontsize=10,color="blue")
plt.figtext(0.905,0.77,"2=Parking",fontsize=10,color="blue")
plt.figtext(0.905,0.74,"3=Site office",fontsize=10,color="blue")
plt.figtext(0.905,0.71,"4=Canteen",fontsize=10,color="blue")
plt.figtext(0.905,0.68,"5=Labour Shed",fontsize=10,color="blue")
plt.figtext(0.905,0.65,"6=Toilet",fontsize=10,color="blue")
plt.figtext(0.905,0.62,"7=Ware House",fontsize=10,color="blue")
plt.figtext(0.905,0.59,"8=Power House",fontsize=10,color="blue")
plt.figtext(0.905,0.56,"9=Water tank",fontsize=10,color="blue")
plt.figtext(0.905,0.53,"10=Q/C Lab",fontsize=10,color="blue")
plt.figtext(0.905,0.50,"11=Batching Plant",fontsize=10,color="blue")


plt.show()

#plt.axis('scaled')
#plt.axis("square")





