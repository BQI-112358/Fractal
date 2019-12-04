level = 5     # たぶん8くらいが限界

def setup():
    fullScreen(P3D)
    noStroke()

def draw():
    global d
    camera(256*cos(TWO_PI*mouseX/width), 256*sin(TWO_PI*mouseX/width), 256, 0, 0, 0, 0, 0, -1)
    background(0)
    draw_fractal(level, 0, 0, 0, 256)
    
def draw_fractal(lv, x, y, z, l):
    if not lv:
        fill(128-x, 128-y, 128-z)
        beginShape(TRIANGLE_STRIP)
        vertex(x-l/2, y-l/2, z-l/2)
        vertex(x+l/2, y-l/2, z+l/2)
        vertex(x-l/2, y+l/2, z+l/2)
        vertex(x+l/2, y+l/2, z-l/2)
        vertex(x-l/2, y-l/2, z-l/2)
        vertex(x+l/2, y-l/2, z+l/2)        
        endShape()
        return
    draw_fractal(lv-1, x-l/4, y-l/4, z-l/4, l/2)
    draw_fractal(lv-1, x-l/4, y+l/4, z+l/4, l/2)
    draw_fractal(lv-1, x+l/4, y-l/4, z+l/4, l/2)
    draw_fractal(lv-1, x+l/4, y+l/4, z-l/4, l/2)
    
def keyPressed():
    global level
    if keyCode == UP:
        level = min(level+1, 10)
    elif keyCode == DOWN:
        level = max(level-1, 0)
        
'''
【補足】
正四面体は立方体の4頂点を結んで形成される
したがって立方体の中心座標を基準に再帰を考えれば良い
'''
