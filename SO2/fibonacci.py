
fibonacci_list = [0, 1]
for i in range (2, 11):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

print("Fibonacci list: " + str (fibonacci_list))

