#!/usr/bin/env python3
import urllib.request
import sys
import zipfile
import os.path
import optparse

#
# Fetches sample input and output data from kattis.
#

_URL_ = "https://kth.kattis.com/download/sampledata?id="
_USAGE_ = """
fetch.py <problem id> [-p <path>]

Fetches input and output data provided by kattis
"""

# Get zipfile and unzip.
def fetch(problem, path=""):
	def _reporthook(dataz, datao, data):
		pass
	
	try:
		response = urllib.request.urlretrieve(_URL_+problem, reporthook=_reporthook)
		filename = response[0]
		
		with zipfile.ZipFile(filename) as _zip:
			print("Data downloaded. Unzipping...")
			files_which_already_exist = []
			for n in _zip.namelist():
				if os.path.exists(n):
					files_which_already_exist.append(n)
			if len(files_which_already_exist) > 0:
				print("The following files already exist in your directory and will be replaced:")
				print(" ".join(files_which_already_exist))				
				print()
				ans = input("Continue? (Y/N) ")
				if not ("y" in ans or "Y" in ans):
					sys.exit(1)
			_zip.extractall(path)
		print("Extracted: " + " ".join(_zip.namelist()))
	except zipfile.BadZipfile as e:
		print("No such problem id: " + problem)
	

def main():
	opt = optparse.OptionParser()
	opt.add_option('-p', '--path', dest='path', metavar='PATH', help='Path where to save the example data.')

	opts, args = opt.parse_args()
	
	if len(args) == 0:
		print(_USAGE_)
		sys.exit(1)
		
	fetch(args[0], opts.path)
		
	
	
if __name__ == "__main__":
	main()
