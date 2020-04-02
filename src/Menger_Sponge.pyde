direction = [(i, j, k) for i in -1, 0, 1 for j in -1, 0, 1 for k in -1, 0, 1 if i*j+j*k+k*i]
def draw_ms(depth, x, y, z, d):
    if not depth:
        stroke(abs(x)/2, abs(y)/2, abs(z)/2)
        point(x, y, z)
        return
    for i, j, k in direction:
        draw_ms(depth-1, x+d*i, y+d*j, z+d*k, d/3)
    
size(960, 960, P3D)
camera(1024, 1024, 1024, 0, 0, 0, -1, 0, 0)
draw_ms(5, 0, 0, 0, 256)
noLoop()
