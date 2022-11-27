x = 5
u = 180
z = 340
v = 240
def setup():
    size(600,600)
def draw():
    global x,u,z,v
    push()
    fill(218, 165, 32)
    triangle(200,180,270,u,v,u)
    triangle(300,180,370,u,z,u)
    pop()
    push()
    fill(139, 0, 0)
    triangle(300,250,270,350,330,350)
    pop()
    line(270,180,270,210)
    line(330,180,330,210)
    line(270,230,330,230)
    ellipse(300,200,100,100)
    x += 5
    u +=5
