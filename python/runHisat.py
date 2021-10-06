import os, subprocess

# IMPORTANT you need to make copies of your gzipped trimmed files
# into a folder where they will be decompressed
#Enter the path to your hisat2 genome index files
path1 = "path1"
#Enter the prefix to your hisat2 genome index files
prefix1 = "genome"

#Enter the path to the SAM output directory
path2 = "path2"

#Enter the path to the log file directory
path3 = "path3"

#Enter the path to your unzipped trimmed files
path4 = "path4"

#Enter the path to your summary log file
path5 = "path5"

#File name counter
j = 1

#total files
k = len(os.listdir(path4))

genomePath = path1 + "\\" + prefix1
# ctrl + / will block and unblock selected code
for filename in os.listdir(path4):
    if filename.endswith('.gz'):
        alignFile = path4 + "\\" + filename
        subprocess.call(["gzip", "-d", alignFile])
        print(str(j) +" file unzipped out of " + str(k))
    j = j + 1
j = 1
for filename in os.listdir(path4):
     oldName = path4 + "\\" + filename
     newName = path4 + "\\" + filename + ".fastq"
     os.rename(oldName, newName)
     print(str(j) + " file renamed out of " + str(k))
     j = j + 1
j = 1
# This needs to be run from the command line so you need
# to run the python script from this point
for filename in os.listdir(path4):
    print("Working on file " + str(j) + " of " + str(k))
    alignFile = path4 + "\\" + filename
    alignFile = alignFile.replace("\\", "/").strip()
    sumFileName = path3 + "\\" + filename + ".log"
    sumFileName = sumFileName.replace("\\", "/").strip()
    samFile = path2 + "\\" + filename + ".sam"
    samFile = samFile.replace("\\", "/").strip()
    genomePath = genomePath.replace("\\", "/").strip()
    #subprocess.call(["hisat2", "-p", "4", "--min-intronlen", "36", "--max-intronlen", "50000", "--summary-file", sumFileName, "--dta", "-x", genomePath, "-U", alignFile, "-S", samFile])
    print('hisat2 -p 4 -k 20 --summary-file ' + sumFileName + ' --dta -x ' + genomePath + ' -U ' + alignFile + ' -S ' + samFile)
    os.system('hisat2 -p 4 --min-intronlen 36 --max-intronlen 50000 --summary-file ' + sumFileName + ' --dta -x ' + genomePath + '  -U ' + alignFile + ' -S ' + samFile)
    #out1.write('hisat2 -p 4 --min-intronlen 36 --max-intronlen 50000 --summary-file ' + sumFileName + ' --dta -x ' + genomePath + ' -U ' + alignFile + ' -S ' + samFile + "\n")
    j = j + 1
print("Done!")

#Create a summary file
print("Writing the summary file...")

#File name counter
j = 1

#total files
k = len(os.listdir(path3))

out1 = open(path5 + '\\ConsolidatedLogFile.csv', 'w')
out1.write('FileName, Total Reads, ' + 'Unpaired, Unpaired %, ' + '0 Alignments, \
    0 Alignments % , 1 Alignments, 1 Alignments %, >1 Alignments, \
    >1 Alignments %, Overall Alignment Rate' + '\n')
for filename in os.listdir(path3):
    print("Working on summary file " + str(j) + " of " + str(k))
    file1 = open(path3 + "\\" + filename, 'r')
    out1.write(filename + ",")
    line1 = file1.readline().strip()
    i = 0
    while line1:
        splitLine = line1.split(" ")
        if i in range(1, 5):
            out1.write(splitLine[0] + ",")
            out1.write(splitLine[1].replace('(', '').replace(')', '') + ",")
        else:
            out1.write(splitLine[0] + ",")
        i = i + 1
        line1 = file1.readline().strip()
    out1.write("\n")
    j = j + 1
    file1.close()
out1.close()
print("Done!")