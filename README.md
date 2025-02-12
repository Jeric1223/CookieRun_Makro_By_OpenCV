---

# 쿠키런 버튼 클릭 자동화
이 Python 스크립트는 지정된 화면 영역에서 버튼을 찾아 클릭하는 자동화 작업을 수행합니다. OpenCV를 사용하여 이미지 처리를 하고, PyAutoGUI를 사용하여 마우스를 제어하고 클릭을 시뮬레이션하며, NumPy는 배열 처리를 담당합니다. 이 스크립트는 그래픽 인터페이스에서 버튼이나 요소와 상호작용하는 작업을 자동화하는 데 유용합니다.

## 전체 순서
1. 맥북 화면 미러링으로 쿠키런 시작 화면상태를 띄운다.
2. 화면 좌표 범위를 설정한다. ( 버튼 화면 범위 ) 
3. 파일을 실행시킨다. 

## 필수 패키지

스크립트를 실행하기 전에 필요한 Python 라이브러리가 설치되어 있는지 확인하세요:

- `opencv-python`
- `numpy`
- `pyautogui`
- `time`
- `random`

다음 명령어로 필요한 패키지를 설치할 수 있습니다:

```bash
pip install opencv-python numpy pyautogui
```

## 스크립트 개요

### `find_and_click_button(template_path, capture_region=(121, 323, 490, 95), match_threshold=0.75)`
이 함수는 화면에서 지정된 영역을 캡처하고, 주어진 템플릿 이미지(`template_path`)와 비교하여 버튼을 클릭합니다. 매칭 강도가 지정된 `match_threshold` 이상일 때 버튼을 클릭합니다.

### 작업 흐름:
1. **화면 캡처**: PyAutoGUI를 사용하여 지정된 영역(`capture_region`)의 화면을 캡처합니다.
2. **템플릿 매칭**: 캡처한 화면을 OpenCV의 `matchTemplate` 함수로 템플릿 이미지와 비교하여 매칭합니다.
3. **클릭 시뮬레이션**: 매칭 강도가 `match_threshold` 이상일 경우, 매칭된 영역의 중앙을 계산하여 클릭합니다. 클릭 시 ±5픽셀의 랜덤 오차를 추가합니다.
4. **반복 및 재시도**: 스크립트는 템플릿을 찾고 클릭할 때까지 계속 시도합니다. 재시도 전에 잠시 기다립니다.

### 종료 조건:
- OpenCV 창이 포커스된 상태에서 `ESC` 키를 누르면 종료됩니다.

## 참고 사항:
- `capture_region` 값을 버튼이 나타나는 화면 영역에 맞게 조정해야 합니다.
- `match_threshold` 값은 매칭 강도의 기준을 결정합니다. 값이 높을수록 더 정확한 매칭이 필요하며, 값이 낮을수록 매칭이 더 유연하게 동작합니다.
- `template_path`는 화면에서 클릭하려는 버튼이나 요소의 템플릿 이미지 경로여야 합니다.

---
