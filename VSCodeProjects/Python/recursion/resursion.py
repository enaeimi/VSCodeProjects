def sum_up_to(n):
    if n==1:
        return 1
    else: 
        return n + sum_up_to(n-1)

print(sum_up_to(100))




def is_palindrom(word):
    if len(word) < 2:
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrom(word[1:-1])

print(is_palindrom("madamimadam"))




def s(n, acc=0):
    if n==0:
        return acc
    else:
        return s(n-1, acc+n)

print(s(1000))


def func(n):
    if n==1:
        print(1)
    else:
        print(n)
        func(n-1)
        print(n)

func(20)




def isPrime(n, i=2):
  for i in range(2,n):
    if n%i == 0:
      return False
  return True

def isPrime_rec(n, call_stack, i=2):
  call_stack.append('isPrime('+str(i)+')')
  print(call_stack)
  
  if i == n:
    call_stack.pop()
    print(call_stack)
    return True
  elif n%i == 0:
    call_stack.pop()
    print(call_stack)
    return False
  
  else:
    call_stack.pop()
    print(call_stack)
    return isPrime_rec(n,call_stack,i+1)

callStack = []
isPrime_rec(11, callStack)



##################################################
def divisor(n):
    div = []
    for i in range(1,n+1):
        if n%i == 0:
            div.append(i)
    
    return div

print(divisor(12))



def divisor_rec(n, i=1, div=[]):
    if i>n:
        return div
    elif n%i == 0:
        div.append(i)

    return divisor_rec(n,i+1,div)

print(divisor_rec(12))

###################################################
def getMin(arr):
    minVal = float('inf')
    for i in range(len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
    
    return minVal



def getMin_rec(arr,i=1,minVal=float('inf')):
    if i==len(arr):
        return minVal
    elif arr[i] < minVal:
        minVal=arr[i]

    return getMin_rec(arr,i+1,minVal)

print(getMin_rec([2,3,5,6,9,8,7,1,2,5,6,]))



def contains(arr,val,i=0):
    if arr[i]==val:
        return True
    elif i>=len(arr):
        return False
    else:   
        return contains(arr,val,i+1)

print(contains([2,3,5,6,9,8,7,1,2,5,6,],10))

