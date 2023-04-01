"""
    Un module qui teste les fonctions du module utils.
"""


from myutils import mypandas


data = [['hello', 'world'], [1, 2], [1, 2]]


def test_is_num():
    """
        Teste la fonction is_num.
    """
    assert mypandas.is_num('world') is False
    assert mypandas.is_num('555') is True


def test_columns_name():
    """
        Teste la fonction columns_name.
    """
    assert mypandas.columns_name(data) == ['hello', 'world']


def test_get_index():
    """
        Teste la fonction get_index.
    """
    assert mypandas.get_index(data, 'world') == 1
    assert mypandas.get_index(data, ['hello', 'world']) == [0,1]


def test_del_columns():
    """
        Teste la fonction del_columns.
    """
    assert mypandas.del_columns(data, 'world') == [['hello'], [1], [1]]


def test_get_columns():
    """
        Teste la fonction get_columns.
    """
    assert mypandas.get_columns(data, 'world') == [['world'], [2], [2]]
    assert mypandas.get_columns(data, ['hello', 'world']) == data


def test_split():
    """
        Teste la fonction split.
    """
    assert mypandas.split(data, 'world', 0.5) == ([['hello'], [1]], [['world'], [2]], [[1]], [[2]])
