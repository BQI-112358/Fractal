size(480, 480)
background(255)

w, cx, cy = 4., 0., 0.    # customable; must be float

h = w * height / width
x0 = cx - w / 2
y0 = cy - h / 2

for x in range(width):
    for y in range(height):
        c = complex(w*x/width + x0, h*y/height + y0)
        z = 0
        for i in range(1024):
            z = z**2 + c
            if abs(z) > 2:
                stroke(4*i)
                point(x, y)
                break
            

'''
【補足】
漸化式 z_n+1 = z_n + c として
w, hはcの実部, 虚部の表示区間の大きさ
ここではhはwに対しheight/width比で決定している
cx, cyは画面中央のcの実部, 虚部
x0. y0は画面左上のcの実部, 虚部
'''
