#!/usr/bin/env python3
import urllib.request
import sys
import zipfile
import os.path

#
# Fetches sample input and output data from kattis.
#

_URL_ = "https://kth.kattis.com/download/sampledata?id="
_USAGE_ = """
fetch.py <problem id>

Fetches input and output data provided by kattis
"""

# Get zipfile and unzip.
def fetch(problem):
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
			_zip.extractall()
		print("Extracted: " + " ".join(_zip.namelist()))
	except zipfile.BadZipfile as e:
		print("No such problem id: " + problem)
	except Exception as e:
		print(e)
	

def main():
	if len(sys.argv) == 1:
		print(_USAGE_)
		sys.exit(1)
		
	fetch(sys.argv[1])
		
	
	
if __name__ == "__main__":
	main()
