theta = 0

def setup():
    size(240, 240)
    stroke(0)
    
def draw():
    global theta
    background(255)
    
    # cardioidをパラメータthetaで表示
    c = complex(.5*(1-cos(theta))*cos(theta)+.25, .5*(1-cos(theta))*sin(theta))
    
    for x in range(width):
        for y in range(height):
            # 実部[-1.5, 1.5], 虚部[-1.5, 1.5]の区間を描画
            z = complex(3.*x/width-1.5, 3.*y/height-1.5)
            for i in range(256):
                z = z**2 + c
                if abs(z) > 2:    # 発散フラグ
                    point(x, y)
                    break
                
    print(millis(), theta%TWO_PI)    # 現在のフレームの描画時間と偏角
    theta += TWO_PI / 180    # 180フレームで偏角が一周する
    
    # 保存用：
    #if frameCount > 180:
    #    exit()
    #saveFrame('frames2/###.png')
    
    # 1フレームだけ描画したければ：
    #noLoop()
