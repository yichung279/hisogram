import numpy as np
import cv2

def discreteHaarWaveletTransform(img, level) :
    cache = np.empty(img.shape)
    length = int(img.shape[0] / (2 ** (level-1)))

    # horizontal
    for i in range(length):
        for j in range(int(length/2)):
            sum = img[i][j * 2] + img[i][j * 2 + 1]
            diff = img[i][j * 2] - img[i][j * 2 + 1]
            cache[i][         j] = sum/2
            cache[i][int(length/2) + j] = diff/2

    # vertical 
    for j in range(length):
        for i in range(int(length/2)):
            sum = cache[i * 2][j] + cache[i * 2 + 1][j]
            diff = cache[i * 2][j] - cache[i * 2 + 1][j]
            img[         i][j] = sum/2
            img[int(length/2) + i][j] = diff/2

    return img

if __name__ == '__main__':
    level = 3 
    filename = 'lena512.bmp'

    img = cv2.imread(filename,0)

    for i in range(level):
        img = discreteHaarWaveletTransform(img, level= i+1)

    cv2.imwrite('lena512.dwt.png', img)
