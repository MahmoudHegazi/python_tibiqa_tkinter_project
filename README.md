# python_tibiqa_tkinter_project

Game At (Tibia.py) full
## Description : 
a two-dimensional tile-based game set in a fantasy world with pixel art graphics and a top-down perspective.
(final goal Online DeskTop python tkinter project)

simple python game with tkinter

# target

![image](https://user-images.githubusercontent.com/55125302/155734097-9c46ce37-9b1d-4de7-85f4-e5bad9c43450.png)


## compass update dynamic for hero or monster or other objects (current)
![image](https://user-images.githubusercontent.com/55125302/155733492-99f89cb3-a01b-4946-ba30-f909ec6bd289.png)


![image](https://user-images.githubusercontent.com/55125302/155687939-67bd9201-f178-4201-bc0e-45249b993e9e.png)

## 1D PY tkinter move right and left with keyboard arrow py (1d left and right controlled using strict py logic)

using this logic reduce 0 chance of error what ever size of current map or champion size or square size or game delay speed

![image](https://user-images.githubusercontent.com/55125302/155692690-5b5ea7f5-5bbe-455c-abe0-7e41e8bc7f8d.png)


## 2D technology to move the hero (x, y) math to calculate boundaries and create a dynamic map

![image](https://user-images.githubusercontent.com/55125302/155696026-f8dd17f3-4fe3-42f3-ad18-aa1befde9015.png)


city_map and compas + with diagonally


| + | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | (0,0) | (50,0) | (100,0) | (150,0) | (200,0) | (250,0) | 300,0) |
| B | (0,50) | (50,50) | (100,50) | 🔵 (150,50) | 🔘 (200,50) | (250,50) | (300,50) |
| C | (0,100) | (50,100) | (100,100) | 🔘 (150,100) | 🟢 (200,100) | (250,100) | (300,100) |


####### current (150,50) need move diagonally right have (200, 50) and (150, 100) so it will  (diagonally (Right Down) with compas can down and can right

```
(200, y1+square (50 + 50) = 100) (200,100)
```

```cx,cy = x1, y1+square = ncx,ncy```

##### note this rule not work only on geting 1 value it can get all after th needed value or before for spells actions and effects 
 
 ```cx,cy = x1, y1+square = ncx,ncy```
 ```cx,cy = x1+square, y1+square = ncx,ncy``` move right +sqaure on x1
![image](https://user-images.githubusercontent.com/55125302/155826103-65eb206b-7570-42e3-85ac-179138a4af3a.png)


