import numpy as np
import cv2
import os
import os.path
import logging
import sys
from PIL import Image
import pathlib

def Dansom(AT,AB,B,M,N):
	TEMP1 = 1 / (3.14 * AT * AB)
	print (TEMP1)
	return
	TEMP1 = 2*(Dot(N,V))
	TEMP2 = Dot(N,V)
	TEMP3 = A**2
	TEMP4 = (Dot(N,V))**2
	TEMP5 = 1 - A**2
	TEMP6 = TEMP5 + TEMP4
	TEMP6 = math.sqrt (TEMP6)
	TEMP6 = TEMP2
	FINAL = TEMP1 / TEMP6
	return FINAL

def KDiff(L,P):
	Kd = dot(L,P)
	return Kd

def KSpec(V,R,S):
	Ks = dot(v,r)
	Ks = Ks ** S
	return Ks

def GetImageDimensions(filename):
	img = cv2.imread(filename)
	height, width, channels = img.shape
	return height, width, channels
	X = [6,5,4]
	Y = [3,2,1]
	DotProduct = np.dot(Light , KD)
	print('Dot product is : ' , DotProduct)
	return

def makegreyscale(filename):
	global img
	LX = 1
	LY = 1
	LZ = 1
	## This turns images black
	print (filename, 'filename to make grey scale')
	text = filename
	global filenameminusext
	filenameminusext, sep, tail = text.partition('.')
	img = cv2.imread(filename)
	b, g, r  = cv2.split(img)
	cv2.imwrite(filename+'_B.PNG' , b)
	cv2.imwrite(filename+'_G.PNG' , g)
	cv2.imwrite(filename+'_R.PNG' , r)
	im_gray = cv2.imread( filename , cv2.IMREAD_GRAYSCALE)
	(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imwrite(filenameminusext+'_BW.PNG', im_bw)
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(filenameminusext+'_TRUEBW.PNG', gray_image)
	print ('Wrote File' , filenameminusext+'_BW.PNG' , 'to disk')
	#writes names of files to colorfile.txt
	ColorFile = open("colorfile.txt", "a")
	ColorFile.write(filename+'_B.PNG\n')
	ColorFile.write(filename+'_G.PNG\n')
	ColorFile.write(filename+'_R.PNG\n')
	ColorFile.write(filenameminusext+'_TRUEBW.PNG\n')
	ColorFile.close()
	return

def getfileslist(filelist):
	global filelistimg
	# this opens .txt file into list to load images later
	checkfile(filelist)
	with open (filelist, "r") as myfile:
		filelistimg = myfile.read().splitlines()
	return

def checkfile(file):
	# this checks files if the file exists it returns if it dosnt exist than the program halts and waits for user input
	if os.path.isfile(file) and os.access(file, os.R_OK):
		return True
	else:
		logging.warning(' %s Does not exist', file )
		print (file, 'does not exist')
		#input("Press Enter to continue...")
		return False

def BWLoop():
	for x in filelistimg:	
		makegreyscale(x)
	return

def ConvertJPEGtoPNG(filelist):
	imagestoConvert = [k for k in filelistimg if 'jpeg' in k]
	imagestoConvert = imagestoConvert+[k for k in filelistimg if 'jpg' in k]
	print (imagestoConvert)
	for object in imagestoConvert:
		checkfile(object)
		print (object)
		ConvertJPEGtoPNGConverting(object)
		return

def ConvertJPEGtoPNGConverting(filenametoconvert):
	im = Image.open(filenametoconvert)
	print (filenametoconvert)
	filenametoconvertsanitized, sep, tail = filenametoconvert.partition('.')
	print (filenametoconvertsanitized)
	im.save(filenametoconvertsanitized+'.png', "PNG")
	os.remove(filenametoconvert)
	return
	
	return

def ColorFileDeleter():
	fileclr = 'colorfile.txt'
	if os.path.exists(fileclr):
		os.remove(fileclr)
		return 
	else:
		return 

def ReadColorFile():
	fileclr = 'colorfile.txt'
	with open (fileclr, "r") as myfile:
		fileclrimg = myfile.read().splitlines()
		return fileclrimg

def LinChk(x,y):
	ReadColorFile()
	Valid_Images = []
	for filenam in fileclrimg:
		filenametoconvertsanitized, sep, tail = filenam.partition('.')
		img = cv2.imread(filenam)
		nm,nn,nb = img[x,y]
		return nm
	
def LinSolve(filename):
	x = 0
	y = 0
	filename = filename
	h,w,c = GetImageDimensions(filename)
	w = w+1
	h = h+1
	for x in range (w):
		for y in range(h):
			nm = LinChk(x,y)
	return nm
	
def GrabLightDirs(LDF):
	checkfile(LDF)
	global LDRLod
	with open (LDF, "r") as myfile:
		LDRLod = myfile.read().splitlines()
		return

def LinEqc(templist):

		
	
		A = np.array([])
	
		B = np.array([])
		return



def MakeArray(Files):
	InitialCount = 0
	while InitialCount < 4:
		if InitialCount == 0:
			ec = '_R.PNG'
		if InitialCount == 1:
			ec = '_G.PNG'
		if InitialCount == 2:
			ec = '_B.PNG'
		if InitialCount == 3:
			ec = '_TRUEBW.PNG'
		global fileclrimg
		fileclrimg = ReadColorFile()
		FilteredWords = filter(lambda word: ec in word, fileclrimg)
		FilteredWords = [*FilteredWords]
		# Every Loop FilteredWords changes, Run pixel code below.
		x = 0
		y = 0
		templist =[]
		filename = FilteredWords[0]
		h,w,c = GetImageDimensions(filename)
		w = w+1
		h = h+1

		print (FilteredWords)
		#Calls PER PIXEL IS PIZDEC
		for x in range (w):
			for y in range(h):
				templist.clear()
				for temp in FilteredWords:
					img = cv2.imread(temp)
					#print (img)
					nm,nn,nb = img[x,y]
					templist.append(nm)
					
					
				
				## THIS LINE HAS TEMPLIST AND IS CURRENT LIST FOR ALL FilteredWords In Current 
				## List ie all of _R intensity Values at x=0 y=0 CAN NOW DO LINEAR EXPRESSIONS WITH NUMPY.

				

		
		input("Press Enter to continue...")
		InitialCount +=1
	return

def FilterFunc(word):
	fileclrimg = ReadColorFile()
	word = '_R'
	if word in fileclrimg:
		print (False)
		return False
	else:
		print (word)
		return True

def CleanUp():
	print ('wiping Files')
	TEMP = checkfile('colorfile.txt')
	if TEMP is False:
		return
	else:
		imgstar = ReadColorFile()
		for images in (imgstar):
			os.remove(images)
			print (images)
		
	os.remove('colorfile.txt')
	
	return



#Sets Logging Details
logging.basicConfig(filename='log.txt', level = logging.DEBUG)

#sets filename to read from and sanitizes all incoming files
filelist = 'test.txt'
LDF_File = 'LDR.txt'
global fileclrimg
global filename 
global filenameminusext
CleanUp()
ColorFileDeleter()
getfileslist(filelist)
ConvertJPEGtoPNG(filelist)
GrabLightDirs(LDF_File)	
BWLoop()
MakeArray(filelistimg)