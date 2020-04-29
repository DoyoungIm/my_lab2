# uni_inter.py
def uni_inter():
	l1=eval(input("1st list: "))
	l2=eval(input("2nd list: "))
	set1=set(l1)
	set2=set(l2)
	uni=set1|set2
	inter=set1&set2
	result1=list(uni)
	result2=list(inter)
	print(result1)
	print(result2)
