from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

# creating a .txt file 
f = open('textfile.txt','w')
f.write('This is my first sentence using this method to write something in a .txt file with python\n')
f.close()

#using the parameter 'a' allows me to add more things to the .txt file.
# user the 'w' parameter would overwrite the whole .txt file
f = open('textfile.txt','a')
f.write ("*** Current Time by opening this .txt file: ***\n" + current_time)
f.close()

