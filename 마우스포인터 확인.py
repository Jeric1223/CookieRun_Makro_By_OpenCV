import pyautogui
import time

print("마우스 좌표를 확인하려면 커서를 움직이세요. 종료하려면 Ctrl + C를 누르세요.")
## 게임 시작 버튼 (513, 371)
## 게임 시작 2 (482, 363)

## 1. x : 121 323, 610 402 || 490, 80


try:
    while True:
        x, y = pyautogui.position()  # 현재 마우스 위치 가져오기
        print(f"마우스 위치: ({x}, {y})", end="\n")  # 한 줄에서 계속 업데이트
        time.sleep(0.1)  # 너무 빠르게 출력되지 않도록 딜레이 추가
except KeyboardInterrupt:
    print("\n프로그램 종료")
