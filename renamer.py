import csv
import os
import shutil


ifile1  = open('input.csv', "rt")
reader1 = csv.reader(ifile1)

directory = "sample_files"

file_extension = ".txt"

files = os.listdir(directory)
os.chdir(directory)

# from parent dir - go in sub dirs
for file in files:
	file_name = file + ""
	long_name = os.getcwd() + "\\" + file_name 
	# print (long_name)

	# reset to HEAD of csv file.
	ifile1.seek(0)

	# iterate through the csv file
	for row1 in reader1:

	# assign the current row's column to a var
		product_SKU = row1[0]
		name = row1[1] 

	# debugging; print data
		# print (product_SKU)
		# print (name)

		current_file_sku = file_name[:-4]
		# print (current_file_sku)

		if product_SKU == current_file_sku:
			name = name + file_extension
			print ("renaming " + file_name + " to " + name)
			# print (long_name)
			os.rename(long_name, name)	 		

ifile1.close()
