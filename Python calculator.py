name = input("enter your name : ")
print (name + " welcome")
n1 = input ("write your first number :  ")
operator =input("enter your operator (+,-,*,/) : ")
n2 = input ("enter your second number : ")
n1=int(n1)
n2=int(n2)
if operator=='+':
	print (n1+n2)
elif operator=='-':
	print (n1- n2)
elif operator=='*':
	print (n1*n2)
elif operator=='/':
	print(n1/n2)
else:
	print ("invalid operator")
print ("Thank You")
