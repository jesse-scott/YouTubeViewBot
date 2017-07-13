# Developed by Jesse Scott
# Windows version

import os
import sys
import time
import socket

os.system("title YouTube View Bot")
os.system("color f0")
os.system("cls")
print("Please paste a YouTube video URL.")
print("")
url = input("[YouTubeViewBot url]# ")

def openURL():
	os.system("start " + url)
	time.sleep(5)
	openURL()
	
openURL()