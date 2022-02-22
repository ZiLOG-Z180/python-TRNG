#!/usr/bin/env python
import _rdrand as rd

import png  # https://raw.github.com/drj11/pypng/main/code/png.py

W, H = 1920, 1080

img = [[rd.rand16() for _ in range(W)] for _ in range(H)]

with open("test_rdrand_grey.png", "wb") as f:
    w = png.Writer(len(img[0]), len(img), greyscale=True, bitdepth=16)
    w.write(f, img)

img = [[rd.rand16() for _ in range(W*3)] for _ in range(H)]

with open("test_rdrand_color.png", "wb") as f:
    w = png.Writer(len(img[0])//3, len(img), greyscale=False, bitdepth=16)
    w.write(f, img)
