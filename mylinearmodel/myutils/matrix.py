"""
    Un module avec des fonctions de manipulation de matrice.
"""


class	Matrix():
    """
        Ceci est une matrice
    """


    def __init__(self, data):
        self.data = data


    def get_nb_row(self):
        "Retourne le nombre de ligne de la matrice self."
        return len(self.data)


    def get_nb_col(self):
        """
            Retourne le nombre de colonne de la matrice self.
        """
        return len(self.data[0])


    def get_size(self):
        """
            Retourne la taille de la matrice self.
        """
        return (self.get_nb_row(), self.get_nb_col())


    @staticmethod
    def zeros(row, col):
        """
            Retourne la matrice nulle de taille (row, col).
        """
        data = [[0 for j in range (0,col)] for i in range (0,row)]
        return Matrix(data)


    @staticmethod
    def ones(row, col):
        """
            Retourne la matrice dont les termes sont que des 1 de taille (row, col).
        """
        data = [[1 for j in range (0,col)] for i in range (0,row)]
        return Matrix(data)


    @staticmethod
    def eye(len_id):
        """
            Retourne la matrice identité de taille len_id.
        """
        identity = Matrix.zeros(len_id,len_id)
        for i in range (0,len_id):
            for j in range (0,len_id):
                if i == j :
                    identity.data[i][j] = 1
        return identity


    def copy(self):
        """
            Retourne une copie de la matrice self.
        """
        (row, col) = self.get_size()
        cop = Matrix.zeros(row, col)
        for i in range (0, row):
            for j in range (0, col):
                temp = self.data[i][j]
                cop.data[i][j] = temp
        return cop


    def is_square(self):
        """
            Vérifie si la matrice self est une matrice carrée.
        """
        return self.get_nb_row() == self.get_nb_col()


    def transpose(self):
        """
            Retourne la transposée de la matrice self.
        """
        col = self.get_nb_row()
        row = self.get_nb_col()
        data_transpose = Matrix.zeros(row,col)

        for j in range (0,row):
            for i in range (0,col):
                temp = self.data[i][j]
                data_transpose.data[j][i] = temp

        return data_transpose


    def sub_matrix_square(self, i, j):
        """
            Retourne la sous-matrice d'indice i et j.
        """
        (row,col) = self.get_size()

        if row == 1:
            return self.copy()

        sub_m = Matrix.zeros(row-1, col-1)
        for k in range (0, row-1):
            if k < i :
                sub_m.data[k] = self.data[k][0:j] + self.data[k][j+1:col]
            if k >= i :
                sub_m.data[k] = self.data[k+1][0:j] + self.data[k+1][j+1:col]

        return sub_m


    def cofactor(self, i , j):
        """
            Retourne le cofacteur d'indice i et j de la matrice self.
        """
        sub_m = self.sub_matrix_square(i, j)
        if sub_m.data == self.data:
            return 1
        if (i+j)%2 == 0:
            return sub_m.determinant()
        return (-1)*sub_m.determinant()


    def determinant(self):
        """
            Retourne le déterminant selon l'algortihme de Gauss de la matrice self.
        """
        if not self.is_square() :
            return "Error : The determinant can only be calculated for a square matrix !"

        len_row = self.get_nb_row()
        if len_row == 1 :
            return self.data[0][0]

        det = 0
        for k in range (0,len_row):
            det += self.data[0][k]*self.cofactor(0,k)
        return det


    def comatrix(self):
        """
            Retourne la comatrice de la matrice self.
        """
        if not self.is_square():
            return "Error"

        len_row = self.get_nb_row()
        com_m = Matrix.ones(len_row, len_row)
        for i in range (0,len_row):
            for j in range (0,len_row):
                com_m.data[i][j] = self.cofactor(i,j)

        return com_m


    def inverse(self):
        """
            Retourne l'inverse de la matrice self.
        """
        if (not self.is_square()) or (self.determinant() == 0):
            return "Error : The matrix is not inversible !"

        det = self.determinant()
        inv = self.comatrix().transpose()

        len_row = inv.get_nb_row()
        for i in range (0,len_row):
            for j in range (0,len_row):
                inv.data[i][j] /= det
        return inv


    def add(self, other):
        """
            Retourne la somme entre la matrice self et other.
        """

        (row, col) = self.get_size()
        if isinstance(other, (float, int)):
            result = self.copy()
            for i in range (0, row):
                for j in range (0,col):
                    result.data[i][j] = self.data[i][j] + other
            return result

        if (row, col) != other.get_size():
            return "Error : Both matrix must have the same size !"

        result = Matrix.zeros(row, col)
        for i in range (0,row):
            for j in range (0,col):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result


    def product(self, other):
        """
            Retourne le produit entre la matrice self et other.
        """
        if not isinstance(other, (float, int, Matrix)) :
            return "Error : The argument must be type float, int or Matrix !"

        if isinstance(other, (float, int)) :
            result = self.copy()
            (row, col) = result.get_size()
            for i in range (0,row):
                for j in range (0,col):
                    result.data[i][j] *= other
            return result

        len_col_self = self.get_nb_col()
        if len_col_self != other.get_nb_row():
            return "Error : col's number of matrix 1 must match row's number of matrix 2 !"

        len_row = self.get_nb_row()
        len_col = other.get_nb_col()
        result = Matrix.zeros(len_row, len_col)
        for i in range (0,len_row):
            for j in range (0,len_col):
                temp = 0
                for k in range (0,len_col_self):
                    temp += self.data[i][k]*other.data[k][j]
                result.data[i][j] = temp

        return result
