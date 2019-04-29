import fnmatch
import os

rootPath = raw_input ("What should be the starting directory? ") # "dirpath"
pattern = raw_input ("What is the file name? ") # "file name"

for root, dirs, files in os.walk(rootPath):
	for filename in fnmatch.filter(files, pattern):
		print(os.path.join(root, filename))
