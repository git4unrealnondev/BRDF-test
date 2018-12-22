import numpy as np
import cv2
import os
import os.path
import logging
import sys
from PIL import Image
import pathlib
import math
import simplejson
import re

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

def Replace(str): 
    make = str.make
    final = str.translate(make(', .', '., ')) 
    return ret 

def LDRParse():
	global LDR_Final
	LDR_Final = []
	for y in LDRLod:
		result = [x.strip() for x in y.split(',')]
		LDR_Final.append(result)
	return

def BWCalc(src,CusCount,PassVar,height,width,FW,IntialCount):
	LDRParse()
	lst = CusCount
	temp=[]
	temp1=[]
	test=[]
	n=[]
	countz=0
	height,width,channel = GetImageDimensions(FW[IntialCount])
	Count = len(FW)
	a=[]
	x=0
	y=0
	for x in range (height):
			for y in range(width):
				ListLookup = ReverseFind(x,y,height,width)
				CurrentInt = ([item[ListLookup] for item in CusCount])
				countz=0
				a=[]
				b=[]
				for egs in FW:
					#b = (CusCount[countz][ListLookup])
					b.append([CusCount[countz][ListLookup]])
					#b = np.array([b])
					a.append([LDR_Final[countz][0],LDR_Final[countz][1],LDR_Final[countz][2]])
					#a.append[[LDR_Final[countz][0]],[LDR_Final[countz][1]],[LDR_Final[countz][2]]]
					
					#x = np.linalg.lstsq(a, b, rcond=None)[0]
					#x = np.linalg.solve(a, b)
					countz +=1
				print (a,b)
				#x = np.linalg.solve(a, b)
				print (len(a)-1)
				c = 0
				z = []
				for eff in b:
					z.append(b[c][0])
					c+=1
				print (z)
				c=0
				for eff in b:
					x = np.linalg.lstsq(a, z, rcond=-1)
					c+=1
				c=0
				temp = []
				for eff in x[3]:
					temp.append(x[3][c])
					c +=1

				print (temp)
			
				input ('pause')
	
	
	
	

		
				#for Li in LDR_Final:
					#ld1=
					#print (Li[0][0])
	#while countzz<len(LDR_Final):
	#	countz = 0
	#	temp = []
	#	while countz<3:
	#		rest = float(LDR_Final[int(countzz)][int(countz)])
		
	return 
def WriteBWImage(FW,IntialCount,CusCount):
	CusCount = CusCount
	PassVar = FW[IntialCount]
	ColorFile = open("colorfile.txt", "a")
	ColorFile.write(str(IntialCount)+'_FINAL_\n')
	ColorFile.close()
	srct = cv2.imread(FW[IntialCount], 0)
	height,width,channel = GetImageDimensions(FW[IntialCount])
	
	BWCalc(srct,CusCount,PassVar,height,width,FW,IntialCount)
	#for x in range (height):
	#			for y in range(width):
	#				INTEN = BWCalc(srct,x,y,CusCount,PassVar,height,width,FW)
	#				srct[x,y] = INTEN
	#cv2.imwrite(str(IntialCount)+'_FINAL_'+'.png',srct)
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
		#Dont Piss With This Its Hard.
		x = 0
		y = 0
		lists=[]
		templist = []
		CusCount = []
		filename = FilteredWords[0]
		height,width,channel = GetImageDimensions(filename)
		count = 0
		for templ in FilteredWords:
			templist = []
			img = cv2.imread(templ)
			print (templ)
			for x in range (height):
				for y in range(width):
					nm,nn,nb = img[x,y]
					templist.append(nm)
			CusCount.append(templist)
		WriteBWImage(FilteredWords,InitialCount,CusCount)
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

