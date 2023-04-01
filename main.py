"""
    Un programme qui permet de tester les outils implémentés sur les données.
"""


from myutils.matrix import Matrix
from myutils.mypandas import file_to_data, del_columns, split
from mylinearmodel.ols import OrdinaryLeastSquares
from mylinearmodel.ridge import Ridge

if __name__ == "__main__":
    data = file_to_data("mylinearmodel/fuel2001.txt", ' ')
    data_train = del_columns(data, 'State')
    (Xtrain, ytrain, Xtest, ytest) = split(data_train, 'FuelC', 1)

    M_Xtrain = Matrix(Xtrain)
    M_Xtest = Matrix(Xtest)
    M_ytrain = Matrix(ytrain)
    M_ytest = Matrix(ytest)


    print("\033[93m", "\nEtape 1. Apprentissage du modèle sur le train set", "\033[0m")
    model_ols = OrdinaryLeastSquares(fit_intercept=True)
    model_ridge = Ridge(penalty=0, fit_intercept=True)

    model_ols.fit(M_Xtrain, M_ytrain)
    model_ridge.fit(M_Xtrain, M_ytrain)

    print("\033[93m", "\nEtape 2. Résumé de la régression linéaire\n", "\033[0m")

    print("\033[93m", "a) Pour le modèle Ordinary Least Squares avec constante :", "\033[0m")
    model_ols.summary(M_Xtrain, M_ytrain)

    print("\033[93m",  "b) Pour le modèle Ridge avec constante de penlaty 0 :", "\033[0m")
    model_ridge.summary(M_Xtrain, M_ytrain)


    print("\033[93m", "Etape 3. Visualisation de la prédiction", "\033[0m")
    model_ols.plot_prediction(M_Xtrain, M_ytrain)
    model_ridge.plot_prediction(M_Xtrain, M_ytrain)
