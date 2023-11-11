def count_repeated_numbers(s):
    count_dict = {}
    for digit in s:
        if digit.isdigit():
            digit = int(digit)
            if digit in count_dict:
                count_dict[digit] += 1
            else:
                count_dict[digit] = 1

    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    result = {}
    for i in range(3):
        if i < len(sorted_counts):
            result[sorted_counts[i][0]] = sorted_counts[i][1]

    return result

s = "12345678900987654321"
result = count_repeated_numbers(s)
print(result)