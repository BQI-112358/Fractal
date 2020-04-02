def draw_st(depth, x, y, z, d):
    if not depth:
        point(x, y, z)
        return
    draw_st(depth-1, x-d, y-d, z-d, d/2)
    draw_st(depth-1, x-d, y+d, z+d, d/2)
    draw_st(depth-1, x+d, y-d, z+d, d/2)
    draw_st(depth-1, x+d, y+d, z-d, d/2)
    
size(960, 960, P3D)
camera(1024, 1024, 1024, 0, 0, 0, 1, 0, 0)
draw_st(8, 0, 0, 0, 256)
noLoop()

'''
【補足】
正四面体は立方体の4頂点を結んで形成される．
したがって立方体の中心座標を基準に再帰を考えれば良い．
'''
