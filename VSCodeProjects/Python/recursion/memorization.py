

def fib(n,lookup):
    key = str(n)
    if key in lookup:
        return lookup[key]
    elif n <= 1:
        lookup[key] = n
        return lookup[key]
    else:
        lookup[key] = fib(n-1)+fib(n-2)
        return lookup[key]
		# return fib(n-1)+fib(n-2)


def fib(n):
    if n <= 1: 
        return n
    else:
        return fib(n-1)+fib(n-2)
