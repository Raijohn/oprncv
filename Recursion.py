n=5
sum=0

for i in range(n+1):
    sum = sum + i 
print(sum)

def totle(value):
    if value == 1:
        return 1
    else:
        return value+ totle(value-1)
    
print(totle(5))

#fibonacci series
def fibonacci_series(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci_series(number-1)+fibonacci_series(number-2)
    
print(fibonacci_series(9),fibonacci_series(8))