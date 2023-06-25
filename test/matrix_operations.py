import numpy as np
import sys

# функція для зчитування елементів матриці з файлу
def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        size = list(map(int, lines[0].split()))
        matrix_data = [list(map(float, line.split())) for line in lines[1:]]
        return np.array(matrix_data), size

# функція для запису елементів матриці у файл
def write_matrix(filename, matrix):
    with open(filename, 'w') as file:
        size = f"{matrix.shape[0]} {matrix.shape[1]}\n"
        matrix_data = "\n".join(" ".join(str(round(num, 2)) for num in row) for row in matrix)
        file.write(size + matrix_data)

# функція для додавання елементів матриць
def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

# функція для віднімання елементів другої матриці від елементів першої
def subtract_matrices(matrix1, matrix2):
    return matrix1 - matrix2

# функція для множення елементів матриць
def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

# функція для знаходження визначника заданої матриці
def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# функція для знаходження зворотньої матриці
def calculate_inverse(matrix):
    return np.linalg.inv(matrix)

# зчитування назви файлу першої матриці та операції, яку треба виконати
input_filename1 = sys.argv[1]
operation = sys.argv[2]
matrix1, size1 = read_matrix(input_filename1)

# перевірка обраної операції та її виконання
if operation == "=":
    output_filename = sys.argv[3]
    write_matrix(output_filename, matrix1)
elif operation == "det":
    result = calculate_determinant(matrix1)
    output_filename = sys.argv[3]
    with open(output_filename, 'w') as file:
        file.write(str(round(result, 2)))
elif operation == "inv":
    result = calculate_inverse(matrix1)
    output_filename = sys.argv[3]
    write_matrix(output_filename, result)
else:
    input_filename2 = sys.argv[3]
    matrix2, size2 = read_matrix(input_filename2)

    if operation == "+":
        result = add_matrices(matrix1, matrix2)
    elif operation == "-":
        result = subtract_matrices(matrix1, matrix2)
    elif operation == "*":
        result = multiply_matrices(matrix1, matrix2)
    
    output_filename = sys.argv[4]
    write_matrix(output_filename, result)
