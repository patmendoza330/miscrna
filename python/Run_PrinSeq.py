import os
##BEGIN ENTERING VARIABLES
#this is the path to the prinseq command from your current directory
path1 = 'PRINSEQ-plus-plus/src'
#this is the path to your files
path2 = 'path2'
#This is the path to your output files
path3 = 'path3'
#This is the path to your log files
path4 = 'path4'
##END ENTERING VARIABLES

#the variable that will hold the path and file name of your prinseq executable
prinseqString = path1 + '/prinseq++'
#These next lines will help in the initializing of variables used in running prinseq
#this will hold the command that will initiate prinseq
commandString = ''
#this will be the filenames that you are cycling through
inFile = ''
outFile = ''
logfile = ''
#this will be the counter for the currently working file
j = 1
#this is the total number of files in the directory
k = len(os.listdir(path2))

#BEGIN RUNNING PRINSEQ
for filename in os.listdir(path2):
    #construct the filenames
    inFile = path2 + '/' + filename
    outFile = path3 + '/' + filename + 'polyA.gz'
    logfile = path4 + '/' + filename + 'polyA.log'
    commandString = prinseqString + ' -fastq ' + inFile + ' -threads 4 -trim_tail_left 10 ' \
            '-trim_tail_right 10 -min_len 40 -out_name ' + outFile + ' -out_gz ' \
            '-out_bad null -out_good ' + outFile + ' > ' + logfile
    print('Working on file ' + str(j) + ' of ' + str(k))
    print(commandString)
    os.system(commandString)
    j = j + 1
print('Prinseq completed!')
#END RUNNING PRINSEQ

#BEGIN CREATING A SUMMARY FILE
print('Begin creating summary file...')
j = 1
k = len(os.listdir(path4))
trimLeft = 0
trimRight = 0
minlength = 0
totalRemoved = 0
out1 = open(path3 + '/ConsolidatedLogFile.csv', 'w')
out1.write('FileName, -trim_tail_left, -trim_tail_right, -min_len, total' + '\n')
for filename in os.listdir(path4):
    print('Working on file ' + str(j) + ' of ' + str(k))
    file1 = open(path4 + "/" + filename, 'r')
    line1 = file1.readline().strip()
    #i = 0
    while line1:
        splitLine = line1.split(" ")
        if splitLine[4] == '-min_len':
            minlength = splitLine[0]
        elif splitLine[4] == '-trim_tail_left':
            trimLeft = splitLine[0]
        elif splitLine[4] == '-trim_tail_right':
            trimRight = splitLine[0]
        #i = i + 1
        line1 = file1.readline().strip()
    # I need to condense the string that I want to write here
    totalRemoved = int(trimLeft) + int(trimRight) + int(minlength)
    out1.write(filename + ', ' + str(trimLeft) + ', ' + str(trimRight) + ', ' + str(minlength) +
               ', ' + str(totalRemoved) + '\n')
    file1.close()
    trimLeft = 0
    trimRight = 0
    minlength = 0
    totalRemoved = 0
    j = j + 1
print('Finished creating summary file')
out1.close()
#END SUMMARY FILE

print('Job completed!')