import keyboard
import pyautogui as pg
from PIL import ImageGrab # 화면 캡쳐

SB=1 # 종료키 기능을 위한 변수
shot=0 # 목표물 찾았는지 확인하는 변수
start=(261, 673) # 왼쪽 위 좌표
end=(1663, 1536) # 오른쪽 아래 좌표
spot=(109, 136, 170) # 목표물 색깔

while SB==1:
    screen = ImageGrab.grab() # 화면 캡쳐
    for i in range(start[0],end[0],13):
        for j in range(start[1],end[1],13): # 직사각형 모양으로 13px 단위로 추적
            rgb=screen.getpixel((i,j)) # 각 좌표에서의 rgb값 추출

            if abs(rgb[0]-spot[0])+abs(rgb[1]-spot[1])+abs(rgb[2]-spot[2])<80: #첫번째 검증
                rgb=screen.getpixel((i+3,j)) # (i+3,j)에서 rgb값 추출

                if abs(rgb[0]-spot[0])+abs(rgb[1]-spot[1])+abs(rgb[2]-spot[2])<80: #두번째 검증
                    pg.click((i+3,j))
                    shot=1
                    break

        if shot==1: # 목표물 찾으면 for문 빠져나옴
            shot=0
            break
        
    if keyboard.is_pressed('F3'): # 코드 종료
        SB=0
        break
