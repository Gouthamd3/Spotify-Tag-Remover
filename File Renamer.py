#just a file t rename songs which have some common name

import os, sys

# Get the path of current working directory 
path = os.getcwd() 
   
# Get the list of all files and directories 
dir_list = os.listdir(path) 
   
print("Files in '", path, "' :")  
# print the list 
print(dir_list)

file_type = ".mp3"
dat_remove = "[SPOTIFY-DOWNLOADER.COM] "
#renaming the files
for i in dir_list:
    if file_type in i:
        print(i)
        if i[0:len(dat_remove)] == dat_remove:
            os.renames(i,i[len(dat_remove):])
            print(i[len(dat_remove):], "Done!!")
