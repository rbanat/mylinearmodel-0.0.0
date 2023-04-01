"""
    Imite la classe Ridge de sklearn.
"""


from myutils.matrix import Matrix
from mylinearmodel.lm import LinearModel


class   Ridge(LinearModel):
    """
        Modèle de régression linéaire selon la méthode des moindres carrées ordinaires régularisé.
    """


    def __init__(self, penalty, fit_intercept=True):
        super().__init__()
        self.fit_intercept = fit_intercept
        self.penalty = penalty
        self.type = 'Ridge'


    def fit(self, xtrain, ytrain):
        """
            Apprentissage du modèle sur les ensembles xtrain et ytrain.
        """
        if not isinstance(xtrain, Matrix) or not isinstance(ytrain, Matrix):
            return "Error : Xtrain and ytrain must be matrix !"

        if isinstance(xtrain.data[0][0], str):
            xbis = Matrix(xtrain.data[1:])
            ybis = Matrix(ytrain.data[1:])
        else:
            xbis = xtrain.copy()
            ybis = ytrain.copy()

        if self.fit_intercept:
            row = xbis.get_nb_row()
            for i in range (0,row):
                xbis.data[i] = [1] + xbis.data[i]


        x_transpose = xbis.transpose()
        identity = Matrix.eye(xbis.get_nb_col())
        penalty_id = identity.product(self.penalty)

        ridge = x_transpose.product(xbis)
        ridge = ridge.add(penalty_id)
        ridge = ridge.inverse()

        if isinstance(ridge, str) :
            self.beta = ridge
            return self

        ridge = ridge.product(x_transpose)
        ridge = ridge.product(ybis)

        if self.fit_intercept:
            self.intercept = ridge.data[0]
            ridge.data = ridge.data[1:]
            self.beta = ridge
        else:
            self.intercept = 0.0
            self.beta = ridge

        return self
