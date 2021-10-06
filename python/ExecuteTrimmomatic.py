import os
import subprocess
import gzip

# Enter the path to your source files
path1 = "path1"

# Enter the path to the output directory
path2 = "path2"

# Enter the path to the log file directory
path3 = "path3"

# Enter the path to the program file
path4 = "C:\\trim"

# os.chdir(path1)
# switch out this next line with the previous line
os.chdir(path4)
# print(os.getcwd())
fileString = ""

in1 = ""
out1 = ""
out2 = ""
out3 = ""
trimFile = ""
commandScript = ""
j = 0

for filename in os.listdir(path1):
    if j <= len(os.listdir(path1)):
        if j == 0:
            fileString = filename
            j = j + 1
        else:
            fileString = fileString + '--' + filename
            j = j + 1
    continue
# print (fileString)
##will need to get rid of the first entry that has an empty string
backExtrlist = fileString.split('--')
# I need to update this to include the log by appending " > log.log " into the command
for i in backExtrlist:
    in1 = path1 + "\\" + i
    out1 = path2 + "\\" + i + "trimmed.gz"
    out2 = path3 + "\\" + i + "trimLog.log"
    out3 = path3 + "\\" + i + "logfile.log"
    trimFile = path4 + "\\" + "trimmomatic-0.39.jar"
    # adaptersPath = "ILLUMINACLIP:" + path4 + "\\adapters\\TruSeq3-SE.fa:2:30:10"
    # print(in1)
    # print(out1)
    # print(out2)
#    commandScript = "java -classpath " + trimFile + " org.usadellab.trimmomatic.TrimmomaticSE -threads 4 -trimlog " \
#                    + out2 + " " + in1 + " " + out1 + " ILLUMINACLIP:adapters/TruSeq3-SE.fa:2:30:10 LEADING:25 " \
#                    + "TRAILING:25 SLIDINGWINDOW:4:25 MINLEN:52 > " + out3
    commandScript = "java -classpath " + trimFile + " org.usadellab.trimmomatic.TrimmomaticSE -threads 4 -trimlog " \
                    + out2 + " " + in1 + " " + out1 + " ILLUMINACLIP:adapters/TruSeq3-PE.fa:2:30:10:1:TRUE LEADING:3 " \
                    + "TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:40 > " + out3
    # print(commandScript)
    os.system(commandScript)
    # subprocess.call(
    #    ["java", "-classpath", trimFile, "org.usadellab.trimmomatic.TrimmomaticSE", "-threads", "4",
    #     "-trimlog", out2, in1, out1, "ILLUMINACLIP:adapters/TruSeq3-SE.fa:2:30:10", "LEADING:25", "TRAILING:25",
    #     "SLIDINGWINDOW:4:25", "MINLEN:52", ">", out3])
print('Job Done!')

# check the length of the nucleotides in the file
# os.chdir(path1)
# readLength = []
# result = False
# out1 = open(path1 + 'read_report.csv', 'w')
# for filename1 in backExtrlist:
#    with gzip.open(filename1, 'rb') as cosFile:
#        j = 0
#        k = 0
#        readLength = []
#        for line in cosFile:
#            if j == 1 or ((j-1)/4).is_integer():
#                readLength.append(len(line))
#                k = k + 1
#            j = j + 1
#    print(filename1)
#    out1.write(filename1 + ',')
#    result = False
# Check to see if the lengths of the reads are all the same
# or not
#    if len(readLength) > 0:
#        result = all(elem == readLength[0] for elem in readLength)
#    if result:
#        print("All Elements in List are Equal to " + str(readLength[0]))
#        out1.write("All Elements in List are Equal to " + str(readLength[0]) + '\n')
#    else:
#        print("All Elements in List are Not Equal")
#        out1.write("All Elements in List are Not Equal" + '\n')
#    cosFile.close()
# print("Job Completed")
# out1.close()


# Will need to switch to subprocess.call: https://docs.python.org/3/library/subprocess.html

# os.system("java -classpath trimmomatic-0.39.jar org.usadellab.trimmomatic.TrimmomaticSE -threads 4 -trimlog Hydro_1/xtrim.log Hydro_1/11759_5751_119945_H22TGBGXG_Hydroponics_1_F02_WT_0Cu_O2_R1_AATCCG_R1.fastq.gz Hydro_1/11759_5751_119945_H22TGBGXG_Hydroponics_1_F02_WT_0Cu_O2_R1_AATCCG_R1_TRIMMED.fastq.gz ILLUMINACLIP:adapters/TruSeq3-SE.fa:2:30:10 LEADING:25 TRAILING:25 SLIDINGWINDOW:4:25 MINLEN:36")
# print(os.getcwd())
# os.system("java -classpath trimmomatic-0.39.jar org.usadellab.trimmomatic.TrimmomaticSE -threads 4 -trimlog Hydro_1/xtrim.log Hydro_1/11759_5751_119945_H22TGBGXG_Hydroponics_1_F02_WT_0Cu_O2_R1_AATCCG_R1.fastq.gz Hydro_1/11759_5751_119945_H22TGBGXG_Hydroponics_1_F02_WT_0Cu_O2_R1_AATCCG_R1_TRIMMED.fastq.gz ILLUMINACLIP:adapters/TruSeq3-SE.fa:2:30:10 LEADING:25 TRAILING:25 SLIDINGWINDOW:4:25 MINLEN:36")
