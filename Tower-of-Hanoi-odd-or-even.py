# Tower of Hanoi
# coded by Julia Hiyeon Kim (c)2022
#
# order of movements:
# 	odd or even number of rings
# 	odd -> target
# 		empty middle to target to get next even
# 	even -> middle
# 		empty taget to middle to get next odd
#
# to overcome its visual impairment, it counts.



def count_moves(c):
	c[0] = c[0] + 1


def shuffle(z, a, b, c, s, m, t):
	if (len(a) - s) == 0:
		return
	else:
		if (len(a) - s)%2 == 1:
			print("Move disk ",a[len(a)-1]," from ",a[0]," to ",c[0])
			c.append(a.pop())
			count_moves(z)
			
			if (len(b) - m) > 0:
				x = len(a)
				y = len(c)
				shuffle(z, b, a, c, m, x, y)
		else:
			print("Move disk ",a[len(a)-1]," from ",a[0]," to ",b[0])
			b.append(a.pop())
			count_moves(z)
			
			if (len(c) - t) > 0:
				x = len(a)
				y = len(b)
				shuffle(z, c, a, b, t, x, y)

	shuffle(z, a, b, c, s, m, t)
		


source = []
middle = []
target = []

source.append('source')
middle.append('middle')
target.append('target')

entered = input("Enter the number of rings: ")
print(entered)
print("\n")

try:
	number = int(entered)
	
	if number <= 0:
		raise Exception("Only positive integer is allowed for the number of rings.")

	y = number
	for x in range(number):
		source.append(y)
		y -= 1

	moves = []
	moves.append(0)

	print("Moves:", moves[0])
	print(source, middle, target, sep="\n")
	print("\n")

	shuffle(moves, source, middle, target, 1, 1, 1)

	print("\n")
	print("Moves:", moves[0])
	print(source, middle, target, sep="\n")
except:
	print("Only positive integer is allowed for the number of rings.")
