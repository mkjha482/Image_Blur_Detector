# Logic:- Convert a regular image into a gray scale image and check the no. of edges in it using
# the laplacian operator. If the no. of edges is lesser than 50, that means an image has low noise
# and hence it is a blurred image while if the no. of edges is greater than 50 that means that the
# image has high noise and hence it is not blurred.
# We will be using open-cv library of python for image processing functionalities.
import cv2 as cv

import numpy as np

# Counter Variable to move to next image file.

ctr="1"

# Total no. of blurred images in the given dataset

totblur = 19 # All the blurry images provided in the dataset
# Variable to count the total no. of blurred images of all the images tested

blurry=0

# Variables to count the total number of unblurred images.

Notblurry=0

# While loop to read all the image file from the directory Test_Images.

# All the images in the test directory has been named as integer numbers to optimise fetching of
# images from the directory and improving speed of program.

while int(ctr)<=45:

  ctr=str(ctr)

  # Used for reading image data and store it in variable img

  img = cv.imread(r"Test_Images/"+ctr+".jpg")

  # Used to convert colored image into gray scale image for better edge detection

  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  # Used to apply a Laplacian operator to the grayscale image and stores the output image

  laplacian_var = cv.Laplacian(gray, cv.CV_64F).var()

  print(ctr)

  print(laplacian_var)

  if laplacian_var<50:

    print("Image Blurry")

    blurry=blurry+1

  else:

    print("Image not blurry")

    Notblurry=Notblurry+1

  ctr= int(ctr)

  ctr=ctr+1 # loop ends

# print total no. of blurred images

print("No. of blurred images",blurry)

# print total no. of unblurred images

print("No. of Unblurred images", Notblurry)

print("Percentage Accuracy=", (blurry/totblur)*100)

# Used to close all the windows after termination of the program

cv.destroyAllWindows()