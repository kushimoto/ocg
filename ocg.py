import cv2
import numpy as np
import random
import os

charcters = ['a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p',
             'q', 'r', 's', 't',
             'u', 'v', 'w', 'x',
             'y', 'z', 'A', 'B',
             'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3',
             '4', '5', '6', '7',
             '8', '9'
            ]

for c in charcters:

    # ファイル名をセット
    img_name = './' + c + '.png'

    # ファイルが存在するか確認
    if os.path.isfile(img_name):
        img = cv2.imread(c + '.png', -1)
    else:
        sys.exit(1)


    # 座標４点をリセット
    #
    # (p1x, p1y) +------+ (p4x, p4y)
    #            |      |
    #            | 画像 |
    #            |      |
    # (p2x, p2y) +------+ (p3x, p3y)
    #
    p1x = 0
    p1y = 0
    p2x = 0
    p2y = 100
    p3x = 100
    p3y = 100
    p4x = 100
    p4y = 0

    # ３回いろんな方向へひっぱったり縮めたり
    for i in range(3):

        # よくわからん
        rows,cols,_=img.shape

        # どの点をいじるかランダムで決定
        point = random.randrange(4)

        # ひっぱるか縮めるかランダムで決定
        toggle = random.randrange(1)

        # どのくらい動かすかランダムで決定
        dx = random.randrange(25)
        dy = random.randrange(25)

        # 動かす直前の座標
        pts1 = np.float32([[p1x,p1y],[p2x,p2y],[p3x,p3y],[p4x,p4y]])

        if point == 0:
            if toggle:
                p1x = p1x + dx
                p1y = p1y + dy
            else:
                p1x = p1x - dx
                p1y = p1y - dy
        elif point == 1:
            if toggle:
                p2x = p2x + dx
                p2y = p2y + dy
            else:
                p2x = p2x - dx
                p2y = p2y - dy
        elif point == 2:
            if toggle:
                p3x = p3x + dx
                p3y = p3y + dy
            else:
                p3x = p3x - dx
                p3y = p3y - dy
        elif point == 3:
            if toggle:
                p4x = p4x + dx
                p4y = p4y + dy
            else:
                p4x = p4x - dx
                p4y = p4y - dy

        # 動かした後となる座標をセット
        pts2 = np.float32([[p1x,p1y],[p2x,p2y],[p3x,p3y],[p4x,p4y]])

        # やっちゃえ日産
        M = cv2.getPerspectiveTransform(pts1,pts2)
        img = cv2.warpPerspective(img,M,(cols,rows))

    # 色反転 (文字が白で背景黒いから文字が黒で背景を白にする)
    img = cv2.bitwise_not(img)

    # 白を透明にする
    img[:, :, 3] = np.where(np.all(img == 0, axis=-1), 255, 0)

    # 保存 (大文字小文字を判断しているだけ)
    if c.islower():
        if os.path.isdir('./lowercase'):
            cv2.imwrite('./lowercase/' + c + '.png', img)
            print("[DONE] ./lowercase/" + c + ".png")
        else:
            os.mkdir('./lowercase')
    elif c.isupper():
        if os.path.isdir('./uppercase'):
            cv2.imwrite('./uppercase/' + c + '.png', img)
            print("[DONE] ./uppercase/" + c + ".png")
        else:
            os.mkdir('./uppercase')
    elif c.isdigit():
        if os.path.isdir('./digit'):
            cv2.imwrite('./digit/' + c + '.png', img)
            print("[DONE] ./digit/" + c + ".png")
        else:
            os.mkdir('./uppercase')
