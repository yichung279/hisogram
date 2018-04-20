import numpy as np
import math
import cv2

def makeImg(fshift, filename):
    # calc magnitude of frequency and save as img 
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    cv2.imwrite('frequency_' + filename, magnitude_spectrum)
    
    # inverse frequency back to pixels and save as img
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.abs(np.fft.ifft2(f_ishift))
    cv2.imwrite('spatial_' + filename, img_back)

if __name__ == "__main__":
    # load img
    img = cv2.imread('456.png', 0)
    rows, cols = img.shape
    crow, ccol = math.ceil(rows/2) , math.ceil(cols/2)
    
    # Fourier tansfrom origin img(and shift)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    
    # make a 30 x 30 lowpass filter
    radius = 30
    lowPassFilter = np.zeros((rows, cols), np.int8) 
    lowPassFilter[crow - radius: crow + radius, ccol - radius: ccol + radius] = 1

    # make a 5 x 5 highpass filter
    radius =  5
    highPassFilter = np.ones((rows, cols), np.int8) 
    highPassFilter[crow - radius: crow + radius, ccol - radius: ccol + radius] = 0
    
    # bandoass filter
    bandPassFilter = highPassFilter * lowPassFilter

    # input_img * filter = output_img
    makeImg(fshift, 'origin.png')
    makeImg(fshift * lowPassFilter, 'lowPass.png')
    makeImg(fshift * highPassFilter, 'highPass.png')
    makeImg(fshift * bandPassFilter, 'bandPass.png')
