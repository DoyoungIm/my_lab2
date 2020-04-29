#conversion.py
def conversion():
	a=input("input binary number ")
	num=int(a,2)
	o=format(num,'o')
	h=format(num,'X')
	print("OCT>",o)
	print("DEC>",num)
	print("HEX>",h)
