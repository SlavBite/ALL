import random

"""  #задача 1
n = int(input())

print((n+1) // 2)
"""

"""  # задача 2
w = int(input())
t = int(input())
string = 0
column = 0
times =  t // (w * 2 + 2)
t = t % (w * 2 + 2)
column = times*2

if t >= w:
	string += w
	t -= w
	if t >= 1:
		column += 1
		t -= 1
		if t >= w:
			string -= w
			t -= w
			if t == 1:
				column += 1
				t -= 1
		else:
			string -= t
			t -= t
else:
	string += t
	t -= t
	
print(string, column)
print(t)
"""	

"""  # задача 3
n = int(input())
m = int(input())
h = 0
for i in range(n):
	h += int(input())
	
if h / n >= m:
	print(0)
else:
	print(m * n - h)
"""

"""  # задача 4
   
n = int(input())
m = int(input())
k = []
for i in range(m):
	k.append(i+1)

btns = [0] * n
for i in k:
	for j in range(len(btns)):
		if (j+1) % i == 0:
			btns[j] = 0 if bool(btns[j]) else 1  		
print(btns.count(1))
"""		
		
	 # задача 5

n = 10000 ** 100000
answer = int(n * (n+1) // 2)
print(answer)		
