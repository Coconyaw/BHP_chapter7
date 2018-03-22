# coding:utf-8

import os

def run(**args):
	
	print("[*] In dirslister module.")
	files = os.listdir(".")

	return str(files)
