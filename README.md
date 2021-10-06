# Misc Scripts 

Here I have a few miscellaneous scripts that I used during my RNA-seq. This repository is not in its final state and scripts are not clean, this is temporarily housing those scripts until I have created a final location and edits.

Briefly, it contains the following:

* Trimmomatic - ExecuteTrimmomatic.py - this will run trimmomatic (paramters are hardcoded) for every file in a particular folder.
* Trommomatic - TrimmLogSum.py - will create a summary of the trimmomatic output.
* Prinseq - Run_PrinSeq.py - this will run prinseq on your trimmed files and create a summary of the output
* HISAT2 - runHisat.py - will take files in a directory, unzip them, run hisat and create a summary file
* Samtools - runsamTools.py - will create BAM and BAI files on all files in a directory
* HTseq - CreateHTSeqCommand.py - this creates the command for the HTSeq program. Its inputs are the bam and bai files, gtf file and ouput is the raw counts file.
* General - Grab_file_names.py - grab the file names for all files in a directory separated by spaces