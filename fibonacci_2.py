#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci_mine(n):
	i = 1
	f0 = 0
	f1 = 1
	if n == 0:
		return 0
	while i < n:
		f2 = f1 + f0
		f0 = f1
		f1 = f2
		i += 1
	return f2

def fibonacci(n):
	current = 0
	after = 1
	for i in range(0, n):
		current, after = after, current + after
	return current


print fibonacci(3)
print fibonacci(36)
#>>> 14930352