#this program selects a local file and appends desired test to that file
#using prompts, input, Files and I/O, strings, and decision making 
import os


signature = input("Enter your signature: ")
path = input("Enter the path of the file you wish to sign: ")
check = input("Is " + path + "your desired file?(Y/n): ")
while True:
    if(check.lower() == "y"):
        break
    elif(check.lower() == "n"): 
        path = input("Enter the path of the file you wish to sign: ")
        check = input("Is " + path + " your desired file?(Y/n): ")
    else: 
        check = input("Is " + path + " your desired file?(Y/n): ")

#TODO search for file with chdir

dirs = path.rpartition("/")
if dirs[1] == '':
    dirs = path.rpartition("\\")
path = dirs[0]
file = dirs[2]

os.chdir(path)

#TODO handle FileNotFoundError

#open file 
f = open(file, "w");

#offset 0 from 2 (which is the end of file parameter)
f.seek(0, 2)
f.write("\n" + signature)
f.close()

print("\n" + "\"" + signature + "\"" + " was added to the end of the file " + "\"" + file + "\"" + " at " + "\"" + path + "\"")
