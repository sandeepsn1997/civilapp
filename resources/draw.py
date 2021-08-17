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
    ox, oy = draw_rect(ox, oy, -10, 0, 250,150)

    #Sites Row1
    ox, oy = draw_rect(ox, oy, 30, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 55, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 80, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 105, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 155, 120, 25, 30)
    ox, oy = draw_rect(ox, oy, 180, 120, 25, 30)

    # Sites Row2
    ox, oy = draw_rect(ox, oy, 30, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 55, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 80, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 105, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 155, 75, 25, 30)
    ox, oy = draw_rect(ox, oy, 180, 75, 25, 30)

    # Sites Row3
    ox, oy = draw_rect(ox, oy, 30, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 55, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 80, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 105, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 155, 45, 25, 30)
    ox, oy = draw_rect(ox, oy, 180, 45, 25, 30)

    # Sites Row4
    ox, oy = draw_rect(ox, oy, 15, 0, 15, 30)
    ox, oy = draw_rect(ox, oy, 30, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 55, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 80, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 105, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 130, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 155, 0, 25, 30)
    ox, oy = draw_rect(ox, oy, 180, 0, 25, 30)

    return ox, oy

def draw_empty_space():
    ox, oy = [], []
    ox, oy = draw_sqr(ox, oy, -5, 130, 15)
    ox, oy = draw_sqr(ox, oy, -5, 85, 15)
    ox, oy = draw_sqr(ox, oy, -5, 65, 15)
    ox, oy = draw_sqr(ox, oy, -5, 45, 15)
    ox, oy = draw_sqr(ox, oy, -5, 25, 15)
    ox, oy = draw_sqr(ox, oy, -5, 5, 15)

    ox, oy = draw_sqr(ox, oy, 215, 125, 20)
    ox, oy = draw_sqr(ox, oy, 215, 95, 20)
    ox, oy = draw_sqr(ox, oy, 215, 65, 20)
    ox, oy = draw_sqr(ox, oy, 215, 35, 20)
    ox, oy = draw_sqr(ox, oy, 215, 5, 20)

    return ox, oy



plt.figure(figsize=(10, 8))
ox, oy = draw_layout()
plt.plot(ox, oy, "sk")

ox, oy = draw_empty_space()
plt.plot(ox, oy, "sg")
plt.axis("equal")
plt.grid(True)

plt.annotate("1",xy=(3,135))
plt.annotate("2",xy=(20,50))
plt.annotate("3",xy=(20,50))
plt.annotate("4",xy=(20,50))
plt.annotate("5",xy=(20,50))
plt.annotate("6",xy=(20,50))
plt.annotate("7",xy=(20,50))
plt.annotate("8",xy=(20,50))
plt.annotate("9",xy=(20,50))
plt.annotate("10",xy=(20,50))
plt.annotate("11",xy=(20,50))

plt.show()

#plt.axis('scaled')
#plt.axis("square")










