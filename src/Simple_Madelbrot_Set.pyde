w, cx, cy = 4., 0., 0.    # parameters

size(480, 480)
background(255)

h = w * height / width
x0 = cx - w / 2
y0 = cy - h / 2

for x in range(width):
    for y in range(height):
        c = complex(w*x/width+x0, h*y/height+y0)
        z = 0
        for i in range(1024):
            z = z**2 + c
            if abs(z) > 2:
                stroke(4*i)
                point(x, y)
                break

'''
【補足】
Mandelbrot集合とは：漸化式 z_(n+1) = (z_n)^2 + c で定義される複素数列z_nが発散しない複素数cの集合．
w, hはcの実部, 虚部の表示区間の大きさ．
ここではwをパラメータとし，hを w:h = width:height となるよう決定している．
cx, cyはそれぞれ画面中央のcの実部, 虚部．
x0, y0はそれぞれ画面左上のcの実部, 虚部．
デフォルトのパラメータでは，左上が-2+2i, 中央が0, 右下が2-2iとなる複素平面を解像度480x480で表示する．
メモリ効率もうちょい良くならんかな...
'''
