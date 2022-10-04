# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number


#range(1,n+1)


# def fizzBuzz(n):
#     # n = int(input())
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 ==0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# fizzBuzz(8)


# def fizzBuzz(n):
#     if n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     elif n % 3 and n % 5 == 0:
#         return 'FizzBuzz'
#     else:
#         return n

# fizzBuzz()

def fib(num):
    if num == 0:
        return 0
    else:
        return num + fib(num + 1)

        
fib(8)