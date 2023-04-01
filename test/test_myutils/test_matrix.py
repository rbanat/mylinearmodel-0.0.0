"""
    Un module qui teste les fonctionnalités de la classe matrix.
"""


from myutils import matrix


M1 = matrix.Matrix([[1,0],[1,0]])
M2 = matrix.Matrix([[21], [20], [19], [18], [17]])
M3 = matrix.Matrix([[1, 2], [3, 4]])
M4 = matrix.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def test_data():
    """
        Teste l'attribut data.
    """
    assert M1.data == [[1, 0], [1, 0]]


def test_get_nb_row():
    """
        Teste la méthode get_nb_row.
    """
    assert M1.get_nb_row() == 2
    assert M2.get_nb_row() == 5


def test_get_nb_col():
    """
        Teste la méthode get_nb_col.
    """
    assert M1.get_nb_col() == 2
    assert M2.get_nb_col() == 1


def test_get_size():
    """
        Teste la méthode get_size.
    """
    assert M1.get_size() == (2,2)
    assert M2.get_size() == (5,1)


def test_zeros():
    """
        Teste la méthode zeros.
    """
    assert matrix.Matrix.zeros(2,1).data == [[0], [0]]


def test_ones():
    """
        Teste la fonction ones.
    """
    assert matrix.Matrix.ones(2,1).data == [[1], [1]]


def test_eye():
    """
        Teste la fonction eye.
    """
    assert matrix.Matrix.eye(3).data == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_copy():
    """
        Teste la fonction copy.
    """
    m_copy = M1.copy()
    assert m_copy.data == M1.data
    m_copy.data[0][0] = 0
    assert M1.data == [[1, 0], [1, 0]]


def test_is_square():
    """
        Teste la méthode is_square.
    """
    assert M1.is_square() is True
    assert M2.is_square() is False


def test_transpose():
    """
        Teste la méthode transpose.
    """
    assert M2.transpose().data == [[21, 20, 19, 18, 17]]
    assert M2.data == [[21], [20], [19], [18], [17]]


def test_sub_matrix_square():
    """
        Teste la méthode sub_matrix_square.
    """
    assert M3.sub_matrix_square(1,1).data == [[1]]


def test_cofactor():
    """
        Teste la méthode cofactor.
    """
    assert M1.cofactor(1,1) == 1
    assert M1.cofactor(0,1) == -1
    assert M3.cofactor(1,1) == 1
    assert M3.cofactor(0,1) == -3
    assert M4.cofactor(2,2) == 1


def test_determinant():
    """
        Teste la méthode déterminant.
    """
    assert M1.determinant() == 0
    assert M3.determinant() == -2
    assert M4.determinant() == 1


def test_comatrix():
    """
        Teste la méthode comatrix.
    """
    assert M3.comatrix().data == [[4, -3], [-2, 1]]


def test_inverse():
    """
        Teste la méthode inverse.
    """
    assert M1.inverse() == "Error : The matrix is not inversible !"
    assert M3.inverse().data == [[-2, 1], [3/2, -1/2]]
    assert M4.inverse().data == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_add():
    """
        Teste la méthode add.
    """
    assert M4.add(M4).data == [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
    assert M4.add(1).data == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]


def test_product():
    """
        Teste la méthode product.
    """
    assert M4.product(-2).data == [[-2, 0, 0], [0, -2, 0], [0, 0, -2]]
    assert M1.product(M3).data == [[1, 2], [1, 2]]
    assert M3.product(M1).data == [[3, 0], [7, 0]]
