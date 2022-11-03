#!/usr/bin/env python
import numpy as np
import png  # https://raw.github.com/drj11/pypng/main/code/png.py

import _rdrand as rd

W, H = 1920, 1080

img = np.array([[rd.rand16() for _ in range(W)] for _ in range(H)])

with open("test_rdrand_grey.png", "wb") as f:
    w = png.Writer(img.shape[1], img.shape[0], greyscale=True, bitdepth=16)
    w.write(f, img)

img = np.array([[rd.rand16() for _ in range(W*3)] for _ in range(H)])

with open("test_rdrand_color.png", "wb") as f:
    w = png.Writer(img.shape[1]//3, img.shape[0], greyscale=False, bitdepth=16)
    w.write(f, img)

img = np.zeros([H, W*3], int)

for i in range(H):
    if i % 2:
        for j in range(W*3):
            if j % 2:
                img[i][j] = rd.rand16()
            continue


with open("test_rdrand_glen.png", "wb") as f:
    w = png.Writer(img.shape[1]//3, img.shape[0], greyscale=False, bitdepth=16)
    w.write(f, img)
