import os

#Enter the path to the bam files (can include the bai files as well)
path1 = "path1"

#Enter the path where the files will reside on the virtual server
path2 = "path2"

#Enter the path and file name where the gtf file will reside on the virtual server
path3 = "gtffile.gtf"

#Enter the path where the raw counts file will be stored
path4 = "rawCountFile.txt"

os.chdir(path1)
fileString = ""

for filename in os.listdir(path1):
    #the next line can be adjusted or commented out
    if filename.endswith('.bam'):
        fileString = fileString + ' ' + path2 + filename
        continue

newString = "htseq-count -f bam " + fileString.strip() + " " + path3 + " > " + path4
print(newString)