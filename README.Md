This program goes through given location and matches all videos name with their subtitles and changes names to a simple clean name for that series

## Installation:
1. Copy main python program file to any location u want.
2. Change **vsm** python file address (main_address variable) to the selected python file in step 1.
3. Copy and Paste **vsm** file to /usr/bin/ 
4. make sure **vsm** file is executable by running `sudo chmod 755 /usr/bin/vsm`

## USAGE :
vsm -t [ ] -n [ ] -e [ ]

### "-t" switch should be first one and it is required!
-t: [target folder location]
-n: [name to use as prefix for all files | defualt=working dir name]
-e: [exclude these folders from this program] ; format for multiple folders : -e "f1, f2, f3"


##NOTE :
make sure that ur series folders hierarchy is like  [Friends/Season1/...]