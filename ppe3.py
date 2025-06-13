def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication not possible. Columns of A must equal rows of B.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

product = multiply_matrices(A, B)
print("Resultant Matrix:")
for row in product:
    print(row)
