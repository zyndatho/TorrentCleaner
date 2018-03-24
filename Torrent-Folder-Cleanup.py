# -*- coding: utf-8 -*-
import os

#Configuration variables
basedir = '/some/root/dir'
supported_ext = (".avi", ".AVI", ".mkv", ".MKV",".mp4",".MP4", ".srt",".SRT", ".m4a",".M4A", ".mp3",".MP3")

#Init Variables
filelist = []
filetodelete = []
foldertodelete = []
i=0
j=0
k=0
print("[-Start-] Starting Process  : {0}").format(basedir) #Printing execution path
for root, dirs, files in os.walk(basedir): #Exploring the basedir folder
	for name in files:
		if name.endswith(supported_ext):
			filelist.append(os.path.join(root, name))
			filename=os.path.basename(filelist[i])
			pathfile=os.path.dirname(filelist[i])
			if pathfile == basedir:
				#Case good file ext in right directory
				print("[To Skip] Good directory for: {0}").format(filename) #Nothing to do
			else:
				#Case good file ext in wrong directory
				destination=basedir+"/"+os.path.basename(filelist[i])
				foldertodelete.append(pathfile)
				os.rename(filelist[i], destination) #Deplacement du fichier dans basedir
			i+=1
		else:
			#Case bad file ext
			filetodelete.append(os.path.join(root, name)) #Construction of the list
			foldertodelete.append(os.path.dirname(filetodelete[j]))
			os.remove(filetodelete[j]) #Will remove a non listed file extension
			j+=1

try:
	while k < len(foldertodelete):
		os.rmdir(foldertodelete[k])
		print("[Removes] The following dir : {0}").format(foldertodelete[k]) #Print removed dir
		k+=1
except:
	print("[ Error ] Removing this dir : {0}").format(foldertodelete[k])