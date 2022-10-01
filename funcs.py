import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import cv2
import matplotlib
import matplotlib.image as img
import numpy as np
from PIL import Image, ImageTk

matplotlib.use( "TkAgg" )
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure

global image1


# def arthadd(image1, value):
#     number = int( value )
#     new = np.array( image1, dtype=np.float32 )
#     new += number
#     new = np.where( new > 255, 255, new )
#     new = np.array( new, dtype="uint8" )
#     image1=new
#     return image1

def brightness(image1, original, value):
    if value == 5:
        return original
    elif value > 5:
        return arthadd( image1, value )
    else:
        return arthsubtract( image1, value )


def arthadd(image1, value):
    return cv2.add( image1, value )


# function to get previous image
def previous():
    global image1
    global image2
    image1 = image2
    image2 = image1
    return image1


# def arthsubtract(image1, value):
#     number = int( 30 )
#     image1 = np.array( image1, dtype=np.float32 )
#     image1 -= number
#     image1 = np.where( image1 < 0, 0, image1 )
#     image1 = np.array( image1, dtype=np.uint8 )
#     return image1

def arthsubtract(image1, value):
    return cv2.subtract( image1, value )


# def arthmultiply(image1, value):
#     number = int( 30 )
#     image1 = np.array( image1, dtype=np.float32 )
#     image1 *= number
#     image1 = np.where( image1 > 255, 255, image1 )
#     image1 = np.array( image1, dtype=np.uint8 )
#     return image1


def arthmultiply(image1, value):
    if value == 0:
        return image1
    else:
        return cv2.multiply( image1, value )


# def arthdivison(image1, value):
#     number = int( 30 )
#     image1 = np.array( image1, dtype=np.float32 )
#     image1 /= number
#     image1 = np.where( image1 > 255, 255, image1 )
#     image1 = np.array( image1, dtype=np.uint8 )
#     return image1


def arthdivison(image1, value):
    if value == 0:
        return image1
    else:
        return cv2.divide( image1, value )


def histogram_equalization(image1):
    image1 = cv2.equalizeHist( image1 )
    return image1


def median_filter(image1):
    image1 = cv2.medianBlur( image1, 3 )
    return image1


def bilateral(image1):
    blur = cv2.bilateralFilter( image1, 9, 75, 75 )
    return blur

def average_filter(image1):
    image1 = cv2.blur( image1, (3, 3) )
    return image1



def gaussian_filter(image1):
    image1 = cv2.GaussianBlur( image1, (3, 3), 0 )
    return image1


# def Bit_plane_slicing(img, k):
#     image = np.array( img, dtype='uint8' )
#     [rows, columns] = image.shape
#     bitplane = np.array( image, dtype='uint8' )
#     for r in range( rows ):
#         for c in range( columns ):
#             bitplane[r][c] = (image[r][c] >> k) & 1
#     return bitplane


#
# def threshold1(image):
#     return cv2.threshold( image, 127, 255, cv2.THRESH_BINARY )
#
# def threshold2(image):
#     return cv2.threshold( image, 127, 255, cv2.THRESH_BINARY_INV )
#
# def threshold3(image):
#     return cv2.threshold( image, 127, 255, cv2.THRESH_TRUNC )
#
# def threshold4(image):
#     return cv2.threshold( image, 127, 255, cv2.THRESH_TOZERO )
#
# def threshold5(image):
#     return cv2.threshold( image, 127, 255, cv2.THRESH_TOZERO_INV )



# def contrast_stretching(image1):
#     return cv2.filter(c)
#

# def contrast_stretching(image1):
#     read_image = image1
#     image = np.array( read_image )
#     new_image = np.array( read_image )
#     s1 = 0
#     s2 = 255
#     r1 = np.min( read_image )
#     r2 = np.max( read_image )
#     rows = image.shape[0]
#     columns = image.shape[1]
#     range_new = (s2 - s1)
#     range_old = (r2 - r1)
#     for i in range( rows ):
#         for j in range( columns ):
#             new_image[i, j] = (range_new / range_old) * (image[i, j] - r1) + s1
#     image1 = new_image.astype( np.uint8 )
#     return image1
#

# def thresholding(image, k):
#     return cv2.threshold( image, k, 255, cv2.THRESH_BINARY )
#

# function to colorize grayscale image
def colorize(image1):
    image1 = cv2.cvtColor( image1, cv2.COLOR_GRAY2RGB )
    return image1


# def Thresholding(image, k):
#     image = np.array( image, dtype='uint8' )
#     [rows, columns] = image.shape
#     bw = np.array( image, dtype='uint8' )
#     for i in range( rows ):
#         for j in range( columns ):
#             if image[i][j] > k:
#                 bw[i][j] = 0
#             else:
#                 bw[i][j] = 1
#     return bw
#

def original(image):
    return image

#
# def graylevelslicing(image):
#     return cv2.filter( graylevelslicing )
#
#
# def logTransform(img1):
#     return cv2.filter( logTransform )
#
#
# def powerTransform(img1):
#     return cv2.filter( powerTransform )
#
#
# def inversePower(img1):
#     return cv2.filter( inversePower )
#
#
# def gammaCorrection(img1):
#     return cv2.filter( gammaCorrection )
#
#
# def bitPlaneSlicing(img1):
#     return cv2.filter( bitPlaneSlicing )
#
#
# def GLPF(img):
#     image1 = img.filter( ImageFilter.GaussianBlur )
#     return image1
#
#
# def laplacian(image1):
#     image1 = image1.filter( ImageFilter.FIND_EDGES )
#     return image1
#
#
# # def inverseLog(img1):
# #     image = np.array( img1 )
# #     r = np.array( img1 )
# #     c = 255 / (np.log( 1 + np.max( img1 ) ))
# #     inverseLog = np.exp( img1 / c ) - 1
# #     inverseLog = np.array( inverseLog, dtype=np.uint8 )
# #     image1=inverseLog
# #     return image1
#
# # def log(imgpil):
# #     image = np.array( imgpil )
# #     r = np.array( imgpil )
# #     c = 255 / np.log( 1 + np.max( r ) )
# #     log_image = (c * np.log( 1 + r )) + 1
# #     log_image = np.array( log_image, dtype=np.uint8 )
# #     image1=log_image
# #     return image1
# #

def image_negative(image1):
    image1 = 255 - image1
    return image1


#
# def Negative(image):
#     neg = np.array( image, dtype='uint8' )
#     L = 2 ** 8
#     neg = (L - 1) - neg
#     image1= neg
#     return image1


def sharpening(image1):
    kernel = np.array( [[0, -1, 0], [-1, 5, -1], [0, -1, 0]] )
    image1 = cv2.filter2D( image1, -1, kernel )
    return image1