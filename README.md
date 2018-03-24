# TorrentCleaner
Scans for Torrent folder, removes unsupported files extension, brings any files at the base directory, removes empty folders

Example

	/some/root/dir/Torrent1.avi  
	/some/root/dir/Torrent2.mp4  
	/some/root/dir/Unwanted-Folder/Torrent3.avi  
	/some/root/dir/Unwanted-Folder/Unwanted-file.nfo  

This will move every files at root directory, remove unnecessary files and folder and will become

	/some/root/dir/Torrent1.avi
	/some/root/dir/Torrent2.mp4
	/some/root/dir/Torrent3.avi

# Configuration
Edit the file and select which folder to run the scrip into. This will be your base directory  

basedir = '/some/path/you/want'  

You can add files of your interest, for the moment it is case sensitive to if you need to add an extension do not forget to add the capital letter eg: .mp3 .MP3:  

supported_ext = (".avi", ".AVI", ".mkv", ".MKV",".mp4",".MP4", ".srt",".SRT", ".m4a",".M4A", ".mp3",".MP3")

# Execution
To launch the script, just use Python2.7 as follow
python /path/to/script/scriptname.py
