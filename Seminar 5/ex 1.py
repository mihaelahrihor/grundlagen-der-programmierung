def sum_diag(matrix):
    result = []

    for i in range(len(matrix)):
        sum_linie = 0


        for j in range(len(matrix)):
            #target = matrix[i][j]

            if i != j:
                sum_linie += matrix[i][j]

            if sum_linie == matrix[i][i]:
                result.append(True)
            else:
                result.append(False)


def test_sum_diag():
    aseert sum_diag([
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
    ]) == [True, True, False]

def main(): pass

test_sum_diag()

main()