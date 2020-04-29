#!/usr/bin/python
import my_pkg

def main():
	while True:
		a=int(input("Select menu: 1) conversion 2) union/intersection 3) exit ?"))
		if a==1:
			my_pkg.conversion()
		elif a==2:
			my_pkg.uni_inter()
		else:
			print("exit the program")
			break
main()
