import os
path1 = "path1"
path2 = "path2"
os.chdir(path1)
print(os.getcwd())
fileString = ""

for filename in os.listdir(path1):
    #the next line can be adjusted or commented out
    #if filename.endswith('.bam'):
    #fileString = fileString + ' ' + filename
    fileString = fileString + ' ' + path2 + '\\' + filename
    continue
print (fileString)