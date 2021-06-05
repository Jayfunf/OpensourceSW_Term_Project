# OpensourceSW_Term_Project
## 21년도 오픈소스SW Term Project

---
### 2021/05/18

Title: Initial commit

Exp: 깃 사용을 위해 깃 repo 생성 및 초기화 작업을 진행함.

---
### 2021/05/19~20

Title: create branches

Exp: 각 팀원들의 개인 branch를 생성함.

---
### 2021/05/21

Title: target object detect(a4 paper)

Exp: a4 용지를 detectiong하기 위한 함수 추가 및 수정을 진행함. 테스트할 이미지들을 추가함.

modify_.py: paperDet.py
add_.py: utlis.py, edgedet.py, sckit.py
add_IMG: testIMG1, testIMG2, testIMG3, testIMG4, testIMG5,testIMG6, pot.jpg
delete_.py: mediapipe.py

reference:
https://github.com/murtazahassan/Document-Scanner

필요패키지
```
pip install matplotlib 
```
---
### 2021/05/29

Title: Countour, big_Countour

Exp: OpenCV 라이브러리를 냄비 검출에 활용, 필요한 지점은 냄비의 위쪽 원의 반지름이 필요하므로 이미지 전처리 후 contour를 찾아내는 작업을 함.
```C
def pot_contour(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.BGR2GRAY)
    blur = cv2.GaussianBlur(img, (5,5), 0)
    ret, th = cv2.threshold(blur, 127, 255, 0)
    contours, _ = cv2.findContours(th, 2, 1)
    return contours
```
이렇게 얻은 값을 실제 냄비 이미지에 적용해보았으나 제대로 된 contour 값을 찾아내지 못함(냄비의 경우 배경이 완전 검은색이 아니였을 경우 배경에 노이즈를 같이 잡아냄)

modify : utils.py
add fun: findContours(), contourArea(), drawContours()

---
### 2021/05/30

Title: modify

test : biggest Data
Merge CMH to main

---
### 2021/06/01

Title: ApproxPolyDP & cylinder(냄비를 대표로) detect

Exp: approxPolyDP(): line length를 통해 Contour를 간략하게 만들어주는 함수 --> 추가, cv2.HoughCircles를 활용해서 냄비 입구를 검출하기 시도함. 하지만 냄비 입구 자체가 완벽한 원이 아니라 타원형이라 검출을 제대로 하지못함. 그래서 타원을 검출할 수 있는 scikit library를 활용해 hough_ellips를 사용해봤지만 냄비의 비슷한 색 때문에 입구 자체를 detection하는게 불가능했음

add_.py: selector.py
add_fun: approxPolyDP()
Merge YCB to main

---
### 2021/06/02

Title: Corner detect

Exp: cornerHarris(): 코너를 검출하는 함수. np.where()를 통해 최소한의 Corner를 검출함.

add_fun: cornerHarris()
modify_.py: selector.py
Merge YCB to main

---
### 2021/06/03

Title: Improve Corner dectect accuracy

Exp: 계산한 알고리즘을 추가함., 값이 비슷하게 겹치는 Corner들을 '필요한 좌표의 특징'을 이용해 하나로 줄여, 성능 개선에 기여함., 자동으로 냄비의 정확한 입구를 검출하는 것이 힘들어 selectROI를 활용
cv2.selectROI는 관심영역을 사람이 직접 지정해 프로세싱하는 기술로 마우스 드래그를 통해서 직접 냄비의 입구와 냄비 높이를 bounding box 형태로 찾아내는 함수를 작성함.
```C
def pot_select(img_path):
    img = cv2.imread(img_path)
    x, y, w, h = cv2.selectROI('image', img, False)
    
    if w and h:
        feature = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 204, 3)

    return feature
```

add_.py: A4detect.py + Test.py
modify_fun: cv2.selectROI()
modify_.py: __pycache__.pyc

---
### 2021/06/05

Title: Add Calculating formula & final

Exp: 알고리즘을 수정함. 보는 시각, 도형의 성질, Reference Object와 Value Object와의 관계를 통해 Value Object의 Volume을 계산하는 공식을 코드로 구현함., 검출된 냄비 입구와 냄비 높이를 A4용지와 비교해 실제 냄비 부피를 측정하여 라면을 몇 개 끓일 수 있는지 도출

modify_.py: Test.py 
add : image
