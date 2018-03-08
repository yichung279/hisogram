from argparse import ArgumentParser
import cv2

PrgumentParser.add_argument('filename', help='filename of image going to histogram equalization')
args = parser.parse_args()

img = cv2.imread(args.filename,0)
equlized = cv2.equalizeHist(img)
cv2.imwrite('equlized_' + args.filename, equlized)
