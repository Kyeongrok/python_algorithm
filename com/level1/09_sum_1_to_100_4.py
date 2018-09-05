def sum_start_to_end(start, end):
    result = 0;

    for num in range(start, end + 1):
        result = result + num

    return result

print("result:", sum_start_to_end(1, 100))
