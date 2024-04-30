def fibonacci(num):
    fibo = [0,1]
    i = 21
    while i <= num:
        next=fibo[i-1]+fibo[i-2]
        fibo.append(next)
        i = i+1
    return fibo
num1 = input("enter the number")
print(fibonacci(num1))
