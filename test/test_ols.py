"""
    Un module qui teste les fonctionnalités de la classe OrdinaryLeastSquares.
"""

from myutils.matrix import Matrix
from mylinearmodel.ols import OrdinaryLeastSquares


Xtrain = Matrix([[21], [20], [19],[18], [17]])
ytrain = Matrix([[17.5], [17.3], [16], [16.3], [15.6]])
Xtest = Matrix([[16], [15]])
ytest = Matrix([[16], [15.3]])


model1 = OrdinaryLeastSquares(fit_intercept=True)
model1.fit(Xtrain, ytrain)
model2 = OrdinaryLeastSquares(fit_intercept=False)
model2.fit(Xtrain, ytrain)


def test_fit_intercept():
    """
        Teste l'attribut fit_intercept.
    """
    assert model1.fit_intercept is True
    assert model2.fit_intercept is False


def test_type():
    """
        Teste l'attribut type.
    """
    assert model1.type == 'Ordinary Least Squares'
    assert model2.type == 'Ordinary Least Squares'


def test_intercept():
    """
        Teste l'attribut intercept.
    """
    model1.fit(Xtrain, ytrain)
    model2.fit(Xtrain, ytrain)
    assert round(model1.intercept[0], 2) == 7.42
    assert model2.intercept == 0


def test_beta():
    """
        Teste l'attribut beta.
    """
    assert round(model1.beta.data[0][0], 2) == 0.48
    assert round(model2.beta.data[0][0], 2) == 0.87
