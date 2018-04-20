import cv2
import numpy as np
import math

def makeImg(fshift, filename):
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    
    cv2.imwrite('frequency_' + filename, magnitude_spectrum)
    
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    cv2.imwrite('spatial_' + filename, img_back)

def makeFilter():

if __name__ == "__main__":
    img = cv2.imread('456.png', 0)
    
    rows, cols = img.shape
    ffilter = [[0] * cols] * rows
    crow,ccol = math.ceil(rows/2) , math.ceil(cols/2)
    
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    

    makeImg(fshift, 'origin.png')
    
    makeImg(fshift, 'highpass.png')

    
