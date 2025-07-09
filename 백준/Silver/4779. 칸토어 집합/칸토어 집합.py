

def cantor(n):
	if n==0:
		return "-"

	before = cantor(n-1)
	return before + " "*3**(n-1) + before

while True:
	try:
		n = int(input())
		line = cantor(n)
		print(line)
	except:
		break
