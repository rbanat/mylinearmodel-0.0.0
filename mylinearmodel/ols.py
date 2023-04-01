"""
    Imite la classe OrdinaryLeastSquares de sklearn.
"""


from myutils.matrix import Matrix
from mylinearmodel.lm import LinearModel


class   OrdinaryLeastSquares(LinearModel):
    """
        Modèle de régression linéaire selon la méthode des moindres carrées ordinaires.
    """


    def __init__(self, fit_intercept=True):
        super().__init__()
        self.fit_intercept = fit_intercept
        self.type = 'Ordinary Least Squares'


    def fit(self, xtrain, ytrain):
        """
            Apprentissage du modèle sur les ensembles xtrain et ytrain.
        """

        if not isinstance(xtrain, Matrix) or not isinstance(ytrain, Matrix):
            return "Error : Xtrain and ytrain must be matrix !"

        xbis = xtrain.copy()
        ybis = ytrain.copy()
        if isinstance(xtrain.data[0][0], str):
            xbis.data = xbis.data[1:]
            ybis.data = ybis.data[1:]

        if self.fit_intercept:
            row = ybis.get_nb_row()
            for i in range (0,row):
                xbis.data[i] = [1] + xbis.data[i]

        x_transpose = xbis.transpose()
        emc = x_transpose.product(xbis)
        emc = emc.inverse()

        if isinstance(emc, str):
            self.beta = emc
            return self

        emc = emc.product(x_transpose).product(ybis)

        if self.fit_intercept:
            self.intercept = emc.data[0]
            emc.data = emc.data[1:]
            self.beta = emc
        else:
            self.intercept = 0.0
            self.beta = emc

        return self
