import pytest
from matrix.matrix2Dim import Matrix2Dim
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "dimensions,value,elements,expectation",
    [
        ((3, 3), 0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], does_not_raise()),
        ((3, 3), None, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], does_not_raise()),
        ((0, 3), 0, None, pytest.raises(ValueError)),
        ((3, 3), "a", None, pytest.raises(TypeError)),
        ((3, 3), None, [1, 2, 3], pytest.raises(ValueError)),
        ((3, 3), None, [[1, 2], [3, 4], [5, 6]], pytest.raises(ValueError)),
        ((3, 3), None, [[1, 2, 3], [4, 5, 6]], pytest.raises(ValueError)),
        ((3, 3), None, [[1, 2, 3], [4, 5, 6], [7, 8, "9"]], pytest.raises(ValueError)),
    ],
)
def test_initialize(dimensions, value, elements, expectation):
    with expectation:
        matrix = Matrix2Dim(dimensions, elements)
        assert matrix.dimensions == dimensions
        assert matrix.elements == elements
        if value is not None:
            matrix.initialize(value)
            assert matrix.elements == elements


def test_transpose():
    matrix = Matrix2Dim((3, 2), [[1, 2], [3, 4], [5, 6]])
    transposed_matrix = matrix.transpose()

    assert Matrix2Dim((2, 3), [[1, 3, 5], [2, 4, 6]]) == transposed_matrix


@pytest.mark.parametrize(
    "matrix,symmetric",
    [
        (Matrix2Dim((3, 3), [[1, 2, 3], [2, 4, 5], [3, 5, 6]]), True),
        (Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), False),
    ],
)
def test_is_symmetric(matrix, symmetric):
    assert matrix.is_symmetric() == symmetric


def test_total():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.total() == 45


def test_average():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.average() == 5.0


def test_stddeviation():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.stddeviation() == pytest.approx(2.581988897471611)


@pytest.mark.parametrize(
    "matrix,coherent",
    [
        (Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), True),
        (Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8]]), False),
    ],
)
def test_is_coherent(matrix, coherent):
    assert matrix.is_coherent() == coherent


@pytest.mark.parametrize(
    "matrix1,matrix2,result",
    [
        (
            Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            True,
        ),
        (
            Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            Matrix2Dim((2, 2), [[1, 2], [3, 4]]),
            False,
        ),
        (
            ((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            False,
        ),
    ],
)
def test_equals(matrix1, matrix2, result):
    assert (matrix1 == matrix2) == result


@pytest.mark.parametrize(
    "index,result,expectation",
    [
        (0, [1, 2, 3], does_not_raise()),
        ((1, 1), 5, does_not_raise()),
        (3, None, pytest.raises(IndexError)),
        ((1, 3), None, pytest.raises(IndexError)),
        ("3", None, pytest.raises(TypeError)),
        ((1, "3"), None, pytest.raises(TypeError)),
        ((1, "3"), None, pytest.raises(TypeError)),
    ],
)
def test_getitem(index, result, expectation):
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with expectation:
        assert matrix[index] == result


def test_str():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_output = "(3, 3)\n| 1 || 2 || 3 |\n| 4 || 5 || 6 |\n| 7 || 8 || 9 |\n"
    assert str(matrix) == expected_output
