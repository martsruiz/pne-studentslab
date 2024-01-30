def fibon (n):
    fibonacci_list = [0, 1]
    for i in range (2, n):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list

print("Fibonacci list: " + str (fibon (16)))

a = fibon(16)
print("5th term Fibonacci sequence: ", a[5])
print("10th term Fibonacci sequence: ", a[10])
print("15th term Fibonacci sequence: ", a[15])