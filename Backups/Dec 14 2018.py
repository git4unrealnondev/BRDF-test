import numpy as np
import cv2
import os
import os.path
import logging
import sys
from PIL import Image
import pathlib
import math

def KSpec(V,R,S):
	Ks = dot(v,r)
	Ks = Ks ** S
	return Ks

def GetImageDimensions(filename):
	img = cv2.imread(filename)
	height, width, channels = img.shape
	return height, width, channels

def makegreyscale(filename):
	global img
	LX = 1
	LY = 1
	LZ = 1
	## This turns images black
	text = filename
	global filenameminusext
	filenameminusext, sep, tail = text.partition('.')
	img = cv2.imread(filename)
	b, g, r  = cv2.split(img)
	cv2.imwrite(filename+'_B.PNG' , b)
	cv2.imwrite(filename+'_G.PNG' , g)
	cv2.imwrite(filename+'_R.PNG' , r)
	im_gray = cv2.imread( filename , cv2.IMREAD_GRAYSCALE)
	#(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	#cv2.imwrite(filenameminusext+'_BW.PNG', im_bw)
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
		try:
			os.remove(fileclr)
			return
		except OSError:
			os.remove(fileclr)
			return
	else:
		print ('true')
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
		print (LDRLod)
		return

def LinEqc(templist):


		
	
		A = np.array([])
	
		B = np.array([])
		return


def ReverseFind(x,y,height,width):
	tempfloor = x * width
	floor = tempfloor + y
	return floor
def BWCalc(src,x,y,CusCount,PassVar,height,width):
	lst = CusCount
	count =0
	temp=[]
	test=[]
	ListLookup = ReverseFind(x,y,height,width)
	#lst2 = item[ListLookup] for item in CusCount
	print([item[ListLookup] for item in CusCount])
	#np.array
	#PULL LDR data data and stick it into an array.
	#LDRLod
	return 255
def WriteBWImage(FW,IntialCount,CusCount):
	CusCount = CusCount
	PassVar = FW[IntialCount]
	ColorFile = open("colorfile.txt", "a")
	ColorFile.write(str(IntialCount)+'_FINAL_\n')
	ColorFile.close()
	srct = cv2.imread(FW[IntialCount], 0)
	height,width,channel = GetImageDimensions(FW[IntialCount])
	for x in range (height):
				for y in range(width):
					INTEN = BWCalc(srct,x,y,CusCount,PassVar,height,width)
					srct[x,y] = INTEN
	cv2.imwrite(str(IntialCount)+'_FINAL_'+'.png',srct)
	#cv2.imwrite(FW[IntialCount]+'.png',cv2.cvtColor(src, cv2.COLOR_BGR2GRAY))
	return

def MakeArray(Files):

	global CusCount
	global fileclrimg

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
		fileclrimg = ReadColorFile()
		FilteredWords = filter(lambda word: ec in word, fileclrimg)
		FilteredWords = [*FilteredWords]
		# Every Loop FilteredWords changes, Run pixel code below.
		x = 0
		y = 0
		templist = []
		CusCount = []
		filename = FilteredWords[0]
		height,width,channel = GetImageDimensions(filename)
		count = 0
		
		# puts intensity vals in CusCount
		for listl in FilteredWords:
			#customL = listl + str(count)
			templist.clear()
			img = cv2.imread(listl)
			for x in range (height):
				for y in range(width):
					nm,nn,nb = img[x,y]
					templist.append(nm)
			CusCount.append(templist)
		lst2 = [item[89] for item in CusCount]
		print (lst2)
		input ('y')
		WriteBWImage(FilteredWords,InitialCount,CusCount)
				## THIS LINE HAS TEMPLIST AND IS CURRENT LIST FOR ALL FilteredWords In Current 
				## List ie all of _R intensity Values at x=0 y=0 CAN NOW DO LINEAR EXPRESSIONS WITH NUMPY.

				

		InitialCount +=1
	return

def FilterFunc(word):
	fileclrimg = ReadColorFile()
	word = '_R'
	if word in fileclrimg:
		return False
	else:
		return True

def CleanUp():
	print ('wiping Files')
	TEMP = checkfile('colorfile.txt')
	if TEMP is False:
		return
	else:
		imgstar = ReadColorFile()
		for images in (imgstar):
			if checkfile('colorfile.txt') is True:
				os.remove('colorfile.txt')
				return
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

