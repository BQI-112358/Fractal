level = 5    # たぶん5くらいが限界

def setup():
    fullScreen(P3D)
    noStroke()
    camera(486, 486, 486, 0, 0, 0, 0, -1, 0)
    
def draw():
    background(0)
    pointLight(255, 255, 255, 0, 0, 0)
    pointLight(255, 255, 255, 486, 0, 0)
    pointLight(255, 255, 255, -486, 0, 0)
    pointLight(255, 255, 255, 0, 486, 0)
    pointLight(255, 255, 255, 0, -486, 0)
    pointLight(255, 255, 255, 0, 0, 486)
    pointLight(255, 255, 255, 0, 0, -486)
    drawMS(level, 0, 0, 0, 486)
    print(millis())
    noLoop()

def drawMS(lv, x, y, z, l):
    if lv == 0:
        fill(256*(x+243)/486, 256*(y+243)/486, 256*(z+243)/486)
        translate(x, y, z)
        box(l, l, l)
        translate(-x, -y, -z)
        return
    
    l /= 3
    for i in -1, 0, 1:
        for j in -1, 0, 1:
            for k in -1, 0, 1:
                if abs(i)+abs(j)+abs(k) > 1:
                    drawMS(lv-1, x+l*i, y+l*j, z+l*k, l)
