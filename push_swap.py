from collections import deque
import sys

a = deque()
b = deque()

#  Function for both sa && sb
#  If ss just call sx(a) && sx(b)
def sx(x):
	if len(x) > 1:
		val1 = x.popleft()
		val2 = x.popleft()
		x.appendleft(val1)
		x.appendleft(val2)

#  Functon for both pa && pb
#  Moves top value from s to e
def px(s, e):
	if len(s) > 0:
		e.appendleft(s.popleft())

# Function for both ra && rb
# If rr call rx(a) && rx(b)
def rx(x):
	x.rotate(-1)

# Function for both rra && rrb
# If rrr call rrx(a) && rrx(b)
def rrx(x):
	x.rotate(1)

def issorted(x):
	if (len(x) > 1):
		for i in range(len(x) - 1):
			if x[i] > x[i + 1]:
				return (False)
		return (True)
	else:
		return (True)

for nbr in sys.argv[1:]:
	a.append(int(nbr))


if a[0] > a[1]:
	sx(a)
	print("sa")
if a[0] > a[-1]:
	rrx(a)
	print("rra")
while len(b) == 0 or a[0] > b[0]:
	px(a,b)
	print("pb")
	if a[0] > a[-1] and a[-1] > b[0]:
		rrx(a)
		print("rra")
	if a[0] > a[1] and a[1] > b[0]:
		sx(a)
		print("sa")
while len(a) > 0:
	if len(a) > 1 and a[0] < a[1]:
		sx(a)
		print("sa")
	if a[0] > b[0]:
		px(a,b)
		print("pb")
	else:
		i = 0
		while a[0] > b[-1]:
			rrx(b)
			print("rrb")
			i += 1
		px(a, b)
		print("pb")
		while i >= 0:
			i -= 1
			rx(b)
			print("rb")
while len(b) > 0:
	px(b, a)
	print("pb")

print (a)


# sort = deque(sorted(list(a)))
# c = []
# while list(a).index(min(a)) != list(sort).index(min(a)):
# 	rx(sort)
# sort = list(sort)
# print(a)
# print(sort)
# for i, val in enumerate(sort):
# 	c.append([(list(a).index(val) - i + len(a)) % len(a), abs(list(a).index(val) - i - len(a)) % len(a), val])
# print(c)
# print(sort)
# print(list(a))
# for i, val in enumerate(a):
# 	r = (i - sort.index(val) + len(a)) % len(a)
# 	l = abs(i - sort.index(val) - len(a)) % len(a)
# 	c.append([l if l < r else r * -1, val])
# 	# c.append(l * -1 if r > l else r)
# print(c)
# avg = sum(c) / len(c)
# print(avg)
# for i, val in enumerate(c):
# 	if val > avg:
# 		px(a, b)
# 	else:
# 		rx(a)
# ac = []
# bc = []
# sorta = sorted(list(a))
# sortb = sorted(list(b))
# for i, val in enumerate(a):
# 	r = (i - sorta.index(val) + len(a)) % len(a)
# 	l = abs(i - sorta.index(val) - len(a)) % len(a)
# 	ac.append(l if r > l else r)
# for i, val in enumerate(b):
# 	r = (i - sortb.index(val) + len(b)) % len(b)
# 	l = abs(i - sortb.index(val) - len(b)) % len(b)
# 	bc.append(l if r > l else r)
# print(a)
# print(ac)
# print(b)
# print(bc)
