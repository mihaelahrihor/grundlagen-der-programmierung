def is_perfect_number(num):
    if num <= 0:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


def is_column_sum_perfect(matrix):
    if not matrix:
        return False

    num_columns = len(matrix[0])
    for col in range(num_columns):
        column_sum = sum(row[col] for row in matrix)
        if not is_perfect_number(column_sum):
            return False
    return True


# Exemplu de utilizare
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = is_column_sum_perfect(matrix)
print(result)  