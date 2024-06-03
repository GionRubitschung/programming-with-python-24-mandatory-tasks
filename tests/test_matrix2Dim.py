import pytest
from matrix.matrix2Dim import Matrix2Dim


def test_initialize():
    matrix = Matrix2Dim((3, 3))
    matrix.initialize(0)
    assert matrix.elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_transpose():
    matrix = Matrix2Dim((3, 2), [[1, 2], [3, 4], [5, 6]])
    transposed_matrix = matrix.transpose()
    assert transposed_matrix.elements == [[1, 3, 5], [2, 4, 6]]


def test_is_symmetric():
    symmetric_matrix = Matrix2Dim((3, 3), [[1, 2, 3], [2, 4, 5], [3, 5, 6]])
    assert symmetric_matrix.is_symmetric() is True

    non_symmetric_matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert non_symmetric_matrix.is_symmetric() is False


def test_total():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.total() == 45


def test_average():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.average() == 5.0


def test_stddeviation():
    matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.stddeviation() == pytest.approx(2.581988897471611)


def test_is_coherent():
    coherent_matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert coherent_matrix.is_coherent() is True

    incoherent_matrix = Matrix2Dim((3, 3), [[1, 2, 3], [4, 5], [7, 8, 9]])
    assert incoherent_matrix.is_coherent() is False
