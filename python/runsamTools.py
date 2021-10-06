import os

#Enter the path to your hisat2 sam files
path1 = "path1"

#Enter the path to the BAM output directory
path2 = "path2"

#Enter the path to the BAM index output directory
path3 = "path3"

#File name counter
j = 1

#total files
k = len(os.listdir(path1))

print("Working on samtools...")

for filename in os.listdir(path1):
    print("Working on sam file " + str(j) + " out of " + str(k))
    samFile = path1 + "\\" + filename
    bamFile = path2 + "\\" + filename + ".bam"
    print('samtools sort -@ 4 -o ' + bamFile + ' ' + samFile)
    os.system('samtools sort -@ 4 -o ' + bamFile + ' ' + samFile)
    j = j + 1
print("Done!")

#create the index files
#File name counter
j = 1

#total files
k = len(os.listdir(path2))
for filename in os.listdir(path2):
    print("Working on sam index file " + str(j) + " out of " + str(k))
    bamFile = path2 + "\\" + filename
    bamIndexFile = path2 + "\\" + filename + ".bai"
    print('samtools index ' + bamFile + ' ' + bamIndexFile)
    os.system('samtools index ' + bamFile + ' ' + bamIndexFile)
    j = j + 1
print("Done!")
