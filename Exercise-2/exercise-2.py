print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i in range(10):
    num_sum = previous_num + i
    print(f"Current number: {i}, Previous number: {previous_num}, Sum: {num_sum}")
    previous_num = i
