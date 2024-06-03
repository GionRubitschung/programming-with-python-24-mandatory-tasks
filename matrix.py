from matrix import Matrix2Dim


def main():
    matrix1 = Matrix2Dim((2, 3))
    matrix1.initialize(1.0)
    print("Matrix 1:")
    print(matrix1)

    transposed_matrix1 = matrix1.transpose()
    print("Transposed Matrix 1:")
    print(transposed_matrix1)

    print("\nIs Matrix 1 symmetric?")
    print(matrix1.is_symmetric())

    print("\nTotal of Matrix 1:")
    print(matrix1.total())

    print("\nAverage of Matrix 1:")
    print(matrix1.average())

    print("\nStandard Deviation of Matrix 1:")
    print(matrix1.stddeviation())

    print("\nIs Matrix 1 coherent?")
    print(matrix1.is_coherent())

    matrix2 = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nMatrix 2:")
    print(matrix2)

    transposed_matrix2 = matrix2.transpose()
    print("Transposed Matrix 2:")
    print(transposed_matrix2)

    print("Is Matrix 2 symmetric?")
    print(matrix2.is_symmetric())

    print("\nTotal of Matrix 2:")
    print(matrix2.total())

    print("\nAverage of Matrix 2:")
    print(matrix2.average())

    print("\nStandard Deviation of Matrix 2:")
    print(matrix2.stddeviation())

    print("\nIs Matrix 2 coherent?")
    print(matrix2.is_coherent())


if __name__ == "__main__":
    main()
