import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('images', help='image filenames in YYYYmmDDHHMM format', nargs='*')
args = parser.parse_args()

filenames = [filename for filename in args.images]
for filename in filenames:
    img = cv2.imread(filename,0)
    equlized = cv2.equalizeHist(img)
    cv2.imwrite('equlized_' + filename, equlized)
