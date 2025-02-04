import cv2
import numpy as np
import pyautogui
import time
import random


def find_and_click_button(template_path, capture_region=(121, 323, 490, 95), match_threshold=0.75):
    """
    지정된 이미지 경로에 해당하는 버튼을 화면에서 찾아 클릭하는 함수.

    :param template_path: 템플릿 이미지의 경로
    :param capture_region: 화면에서 캡처할 영역 (x, y, width, height)
    :param match_threshold: 매칭 강도 기준 (0 ~ 1, 기본값 0.8)
    """
    # 템플릿 이미지 로드
    template = cv2.imread(template_path)  # 템플릿 이미지 (버튼 이미지)
    if template is None:
        print(f"Error: 템플릿 이미지 '{template_path}'을(를) 로드할 수 없습니다.")
        return

    template_w, template_h = template.shape[1], template.shape[0]

    while True:
        # 1. 스크린샷 캡처
        screenshot = pyautogui.screenshot(region=capture_region)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # PIL에서 OpenCV 형식으로 변환

        # 2. 템플릿 매칭
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(f"({template_path})매칭 강도: {max_val}, 위치: {max_loc}")

        # 3. 매칭 확인
        if max_val >= match_threshold:
            match_x, match_y = max_loc
            real_x = match_x + capture_region[0] + template_w // 2
            real_y = match_y + capture_region[1] + template_h // 2

            # 랜덤한 오차 추가 (±5 픽셀)
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            random_x = real_x + offset_x
            random_y = real_y + offset_y

            print(f"✔ 클릭 좌표: ({random_x}, {random_y}), 매칭 강도: {max_val}")

            # 두 번 클릭 (랜덤 좌표 사용)
            pyautogui.click(x=random_x, y=random_y)  # 첫 번째 클릭
            time.sleep(0.2)  # 0.2초 대기
            pyautogui.click(x=random_x, y=random_y)  # 두 번째 클릭

            break  # 버튼을 클릭한 후 반복 종료

        # 4. 이미지 화면에 출력
        cv2.imshow("Captured Screenshot with Region", screenshot)

        # 종료 조건 (ESC 키 누르면 종료)
        if cv2.waitKey(1) & 0xFF == 27:
            break

        if template_path == './1.png':
            time.sleep(3)
        else:
            time.sleep(0.1)

    cv2.destroyAllWindows()


# 함수 호출 예시
while True:
    find_and_click_button("./game_start_ep5.png")
    find_and_click_button("./game_start_ep5.png")
    find_and_click_button("./1.png")
    find_and_click_button("./2.png")
    find_and_click_button("./3.png")

    # 종료 조건 (ESC 키 누르면 종료)
    if cv2.waitKey(1) & 0xFF == 27:
        break
