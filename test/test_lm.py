"""
    Un module qui teste les fonctionnalités de la classe LinearModel.
"""


from myutils.matrix import Matrix
from myutils.mypandas import file_to_data, del_columns, split
from mylinearmodel.lm import LinearModel
from mylinearmodel.ols import OrdinaryLeastSquares


Xtrain = Matrix([[21], [20], [19],[18], [17]])
ytrain = Matrix([[17.5], [17.3], [16], [16.3], [15.6]])
Xtest = Matrix([[16], [15]])
ytest = Matrix([[16], [15.3]])


model = LinearModel()
model_ols = OrdinaryLeastSquares(fit_intercept=False)


def test_fit_intercept():
    """
        Teste l'attribut fit_intercept.
    """
    assert model.fit_intercept is True


def test_type():
    """
        Teste l'attribut type.
    """
    assert model.type == "Linear Model"


def test_beta():
    """
        Teste l'attribut beta.
    """
    model.beta = 2
    assert model.beta == 2


def test_intercept():
    """
        Teste l'attribut intercept.
    """
    model.intercept = 4
    assert model.intercept == 4


def test_get_intercept():
    """
        Teste la méthode get_intercept.
    """
    model.intercept = 5
    assert model.get_intercept() == 5


def test_get_coeffs():
    """
        Teste la méthode get_coeffs.
    """
    model.beta = 5
    assert model.get_coeffs() == 5


model_ols.fit(Xtrain, ytrain)


def test_fit():
    """
        Teste la méthode fit.
    """
    beta = model_ols.beta.data
    assert round(beta[0][0], 2) == 0.87

    intercept = model_ols.intercept
    assert intercept == 0


def test_predict():
    """
        Teste la méthode predict.
    """
    pred = model_ols.predict(Xtrain).data
    assert round(pred[0][0], 2) == 18.24
    assert round(pred[1][0], 2) == 17.37
    assert round(pred[2][0], 2) == 16.50
    assert round(pred[3][0], 2) == 15.63
    assert round(pred[4][0], 2) == 14.76


def test_get_residuals():
    """
        Teste la méthode get_residuals.
    """
    res = model_ols.get_residuals(Xtrain, ytrain)
    assert round(res[0], 2) == -0.74
    assert round(res[1], 2) == -0.07
    assert round(res[2], 2) == -0.5
    assert round(res[3], 2) == 0.67
    assert round(res[4], 2) == 0.84


def test_ssr():
    """
        Teste la méthode ssr.
    """
    assert round(model_ols.ssr(Xtrain, ytrain), 2) == 1.94


def test_sst():
    """
        Teste la méthode ssr.
    """
    assert round(model_ols.sst(ytrain), 2) == 1370.59


def test_sse():
    """
        Teste la méthode ssr.
    """
    assert round(model_ols.sse(Xtrain, ytrain), 2) == 1368.65


data = file_to_data("mylinearmodel/fuel2001.txt", ' ')
data_train = del_columns(data, 'State')
(Xtrain2, ytrain2, Xtest2, ytest2) = split(data_train, 'FuelC', 1)

Xtrain2 = Matrix(Xtrain2)
ytrain2 = Matrix(ytrain2)
model_ols2 = OrdinaryLeastSquares(fit_intercept=False)
model_ols2.fit(Xtrain2, ytrain2)


def test_determination_coefficient():
    """
        Teste la méthode determination_coefficient.
    """
    assert round(model_ols2.determination_coefficient(Xtrain2, ytrain2), 4) == 0.9898


def test_adjusted_determination_coefficient():
    """
        Teste la méthode adjusted_determination_coefficient.
    """
    assert round(model_ols2.adjusted_determination_coefficient(Xtrain2, ytrain2), 4) == 0.9885


def test_fisher_test():
    """
        Teste la méthode fisher_test.
    """
    fstat = model_ols2.fisher_test(Xtrain2, ytrain2)
    assert round(fstat, 1) == 731.2


def test_student_test():
    """
        Teste la méthode student_test.
    """
    tstat = model_ols2.student_test(Xtrain2, ytrain2, 'Drivers')[1]
    assert round(tstat, 1) == 4.4
