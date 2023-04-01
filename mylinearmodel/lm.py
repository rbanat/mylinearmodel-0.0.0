"""
    Imite la classe LinearModel de sklearn.
"""


import matplotlib.pyplot as plt
from myutils.matrix import Matrix
from myutils.mypandas import columns_name, get_index
from myutils.mystats import median, first_quarter, third_quarter, pstud, pfish


class	LinearModel():
    """
        Modèle de régression linéaire.
    """

    def __init__(self):
        self.fit_intercept = True
        self.beta = 0
        self.penalty = 0
        self.intercept = 0
        self.type = "Linear Model"


    def get_intercept(self):
        """
            Retourne la constante du modèle.
        """
        return self.intercept


    def get_coeffs(self):
        """
            Retourne l'estimateur beta du modèle.
        """
        if isinstance(self.beta, (float, int)):
            return self.beta
        return self.beta.data


    def predict(self, xtest):
        """
            Retourne la prédiction sur les données xtest.
        """
        if isinstance(xtest.data[0][0], str):
            xbis = Matrix(xtest.data[1:])
        else:
            xbis = xtest.copy()

        if self.fit_intercept:
            row = xbis.get_nb_row()
            for i in range (0, row):
                xbis.data[i] = [1] + xbis.data[i]

        if not self.fit_intercept:
            pred = xbis.product(self.beta)
            return pred

        beta = self.beta.copy()
        beta.data = [[0.0]] + self.beta.data
        pred = xbis.product
        return xbis.product(beta).add(self.intercept[0])


    def get_residuals(self, xtrain, ytrain):
        """
            Retourne les résidus du modèle sous forme d'une liste.
        """
        if isinstance(ytrain.data[0][0], str):
            ybis = Matrix(ytrain.data[1:])
        else:
            ybis = ytrain.copy()
        ypred = self.predict(xtrain)
        len_y = ypred.get_nb_row()
        res = []
        for i in range(0,len_y):
            res += [ybis.data[i][0] - ypred.data[i][0]]
        return res


    def ssr(self, xtrain, ytrain):
        """
            Retourne la somme des carrés résiduels.
        """
        ypred = self.predict(xtrain).copy()
        if isinstance(ytrain.data[0][0], str):
            ybis = Matrix(ytrain.data[1:])
        else:
            ybis = ytrain.copy()
        len_y = ypred.get_nb_row()

        out = 0
        for k in range (0, len_y):
            temp = ypred.data[k][0] - ybis.data[k][0]
            out += temp*temp

        return out


    def sst(self, ytrain):
        """
            Retourne la somme des carrés totale.
        """
        if isinstance(ytrain.data[0][0], str):
            ybis = Matrix(ytrain.data[1:])
        else:
            ybis = ytrain.copy()
        len_y = ybis.get_nb_row()

        out = 0
        if not self.fit_intercept:
            for k in range (0, len_y):
                temp = ybis.data[k][0]
                out += temp*temp

        else:
            y_bar = 0
            for k in range (0, len_y):
                y_bar += ybis.data[k][0]/len_y
            for k in range (0, len_y):
                temp = ybis.data[k][0] - y_bar
                out += temp*temp

        return out


    def sse(self, xtrain, ytrain):
        """
            Retourne la somme des carrés estimés.
        """
        if isinstance(ytrain.data[0][0], str):
            ybis = Matrix(ytrain.data[1:])
        else:
            ybis = ytrain.copy()
        len_y = ybis.get_nb_row()
        ypred = self.predict(xtrain).copy()

        out = 0
        if not self.fit_intercept:
            for k in range (0, len_y):
                temp = ypred.data[k][0]
                out += temp*temp

        else:
            y_bar = 0
            for k in range (0, len_y):
                y_bar += ybis.data[k][0]/len_y
            for k in range (0, len_y):
                temp = ypred.data[k][0] - y_bar
                out += temp*temp

        return out


    def determination_coefficient(self, xtrain, ytrain):
        """
            Retourne le coefficient de détermination du modèle.
        """
        rsquared = 1 - (self.ssr(xtrain, ytrain)/self.sst(ytrain))
        return rsquared


    def adjusted_determination_coefficient(self, xtrain, ytrain):
        """
            Retourne le coefficient de détermination ajusté du modèle.
        """
        rsquared = self.determination_coefficient(xtrain, ytrain)
        if isinstance(xtrain.data[0][0], str):
            len_x = len(xtrain.data)-1
        else:
            len_x = len(xtrain.data)

        rank = len(xtrain.data[0])
        if self.fit_intercept:
            rank += 1
            return 1-((len_x-1)/(len_x-rank))*(1-rsquared)

        return 1-((len_x-1)/(len_x-rank-1))*(1-rsquared)


    def fisher_test(self, xtrain, ytrain):
        """
            Retourne la statistique de test de Fisher.
        """
        rsquared = self.determination_coefficient(xtrain,ytrain)

        if isinstance(xtrain.data[0][0], str):
            len_x = len(xtrain.data)-1
        else:
            len_x = len(xtrain.data)

        rank = len(xtrain.data[0])
        if self.fit_intercept:
            rank += 1
            return ((len_x-rank)/(rank-1))*(rsquared/(1-rsquared))

        return ((len_x-rank)/rank)*(rsquared/(1-rsquared))


    def student_test(self, xtrain, ytrain, var):
        """
            Retourne l'erreur associé à l'écart-type la statistique de test de Student.
        """
        xbis = Matrix(xtrain.data[1:])
        row = xbis.get_nb_row()
        if self.fit_intercept:
            for k in range (0,row):
                xbis.data[k] = [1] + xbis.data[k]

        rank = len(xbis.data[0])
        sigma = (self.ssr(xtrain, ytrain)/(row-rank))**(1/2)

        if var == 'Intercept':
            j = 0
            beta_j = self.intercept[0]
        else:
            if self.fit_intercept:
                j = get_index(xtrain.data, var)+1
                beta_j = self.beta.data[j-1][0]
            else:
                j = get_index(xtrain.data, var)
                beta_j = self.beta.data[j][0]

        if self.type == 'Ordinary Least Squares':
            sig_j = sigma * (xbis.transpose().product(xbis).inverse().data[j][j])**(1/2)
        if self.type == 'Ridge':
            penalty_id = Matrix.eye(xbis.get_nb_col()).product(self.penalty)
            sig_j = xbis.transpose().product(xbis).add(penalty_id).inverse().data[j][j]
            sig_j = sigma*(sig_j**(1/2))

        return sig_j, beta_j/sig_j


    def plot_prediction(self, xdata, ydata):
        """
            Retourne le graphe qui représente les valeurs estimés en fonction des valeurs réelles.
        """
        y_temp = self.predict(xdata).data
        if isinstance(ydata.data[0][0], str):
            ypred_temp = ydata.data[1:]
        else:
            ypred_temp = ydata.data

        ybis = []
        ypred = []
        for elt in y_temp:
            ybis += elt
        for elt in ypred_temp:
            ypred += elt

        axplot = plt.subplots()[1]
        axplot.scatter(ybis, ypred, marker='o', c='blue', edgecolors='none', label='Y predicted')
        axplot.plot([min(ybis),max(ybis)], [min(ybis),max(ybis)],c='hotpink',ls="-", label='Y')
        axplot.legend()
        axplot.set_ylabel("Predicted")
        axplot.set_xlabel("Measured")
        plt.show()


    def summary(self, xtrain, ytrain):
        """
            Retourne un résumé de toutes les données obtenues du modèle.
        """
        col = columns_name(xtrain.data)
        rsquared = self.determination_coefficient(xtrain, ytrain)
        r_adjusted = self.adjusted_determination_coefficient(xtrain, ytrain)
        res = self.get_residuals(xtrain,ytrain)
        fstat = self.fisher_test(xtrain, ytrain)
        len_x = len(xtrain.data)-1
        rank = len(xtrain.data[0])
        if self.fit_intercept:
            rank += 1

        print("Variable à expliquer :", ytrain.data[0][0])

        if self.type == 'Ridge':
            print("Model : {}, penalty = {}".format(self.type, self.penalty))
        if self.type == 'Ordinary Least Squares':
            print("Model : {}".format(self.type))

        print("Nb. Obs :", len_x)

        print("\n\nResiduals :")
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Min", "1Q", "Median", "3Q", "Max"))
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(min(res), first_quarter(res), median(res), third_quarter(res), max(res)))

        print("\n\nCoefficients :")

        print("{:<15} {:<23} {:<23} {:<23} {:<23}".format("", "Estimate", "Std. Error", "t value", "Pr(>|t|)"))
        if self.fit_intercept:
            sigma, tstat = self.student_test(xtrain,ytrain,'Intercept')
            print("{:<15} {:<23} {:<23} {:<23} {:<23}".format("(Intercept)", self.intercept[0], sigma, tstat, pstud(tstat, len_x-rank)))
        else:
            print("{:<15}".format("(Intercept)"))

        i = 0
        for elt in col:
            sigma, tstat = self.student_test(xtrain,ytrain,elt)
            print("{:<15} {:<23} {:<23} {:<23} {:<23}".format(elt, self.beta.data[i][0], sigma, tstat, pstud(tstat, len_x-rank)))
            i += 1


        res_std_err = (self.ssr(xtrain, ytrain)/(len_x-rank))**(1/2)
        print("\n\nResidual standard error : {} on {} degrees of freedom".format(res_std_err, len_x-rank))
        print("R-squared : {}, \tAdj. R-squared : {}".format(rsquared, r_adjusted))

        if self.fit_intercept:
            print("F-statistic : {} on {} and {} degrees of freedom, \tp-value : {}".format(fstat, rank-1, len_x-rank, pfish(fstat,rank,len_x-rank)))
        else:
            print("F-statistic : {} on {} and {} degrees of freedom, \tp-value : {}".format(fstat, rank, len_x-rank, pfish(fstat, rank, len_x-rank)))
        print("\n\n")
