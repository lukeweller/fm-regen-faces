#!/usr/bin/env python3
# Luke Weller [https://github.com/lukeweller]
# Mar 8 2022
# -------------------------------------------
import sys

def get_os():

	os = sys.platform

	if os == 'linux' or os == 'linux2':
		return 'linux'
	elif os == 'darwin':
		return 'macos'
	elif os == 'win32':
		return 'windows'
	else:
		print('error: sys.platform returned an unrecognize/unsupported os: {}'.format(os))
		sys.exit(1)


if __name__ == '__main__':

	os = get_os()

	if os == 'linux' or 'macos':
		from os_lib import regen_faces_unix as regen_faces_lib
	elif os == 'windows':
		from os_lib import regen_faces_windows as regen_faces_lib
	else:
		print('error: get_os() returned an unrecognized os string: {}'.format(os))
		sys.exit(1)

	df = regen_faces_lib.load_rtf('./input/input.rtf')

	df = regen_faces_lib.preprocessing(df)

	df = regen_faces_lib.create_regens(df)
	