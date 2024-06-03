class Matrix2Dim:
    """
    Two-dimensional matrix based on a list of lists of items and a tuple that defines the dimensions
    of the matrix (number of rows and number of columns).
    """

    def __init__(self, dimensions: tuple[int, int], elements=None) -> None:
        """Constructor
        :param dimensions: tuple (pair) of the size of both the dimensions.
        (first item of dimensions corresponds to the rows, second item to the columns)
        Important: the dimensions must be greater or equal to 1.
        :param elements: content of the matrix (list of lists of elements).
        """
        if elements is None:
            elements = []
        self.dimensions = dimensions
        self.elements = elements

    def __getitem__(self, index: int | tuple[int, int]):
        if isinstance(index, int):
            return self.elements[index]
        return self.elements[index[0]][index[1]]

    def initialize(self, value: float) -> None:
        """
        Initialize the content of the matrix with given value.
        :param value: value assigned to all the elements of matrix.
        """
        self.elements = []
        xs = [value] * self.dimensions[1]
        for i in range(self.dimensions[0]):
            self.elements.append(xs)

    def __str__(self):
        """
        Defines the way that class instance should be displayed. The __str__ method is called when
        the following functions are invoked on the object and return a string: print() and str().
        Without this function print() displays a class instance as an object and not as a human-readable way.
        :return: the human-readable string of a class instance (object).
        """
        output = (
            "(" + str(self.dimensions[0]) + ", " + str(self.dimensions[1]) + ")" + "\n"
        )
        max_length = max(
            len(str(element)) for line in self.elements for element in line
        )
        for line in self.elements:
            for element in line:
                output += f"| {str(element):>{max_length}s} |"
            output += "\n"
        return output

    def transpose(self):
        """
        Performs the matrix transposition based on swapping row and column.
        :return: the transposed matrix.
        """
        transposed_elements = [
            [self.elements[j][i] for j in range(self.dimensions[0])]
            for i in range(self.dimensions[1])
        ]
        transposed_matrix = Matrix2Dim(
            (self.dimensions[1], self.dimensions[0]), transposed_elements
        )
        return transposed_matrix

    def is_symmetric(self) -> bool:
        """
        Determine if a matrix is symmetric or not.
        :return: true if the matrix is symmetric, false otherwise.
        """
        if self.dimensions[0] != self.dimensions[1]:
            return False
        for i in range(self.dimensions[0]):
            for j in range(i + 1, self.dimensions[1]):
                if self.elements[i][j] != self.elements[j][i]:
                    return False
        return True

    def total(self) -> float:
        """
        :return: the sum of all the elements of the matrix.
        """
        total = 0.0
        for line in self.elements:
            for element in line:
                total += element
        return total

    def average(self) -> float:
        """
        :return: the average of the elements of the matrix.
        """
        total = self.total()
        return total / (self.dimensions[0] * self.dimensions[1])

    def stddeviation(self) -> float:
        """
        :return: the standard deviation of all the elements of the matrix.
        """
        avg = self.average()
        deviation = 0.0
        for line in self.elements:
            for element in line:
                deviation += (element - avg) ** 2
        deviation /= self.dimensions[0] * self.dimensions[1]
        return deviation**0.5

    def is_coherent(self):
        """
        Determine if the matrix is coherent.  A matrix is coherent if and only if all the lines (sub-lists) of
        elements have the same number of elements which is the number of lines in the dimension tuple and the
        number of sub-lists of elements is the same as the number of columns in the dimension tuple.
        :return: true if the matrix is coherent, false otherwise.
        """
        num_rows = self.dimensions[0]
        num_cols = self.dimensions[1]
        for line in self.elements:
            if len(line) != num_cols:
                return False
        if len(self.elements) != num_rows:
            return False
        return True
