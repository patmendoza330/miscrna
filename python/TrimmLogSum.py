import os, pandas as pd

#this will be the path to the files that you want to open and report on
path1 = "path1"
outfilePath = "path2"
#this is the file counter for going through the files
j = 1

for filename in os.listdir(path1):
    print("Starting file " + str(j) + " of " + str(len(os.listdir(path1))))
    if filename.endswith(".log"):
        #creating a variable to house the path and the file name
        filePath = path1 + "\\" + filename
        #open the file for reading
        file1 = open(filePath, 'r')
        print("Opening file " + filename)
        #read the first line of the file
        line1 = file1.readline()
        print("Reading file...")
        #variable to store the row number
        i = 0
        #list of rowNum
        rowNum = []
        #list of lengths
        readLength = []
        #list of surviving
        readSurvival = []
        while line1:
            #store the line in an array
            rowData = line1.strip().split(" ")
            rowNum.append(int(i))
            #The first entry in the array is indexed at 0 so we need to program accordingly.
            originalLength = int(rowData[2]) + int(rowData[3]) + int(rowData[5])
            readLength.append(originalLength)
            readSurvival.append(int(rowData[2]))
            #prints a message that finished every million records
            if i % 1000000 == 0:
                print("Reading line " + str(i))
            i = i + 1
            line1 = file1.readline()
        print("Finished reading file")
        #close the input file
        file1.close()
        print("Transforming data...")
        # get the list of tuples from two lists.
        # and merge them by using zip().
        list_of_tuples = list(zip(rowNum, readLength, readSurvival))
        df = pd.DataFrame(list_of_tuples, columns = ['rowNum', 'readLength', 'readSurvival'])
        #preliminary grouping of data for writing
        grouped = df.groupby(by=['readLength', 'readSurvival']).count()
        #add the percentage to the report
        grouped["%"] = grouped.apply(lambda x: 100*x/x.sum())
        #the line below will subpercentage based on a level in the dataframe, but unnecessary for this
        #groupedperc = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
        grouped.to_csv(outfilePath + "\\" + filename + 'summary.csv')
        print("Finished writing report")
    j = j+1
#print a job completion
print('Job Done!')

# FOR ONE FILE

# import os, pandas as pd
#
# #this will be the path to the files that you want to open and report on
# path1 = "path1"
# outfilePath = "path2"
#
# #for filename in os.listdir(path1):
#     print("Starting file 1" + " of " + "1")
#     if fileToOpen.endswith(".log"):
#         #creating a variable to house the path and the file name
#         filePath = path1 + "\\" + fileToOpen
#         #open the file for reading
#         file1 = open(filePath, 'r')
#         print("Opening file " + fileToOpen)
#         #read the first line of the file
#         line1 = file1.readline()
#         print("Reading file...")
#         #variable to store the row number
#         i = 0
#         #list of rowNum
#         rowNum = []
#         #list of lengths
#         readLength = []
#         #list of surviving
#         readSurvival = []
#         while line1:
#             #store the line in an array
#             rowData = line1.strip().split(" ")
#             rowNum.append(int(i))
#             #The first entry in the array is indexed at 0 so we need to program accordingly.
#             originalLength = int(rowData[2]) + int(rowData[3]) + int(rowData[5])
#             readLength.append(originalLength)
#             readSurvival.append(int(rowData[2]))
#             #prints a message that finished every million records
#             if i % 1000000 == 0:
#                 print("Reading line " + str(i))
#             i = i + 1
#             line1 = file1.readline()
#         print("Finished reading file")
#         #close the input file
#         file1.close()
#         print("Transforming data...")
#         # get the list of tuples from two lists.
#         # and merge them by using zip().
#         list_of_tuples = list(zip(rowNum, readLength, readSurvival))
#         df = pd.DataFrame(list_of_tuples, columns = ['rowNum', 'readLength', 'readSurvival'])
#         #preliminary grouping of data for writing
#         grouped = df.groupby(by=['readLength', 'readSurvival']).count()
#         #add the percentage to the report
#         grouped["%"] = grouped.apply(lambda x: 100*x/x.sum())
#         #the line below will subpercentage based on a level in the dataframe, but unnecessary for this
#         #groupedperc = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
#         grouped.to_csv(outfilePath + "\\" + filename + 'summary.csv')
#         print("Finished writing report")
#     j = j+1
# #print a job completion
# print('Job Done!')